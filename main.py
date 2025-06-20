
def get_book_text(filepath):

    with open(filepath) as f:
              file_contents = f.read()
              return file_contents

def get_book_words(file_contents):
      list = file_contents.split()
      num_words = len(list)
      print(f"{num_words} words found in the document")

def main():
       
    x = get_book_text("books/frankenstein.txt")
    get_book_words(x)

main()