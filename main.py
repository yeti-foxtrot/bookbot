import sys
from stats import get_book_words, lower, char_set, init_dict , update_dict, sort, sort_on

def get_book_text(filepath):

    with open(filepath) as f:
              file_contents = f.read()
              return file_contents

def main():
       
    x = get_book_text("books/frankenstein1.txt")
    
    y = lower(x)
    z = char_set(y)
    aa = init_dict(z)
    ab = update_dict(aa,y)
    ac = sort(ab)
    ac.sort(reverse=True, key=sort_on)

    print("=====================BOOKBOT=====================")
    print("Analyzing book found at books/frankenstein.txt...")
    print("------------------- Word Count ------------------")
    get_book_words(x)
    print("-----------------Character Count-----------------")
    for i in range(0, len(ac)):
        char = ac[i]["char"]
        num = ac[i]["num"]
        print(f"{char}: {num}")
    print("=====================END=========================")
main()