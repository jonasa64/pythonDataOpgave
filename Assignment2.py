import time #import time to access mktime() for time comparison
import string #import string for punctuation to use in punctuation removal
from webget import download #import the download function for downloading the BobRoss.txt


#function to remove punctuation
def rem_punct(str):
    punct = string.punctuation
    no_punct = ''
    for char in str: #for each character in the string, check if its not a punctioation. If so - add it to the return string 
       if char not in punct:
           no_punct = no_punct + char

    return(no_punct)


class time_comp: # class initiated by a datetime format
    
    def timedelim(delims):
        delimlist = ["YYYY","DD","MM","hh","mm","ss"] #List of datetime-delimiters

        delimdict = {}
        for delim in delimlist:
            delimdict[delim] = delims.find(delim)
        
        return delimdict
    
    def __init__(self, delims): #initiation - store positions of time-delimiters
        self.comp = False # make sure that set_timeB returns false if not paramaters has been set
        
        format_dict = timedelim(delims)
        
        self.ts_s = format_dict["ss"]
        self.ts_m = format_dict["mm"]
        self.ts_h = format_dict["hh"]
        self.ts_d = format_dict["DD"]
        self.ts_M = format_dict["MM"]
        self.ts_y = format_dict["YYYY"]
        
    def set_timeA(self,time_a): #set a comparison time, and calculate a mktime
        ta = (int(time_a[ts_y:(ts_y+4)]), int(time_a[ts_M:(ts_M+2)]), int(time_a[ts_d:(ts_d+2)]), int(time_a[ts_h:(ts_h+2)]), int(time_a[ts_m:(ts_m+2)]), int(time_a[ts_s:(ts_s+2)]), 0, 0, 0)
        self.mk_a = time.mktime(ta)

    def set_timeB(self,time_b): #set a time to compare, calculate it's mktime and return the mk_a > mk_b evalutation
        tb = (int(time_b[ts_y:(ts_y+4)]), int(time_b[ts_M:(ts_M+2)]), int(time_b[ts_d:(ts_d+2)]), int(time_b[ts_h:(ts_h+2)]), int(time_b[ts_m:(ts_m+2)]), int(time_b[ts_s:(ts_s+2)]), 0, 0, 0)
        self.mk_b = time.mktime(tb)
        
        try:
            self.comp = self.mk_a > self.mk_b
            return self.comp
        except:
            return self.comp

download("https://github.com/HawkDon/Python_Assignment1/raw/master/BobRoss.txt", "BobRoss.txt") #download the BobRoss.txt if it does not already exist

datafile = "BobRoss.txt"
timings = time_comp("YYYY-MM-DDThh:mm:ss.") # declare the time format used in the chatlog 
timings.set_timeA("2015-10-30T05:00:00.") #fixed time for time comparison



users = set() # users set to add users when found - contains only unique users
worddict = {} # worddict dictionary for holding all words from the chatlog as a key, and the number of appearances as value 

with open(datafile) as fp: #open the BobRoss chatlog
    l = 0
    i = 0
    for line in fp: #iterate the lines in the chatlog
        l += 1 #count the lines
        ls = line.split() #split and slice the lines, to retrieve wanted information
        timestring = ls[0] # the time the chatmessage was sent (each line has ONE message -no-wrap)
        usr = ls[1].split(":")[0] #find the username
        msg = line.split(":",3)[3] #find the actual chatline NB: the maxsplit-argument in split() 
        words = rem_punct(msg).split() #remove punctuation and split the chatline into single words
        
        users.add(usr) #add the user to the users set
        
        for word in words: # Increase the word count for each word in the worddict dictionary. If the word doesn't exist, add it
            try:
                worddict[word] += 1
            except:
                worddict[word] = 1
        
        if timings.set_timeB(timestring): #compare the timestring with the fixedtime
            i += 1
    
    mfreq = sorted(worddict,key=worddict.__getitem__)[-1] #sort the words in the worddict by most frequent apperances
    
    print("Lines         :", l)
    print("\"After 05:00\" :", i)
    print("Unique users  :",len(users))
    print("\"RUINED\"      :", worddict["RUINED"])
    print("Most frequent :", mfreq, ":", worddict[mfreq], "times")
