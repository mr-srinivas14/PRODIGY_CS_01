# Function to encrypt the message using Caesar Cipher
def encrypt(message, shift):
    encrypted_text = ""
    for char in message:
        if char.isalpha():  # Check if the character is an alphabet
            shift_base = 65 if char.isupper() else 97
            # Shift character and handle wrapping around the alphabet
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabet characters remain unchanged
    return encrypted_text

# Function to decrypt the message using Caesar Cipher
def decrypt(message, shift):
    return encrypt(message, -shift)  # Decryption is just reverse of encryption

# Main function
def main():
    print("Welcome to Mr. Srinivas's Caesar Cipher Algorithm Tool.")
    choice = input("If you want to encrypt, enter E. If you want to decrypt, enter D: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    print("You need to enter this same shift value while Decryption.")
    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
        print("Use this Encrypted message for Decryption.")
    elif choice == 'd':
        print("Decrypted message:", decrypt(message, shift))
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
    print("Thanks for using Mr. Srinivas's Tool.")

if __name__ == "__main__":
    main()
