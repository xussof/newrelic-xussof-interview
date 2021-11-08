import os
import time

from nltk import ngrams
from collections import Counter

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

num_common_words = 100
txtfolder = "../txtfolder"
to_replace = "!", ",", ".", "?"

def common_words():
    result = []
    for file in os.listdir(txtfolder):
       with open(os.path.join(txtfolder, file), 'r') as f:
        sentence = f.read().rstrip()
        #Let's clean all special caracters
        for replace in to_replace:
            sentence = sentence.replace(replace, '').lower()
    for n in range(len(sentence.split(' ')), 2, -1):
        phrases = []
        for token in ngrams(sentence.split(), n):
            phrases.append(' '.join(token))
    n = 0
    while n < num_common_words:
        n += 1
        print("The number ",n," most common phrase is",Counter(phrases).most_common(n)[-1])

def common_words_stdin(word):
    print(word)
    
def remove_file(event):
    os.remove(event.src_path)
        
def observer():
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    path = txtfolder
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    
    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    
    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()

def on_created(event):
    print(f"New file found named {event.src_path}. Let's read it")
    common_words()
    remove_file(event)
    
def on_deleted(event):
    print(f"File {event.src_path} sucsessfully deleted!")


if __name__ == "__main__":
    observer()
    #common_words()
