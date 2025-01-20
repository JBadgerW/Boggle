"""
00 01 02 03
04 05 06 07
08 09 10 11
12 13 14 15

Y  L  O  M
A  T  E  T
I  R  A  S
S  E  E  C
"""
neighbors = {
    0: (1, 4, 5),
    1: (2, 0, 4, 5, 6),
    2: (3, 1, 5, 6, 7),
    3: (2, 6, 7),
    4: (5, 1, 0, 8, 9),
    5: (6, 2, 1, 0, 4, 8, 9, 10),
    6: (7, 3, 2, 1, 5, 9, 10, 11),
    7: (3, 2, 6, 10, 11),
    8: (9, 5, 4, 12, 13),
    9: (10, 6, 5, 4, 8, 12, 13, 14),
    10: (11, 7, 6, 5, 9, 13, 14, 15),
    11: (7, 6, 10, 14, 15),
    12: (13, 9, 8),
    13: (14, 10, 9, 8, 12),
    14: (15, 11, 10, 9, 13),
    15: (11, 10, 14)
}

board = {
    0: "y",
    1: "l",
    2: "o",
    3: "m",
    4: "a",
    5: "t",
    6: "e",
    7: "t",
    8: "i",
    9: "r",
    10: "a",
    11: "s",
    12: "s",
    13: "e",
    14: "e",
    15: "c"
}

def explore(position, visited_positions, word_length, temp_words_found, boggle_words):
    visited_positions.append(position)
    if len(visited_positions) == word_length:
        potential_word = make_word(visited_positions)
        if potential_word in boggle_words:
            temp_words_found.add(potential_word)
        visited_positions.pop()
    else:
        for neighbor in neighbors[position]:
            if neighbor not in visited_positions:
                explore(neighbor, visited_positions, word_length, temp_words_found, boggle_words)
        visited_positions.pop()

def make_word(positions):
    letters = [board[position] for position in positions]
    word = "".join(letters)
    return word

def main():
    for num_letters in range(3, 17):
        print(f"Words of {num_letters} letters...")
        dictionary_file = f"words_{num_letters}_letters.txt"
        truncated_file = f"truncated_words_{num_letters}_letters.txt"

        with open(dictionary_file, "r") as word_file:
            boggle_words = set(word_file.readlines())
        boggle_words = [word.strip() for word in boggle_words]

        for key in neighbors:
            explore(key, [], num_letters, temp_words_found, boggle_words)

            found_words_by_num_letters = list(temp_words_found)
            found_words_by_num_letters.sort()

        all_scoring_words.extend(found_words_by_num_letters)
        temp_words_found.clear()
    
        with open("word_output.txt", "w") as output_file:
            scoring_words_for_file = [word + "\n" for word in all_scoring_words]
            output_file.writelines(scoring_words_for_file)

    for word in all_scoring_words:
        print(word)

    print(f"{len(all_scoring_words)=}")


temp_words_found = set()
all_scoring_words = []

if __name__ == "__main__":
    main()