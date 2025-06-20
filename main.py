import sys
from stats import get_book_words, lower, char_set, init_dict , update_dict, sort, sort_on

def get_book_text(filepath):

    with open(filepath) as f:
              file_contents = f.read()
              return file_contents

def main():

    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    x = get_book_text(filepath)
    
    y = lower(x)
    z = char_set(y)
    aa = init_dict(z)
    ab = update_dict(aa,y)
    ac = sort(ab)
    ac.sort(reverse=True, key=sort_on)

    print("=====================BOOKBOT=====================")
    print(f"Analyzing book found at {filepath}")
    print("------------------- Word Count ------------------")
    get_book_words(x)
    print("-----------------Character Count-----------------")
    for i in range(0, len(ac)):
        char = ac[i]["char"]
        num = ac[i]["num"]
        print(f"{char}: {num}")
    print("=====================END=========================")
main()