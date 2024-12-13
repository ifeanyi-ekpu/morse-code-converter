from morse import morse_codes

def morse_converter():
    """
    A text-based Python program to convert Strings into Morse Code.
    """
    converter = True
    while converter:
        user_input = input("Enter letters/numbers to be converted, or type quit to end: ")
        converted_letters = []
        result = ""
        try:
            for char in user_input:
                if char.isalpha():
                    result += char.upper()
                else:
                    result += char
        except ValueError:
            print("Invalid input. Please, enter letters only")

        if result == "QUIT":
            converter = False
            return print("Thanks for playing, see you again!")

        for letter in result:
            for key, value in morse_codes.items():
                if letter == key:
                    converted_letters.append(value)
        sentence = " ".join(converted_letters)
        print(sentence)


morse_converter()

