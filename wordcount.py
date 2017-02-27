# put your code here.
def word_count(filepath):
    """Takes a filename as input and prints word/count."""
    
    unique_words = {} #creates empty dictionary
    openfile = open(filepath)
    
    for line in openfile:
        line = line.rstrip() #removes extra character whitespace from end of each line
        words = line.split(" ")
        for word in words:
            unique_words[word] = unique_words.get(word, 0) + 1 
            #line above finds value of key or substitues default, increments by 1, and stores

    for word, count in unique_words.iteritems():  #iteritems a lazy evaluation of unique words dictionary for looping
        print word, count  #prints unpacked tuple


word_count("test.txt")