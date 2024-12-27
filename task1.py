
def shiftchar(char, shift, decrypt=False):
    """Shift a single character by the specified amount."""
    if not char.isalpha():
        return char
        
    asciioffset = ord('A') if char.isupper() else ord('a')
    shifted = ord(char) - asciioffset
    
    if decrypt:
        shifted = (shifted - shift) % 26
    else:
        shifted = (shifted + shift) %  26
        
    return chr(shifted + asciioffset)

def encrypt(text, shift):
    """Encrypt the text using Caesar cipher."""
    return ''.join(shiftchar(char, shift) for char in text)

def decrypt(text, shift):
    """Decrypt the text using Caesar cipher."""
    return ''.join(shiftchar(char, shift, decrypt=True) for char in text)


def main():
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '3':
            print("Goodbye!")
            break
            
        if choice not in ['1', '2']:
            print("Invalid choice. Please try again.")
            continue
            
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (1-15):"))
        
        if choice == '1':
            result = encrypt(message, shift)
            print(f"\nEncrypted message: {result}")
        else:
            result = decrypt(message, shift)
            print(f"\nDecrypted message: {result}")

if __name__ == "__main__":
    main()