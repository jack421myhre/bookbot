import sys
from stats import get_num_words, char_count, char_sorted




def main():

  if len(sys.argv) < 2:
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)
  book_path = sys.argv[1]


  book_text = get_book_text(book_path)
  num_words = get_num_words(book_text)
  chars_dict = char_count(book_text)
  char_list = char_sorted(chars_dict)
  print_report(book_path, num_words, char_list)

def get_book_text(file):
  
    with open(file) as f:
      return f.read()



def print_report(book_path, num_words, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in char_list:
      if not i["char"].isalpha():
        continue
      print(f"{i['char']}: {i['num']}")

    print("============= END ===============")



main()