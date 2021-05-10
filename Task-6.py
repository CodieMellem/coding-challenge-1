list_of_words = ["once", "upon", "a", "time"] 
#list_of_words = ["the","quick","brown", "fox", "ate", "my", "chickens"]



def hello(list_of_words):
    longest_words = []
    count = 0

    for i in list_of_words:
        if len(i) >= count:
            count = len(i)
    for i in list_of_words:
        if len(i) == count:
            longest_words.append(i)
    for i in longest_words:
        print(i)


hello(list_of_words)