from donlowder import download




download('https://github.com/HawkDon/Python_Assignment1/raw/master/BobRoss.txt', 'BobRoss.txt')


filename = "BobRoss.txt"

def total_lines(filename):
   with open(filename, 'r') as fn:
        data = fn.read()
        num_lines = len(data.splitlines())
        print( num_lines)


def word_cont(filename):
    wordcount = {}


    for word in filename.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    for k, v in wordcount.items():
        print( k, v)
