with open("boggle-word-list.txt", "r") as list_file:
    all_words = list_file.readlines()

word_lists = dict()

for num_letters in range(3, 17):
    print(num_letters)
    #breakpoint()
    word_lists[num_letters] = {word for word in all_words if len(word.strip()) == num_letters}

for key in word_lists:
    filename = f"words_{key}_letters.txt"
    #filename_of_trunc = f"truncated_words_{key}_letters.txt"

    with open(filename, "w") as words_file:
        word_list = list(word_lists[key])
        word_list.sort()
        words_file.writelines(word_list)
    
    # with open(filename_of_trunc, "w") as truncated_words_file:
    #     word_list = list(word_lists[key])
    #     word_list = {word[0:3] + "\n" for word in word_list}
    #     word_list = list(word_list)
    #     word_list.sort()

    #     truncated_words_file.writelines(word_list)



