# Dictionary for mapping letters, numbers, punctuation to "0" for raised dots and "." for unraised dots
braille_dict = {
    'a': '0.....', 'b': '00....', 'c': '0..0..', 'd': '0..00.', 'e': '0...0.', 'f': '00.0..', 'g': '00.00.', 'h': '00..0.',
    'i': '.0.0..', 'j': '.0.00.', 'k': '0.0...', 'l': '00.0...', 'm': '0.00..', 'n': '0.000.', 'o': '0...00', 'p': '00.00..',
    'q': '00.000', 'r': '00..00', 's': '.0.00.', 't': '.0..0.', 'u': '0.0..0', 'v': '00.0..', 'w': '.0.000', 'x': '0..000',
    'y': '0.00.0', 'z': '0...00', ' ': '......', ',': '.0....', '.': '.0..00', '?': '.0.00.', '!': '00..0.', '-': '....0.',
    '0': '.0.000', '1': '0.....', '2': '00....', '3': '0..0..', '4': '0..00.', '5': '0...0.', '6': '00.0..', '7': '00.00.',
    '8': '00..0.', '9': '.0.00.'
}

# Special prefixes for numbers and capitalization
CAPITAL_PREFIX = ".....0"  # Braille prefix for capitalization
NUMBER_PREFIX = "0.0000"   # Braille prefix for numbers

# Function to translate English text to Braille in "0" and "." format
def string_to_braille(text_string):
    translated = ""
    number_mode = False  # To track if we are in number mode

    for char in text_string:
        if char.isdigit():
            if not number_mode:
                translated += NUMBER_PREFIX + " "  # Add number prefix and space
                number_mode = True
            translated += braille_dict[char] + " "
        elif char.isalpha():
            if number_mode:
                number_mode = False  # Reset number mode after finishing number sequence
            if char.isupper():
                translated += CAPITAL_PREFIX + " "  # Add capital prefix
            translated += braille_dict[char.lower()] + " "
        elif char == ' ':
            translated += braille_dict[char] + " "
        else:
            translated += braille_dict.get(char, '......') + " "  # Default to empty Braille for unknown symbols
    return translated.strip()

# Braille to English translation dictionary
english_dict = {v: k for k, v in braille_dict.items()}

# Function to translate Braille in "0" and "." format to English
def braille_to_string(braille_string):
    translated = ""
    parts = braille_string.split()  # Split Braille input by spaces
    is_capital = False
    is_number = False

    for part in parts:
        if part == CAPITAL_PREFIX:
            is_capital = True
        elif part == NUMBER_PREFIX:
            is_number = True
        else:
            letter = english_dict.get(part, '?')
            if is_number:
                letter = letter if letter.isdigit() else '?'
            if is_capital:
                letter = letter.upper()
                is_capital = False
            translated += letter
    return translated

# Detect if input is Braille or English
def is_braille(text):
    for char in text:
        if char in "0.":
            return True
    return False

def main():
    user_input = input().strip()
    
    # Check if input is in Braille or English
    if is_braille(user_input):
        # Output English translation
        print(braille_to_string(user_input))
    else:
        # Output Braille translation
        print(string_to_braille(user_input))

if __name__ == "__main__":
    main()

