
def get_num_words(book):

  words = book.split()
  num_words = 0

  for word in words:
    num_words += 1

  return num_words


def char_count(book):
  char_dict = {}

  for c in book:
    lowered = c.lower()
    if lowered in char_dict:
      char_dict[lowered] += 1
    else:
      char_dict[lowered] = 1

  return char_dict


def sort_on(d):
  return d["num"]


def char_sorted(num_chars_dict):
  sorted_list = []
  for ch in num_chars_dict:
    sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list

  


