# Caesar Cipher Encryption and Decryption

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

print("=== Caesar Cipher Encryption & Decryption ===")
message = input("Enter the message: ")
shift = int(input("Enter the shift key: "))

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print("\nOriginal Message :", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
