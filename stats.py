def get_book_words(file_contents):
      list = file_contents.split()
      num_words = len(list)
      print(f"Found {num_words} total words")

def lower(file_contents):
      lowered = file_contents.lower()
      return lowered

def char_set(lowered):
      char_set = set()
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
      return dict

def sort(dict):
      
      list1 = []
      for entry in dict:
            small_dict = {}
            small_dict["char"] = entry
            small_dict["num"] = dict[entry]
            list1.append(small_dict)
      return(list1)

def sort_on(dict):
      return dict["num"]