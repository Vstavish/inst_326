""" Sort books by Library of Congress call number. """
from argparse import ArgumentParser
import re
import sys

# replace this comment with your implementation of the Book class

def book():

     """ defines attributes of the book and associated call number"""

def __init__(self, callname, title, author):
        callname.callname = ("Q2044.J3 C43 2000") 
        title.title = ("Re-visiting Hong Kong paradise : a study of Japanese net surfers")
        author.author = ("Cheung, Sidney C. H.")
    
"""orders the books by their call number using regex"""

def __lt__(self, other):
        self.regex = r"(?:[A-Za-z]{1,}\s[A-Za-z]{1,},)"
        self.matches = re.finditer(regex, callname.callname, re.MULTILINE)
        other.matches = ("")
        if self.matches > other.matches:
            print("TRUE")
        if self.matches < other.matches:
            print("FALSE")

"""Returns the string that results in the instance of a book title, call number and author name"""

def __repr__(self):
        self.__repr__ = (callname + ", " + title + ", " + author)

"""Opens a file of all teh books awith thei associated information"""

def read_books(self):
        self.sample = ("books.tsv")




# replace this comment with your implementation of the read_books() function
def print_books(books):
    """ Print information about each book, in order. """
    for book in sorted(books):
        print(book)
def main(filename):
    """ Read book information from a file, sort the books by call number,
    and print information about each book. """
    books = read_books(filename)
    print_books(books)
def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser(arglist)
    parser.add_argument("filename", help="file containing book information")
    return parser.parse_args(arglist)
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)