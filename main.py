from stats import get_book_words, lower, init_dict , update_dict

def get_book_text(filepath):

    with open(filepath) as f:
              file_contents = f.read()
              return file_contents

def main():
       
    x = get_book_text("books/frankenstein.txt")
    get_book_words(x)
    y = lower(x)
    z = init_dict(y)
    update_dict(z,x)

main()