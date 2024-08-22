def count_letter(word_list, letter):
    count = 0
    for word in word_list:
        if letter in word:
            count += 1
    print(count)


count_letter(['python', 'c++', 'c', 'scala', 'java'], 'c')
