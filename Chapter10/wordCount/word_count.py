from pathlib import Path

def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        contents = path.read_text(encoding = 'utf-8')
    except FileNotFoundError:
        # print(f"Sorry the file path {filename} does not exist.")
        pass
    else:
        #Cunt the approximate number of  words in the file
        words = contents.split()
        num_word = len(words)
        print(f"The file {filename} has about {num_word} words.")



filenames  =['alice.txt','book2.txt']
for filename in filenames:
    path= Path(filename)
    count_words(path)
