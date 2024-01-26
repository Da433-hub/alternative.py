title = "Get rich or die tryin' is a movie starring rapper fifty cent. "

print(''.join(x + y for x, y in zip(title[0::2].upper(), title[1::2].lower()))) # Alternates each individual character's case.

split_title = title.split() # Stores the split string. 

final_title = " " # Stores the string.

# The for loop below alternates the word's case between .upper() and .lower().

for i in range(len(split_title)):
    if i % 2 == 0:
        final_title += split_title[i].upper() + " " # If item index is even, make uppercase
    else:
        final_title += split_title[i].lower() + " "   # Else convert to lowercase

print(final_title)