english_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

morse_chars = ['• ─', '─ • • •', '─ • ─ •', '─ • •', '•', '• • ─ •',
               '─ ─ •', '• • • •', '• •', '• ─ ─ ─', '─ • ─', '• ─ • •',
               '─ ─', '─ •', '─ ─ ─', '• ─ ─ •', '─ ─ • ─', '• ─ •',
               '• • •', '─', '• • ─', '• • • ─', '• ─ ─',
               '─ • • ─', '─ • ─ ─', '─ ─ • •']

text = input("Please insert your written text here: ").upper()

new_text = []
convert = ''
for letter in text:
    if letter in english_letters:
        new_text.append(english_letters.index(letter))
    else:
        new_text.append(letter)

for i in new_text:
    try:
        convert += morse_chars[i]
    except TypeError:
        convert += i

print(f"Converted Text: {convert}")
