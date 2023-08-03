def word_counter(file_name, search_words):
    word_count={}
    for word in search_words:
        word_count[word] = 0

    with open(file_name, 'r') as file:
        for l in file:
            l = l.strip()
            if l in search_words:
                word_count[l] += 1

    for word, count in word_count.items():
        print(f"{word} -> {count}")

file_name= "input.txt"
search_words =  ["Python", "C", "OOP", "Hello", "Java"]


word_counter(file_name, search_words)