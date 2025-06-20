def get_book_words(file_contents):
      list = file_contents.split()
      num_words = len(list)
      print(f"{num_words} words found in the document")

def lower(file_contents):
      char_set = set()
      lowered = file_contents.lower()
      for char in lowered:
            char_set.add(char)
      return char_set

def init_dict(char_set):
      dict = {}
      for char in char_set:
            dict[char] = 0
      return(dict)

def update_dict(dict, file_contents):
      for word in file_contents:
            for key in dict:
                  if word == key:
                        dict[key] += 1
      print(dict)
      return dict