import string
from termcolor import colored
from  readchar import readkey
from time import perf_counter
from time import sleep
import sys


def typegame(s, author):
    """A typing game. Input must be a string with english letters"""
    start =perf_counter()
    #number of words
    n_words=len(s.split(" "))
    for i in s:
        if i not in string.printable+"\n":
            s=s.replace(i,"")
    #list of lines
    l=list(filter(bool,s.splitlines()))
#for every sentence
    for k in l:
    #for every letter
        for j in range(0,(len(k)//100)+1):
            #separate the sentence into chunks
            p=list(k[j*100:(j*100)+100])
            #for every character in the part
            for i,char in enumerate(list(p)):
                #the character that must be typed
                p[i]=colored(char,"red","on_white")
                print("\r"+"".join(p),end="")
                while readkey(str(p))!=char:
                    pass
                #paint the character green and go to the next
                p[i]=colored(char,"green")
            #painting the last letter of the line 
            print("\r"+"".join(p),end="")
            print("")
            sys.stdout.flush()
    #words per minute calculation
    wpm = 60*n_words/(perf_counter()-start)
    print("\t-{}".format(author))
    return(wpm)

if __name__=="__main__":
    s = "This is a quote"
    for i in range(5,0,-1):
        print("Game starts in {}".format(i),end = "\r")
        sleep(1)
    else:
        print("\nGo!")
    timer = typegame(s,"Aristeidis")
    print("Completed in : {0:.1f} seconds".format(timer))
    print("Words per minute: {}".format(60*len(s.split())/(timer)))
