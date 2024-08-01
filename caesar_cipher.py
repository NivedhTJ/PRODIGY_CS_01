def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
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
    shift = int(input("Enter the shift value: "))

    if choice.lower() == 'e':
        encrypted_text = caesar_encrypt(text, shift)
        print(f"Encrypted text: {encrypted_text}")
    else:
        decrypted_text = caesar_decrypt(text, shift)
        print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
