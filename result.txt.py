def replace_even_odd(text, word_to_replace, even_replace, odd_replace):
    count = 0
    new_text = []
    for word in text.split():
        if word == word_to_replace:
            count += 1
            if count % 2 == 0:
                new_text.append(even_replace)
            else:
                new_text.append(odd_replace)
        else:
            new_text.append(word)
    return ' '.join(new_text)

# Read the file
try:
    with open('file_to_read.txt', 'r') as file:
        text = file.read()
except FileNotFoundError:
    print("The file 'file_to_read.txt' was not found.")
    exit()

# Count
count_terrible = text.split().count('terrible')
print(f"The word 'terrible' appears {count_terrible} times.")

# Replace
new_text = replace_even_odd(text, 'terrible', 'pathetic', 'marvellous')

# Write the new text to a new file
with open('result.txt', 'w') as file:
    file.write(new_text)

print("The new text has been written to 'result.txt'.")