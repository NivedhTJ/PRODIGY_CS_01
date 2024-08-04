def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha(): # checks if char is in upper case
            shift_base = 65 if char.isupper() else 97 # if char is in upper case ASCII value of 'A' is 65 else 'a'is 97 
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            #using %26 so that characters stay in the A-Z or a-z range
            #ord(char):function converts a character (char) to its corresponding ASCII value 
            #chr(...):Convert the resulting ASCII value back to a character.
            
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")
    if choice.lower() not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
        return

    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))# for caeser code shift value is 3 

    #calling functions for either encrypting or decrypting based on user input
    if choice.lower() == 'e':
        encrypted_text = caesar_encrypt(text, shift)
        print(f"Encrypted text: {encrypted_text}") #prints the formatted encrypted text
    else:
        decrypted_text = caesar_decrypt(text, shift)
        print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
