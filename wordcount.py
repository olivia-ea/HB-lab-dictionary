# put your code here.

def word_count(textfile):
    the_data = open(textfile)
    word_counts = {}
    for line in the_data:
        minus_wspace = line.rstrip()
        list_of_words = minus_wspace.split(' ')
        
        
        for word in list_of_words:
            word_counts[word] = word_counts.get(word, 0) + 1
        
    
    for count_of_word in word_counts:
        print(count_of_word, word_counts[count_of_word])


word_count("twain.txt")