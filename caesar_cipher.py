# Choice for encryption and decrpytion

choice = input("What do you want to do?: " + "\n"
               "1. Encrypt" + "\n"
               "2. Decrypt" + "\n")

# Message to convert and key

data = input("Enter your message : ")
key = input("Enter the key: ")


def caesar_encrypt(data, key):
    # Result variable
    result = ""

    # Go through each character in message
    for char in data.upper():
        if char.isalpha():

            # Convert characters to ASCII code
            char_code = ord(char)

            # Shifting each character's ASCII according to provided key
            new_char_code = char_code + int(key)

            if new_char_code > ord('Z'):
                new_char_code -= 26

            # Converting new ASCII code back to characters
            new_char = chr(new_char_code)

            # Adding new characters into result string
            result += new_char

        else:
            # Adding the special characters as it is
            result += char

    print("Your encrypted message is: " + result.lower())


def caesar_decrypt(data, key):
    # Result variable
    result = ""

    # Go through each character in message
    for char in data.upper():
        if char.isalpha():

            # Convert characters to ASCII code
            char_code = ord(char)

            # Shifting each character's ASCII according to provided key
            new_char_code = char_code - int(key)

            if new_char_code < ord('A'):
                new_char_code += 26

            # Converting new ASCII code back to characters
            new_char = chr(new_char_code)

            # Adding new characters into result string
            result += new_char

        else:
            # Adding the special characters as it is
            result += char

    print("Your decrypted message is: " + result.lower())


if choice == "1":
    caesar_encrypt(data, key)

elif choice == "2":
    caesar_decrypt(data, key)

else:
    print("Invalid input")
