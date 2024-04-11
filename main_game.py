import argparse
import requests
import re
from random import choice
from typeit import typegame
import os
from bs4 import BeautifulSoup
from readchar import readkey

def extract_quotes(author_code:str)->list[str]:
    """extract codes from author"""
    html=requests.get("https://www.azquotes.com/author/"+author_code)
    soup = BeautifulSoup(html.text, 'html.parser')
    quotes = [q.get_text() for q in soup.find_all("a",class_="title")]
    return(quotes)

def clean_up(ac:str)->str:
    """turn the author code to the name of the author"""
    ac = re.sub("[\d]","",ac).replace("-"," ").replace("_"," ").strip()
    return(ac)

def list_of_authors()->dict:
    html=requests.get("https://www.azquotes.com/")
    authorcodes=re.findall("\/author\/(\d+\-\w+)",html.text)
    authors =[clean_up(i) for i in authorcodes]
    return dict(zip(authors, authorcodes))

def author_check(ath_list:list)->str:
    """User types the name of the author until it's viable
    ath_list:list of viable author names"""
    print("Please type the name of the writer")
    el = readkey()
    while el not in ath_list:
        print("{0:<20s}".format(el,end="\n"))
        for name in ath_list:
            if name.startswith(str(el)):
                print("{0:>40s}".format(name),end="\n")
        a=readkey()
        #escape
        if ord(a)==27:
            break
        #backspace
        elif ord(a)==8:
            el=el[:-1]
        else:
            el=el+a
    else:
        print(el)
    #returns the name of the author
    return(el)


def main():
    parser = argparse.ArgumentParser(prog = "Typing Game",description= "A typing game with quotes from various authors.", epilog = "Github: ArisPag")
    parser.add_argument("-author",help = "random|name_of_author:ex. Albert_Camus|None", type = str)
    args = parser.parse_args()
    #dictonary author:author_code
    authors_info = list_of_authors()
    author = args.author
    #if the author is random or specified
    if author:
        author = author.replace("_", " ")
    if author=="random":
        #choose an author randomly
        author = choice(list(authors_info.keys()))
    elif author not in authors_info.keys():
        #the user has to type the name of the author
        authors = list(authors_info.keys())
        author = author_check(authors)
    #extract all of his/her quotes if the author's name is viable
    if authors_info.get(author,0):
        quotes = extract_quotes(authors_info[author])
        #choose one randomly
        quote = choice(quotes)
        #clear the screen and launch the game
        os.system("cls")
        #run the game
        typegame(quote, author)
    #else the user pressed esc when typing the name of the author

if __name__=="__main__":
    main()