word_count_map = {}

# Open file
with open("./hw2_data.txt", "r") as file:
    # Read file line by line
    for line in file:
        # print("line: ", type(line))
        word = line.strip()
        if word not in word_count_map:
            word_count_map[word] = 1
        else:
            word_count_map[word] += 1

# Display total unique words
print("Total unique words:", len(word_count_map))

# Display word counts
print("Word counts:")
for word, count in word_count_map.items():
    print(word + ": ", count)
