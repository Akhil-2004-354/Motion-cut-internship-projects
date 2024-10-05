# random password generator
import random
import string
import pyperclip

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Secure Password Generator")
    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no)): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no)): ").lower() == 'yes'

    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    print("Generated Password:", password)

    copy_to_clipboard = input("Copy to clipboard? (yes/no)): ").lower() == 'yes'
    if copy_to_clipboard:
        pyperclip.copy(password)
        print("Password copied to clipboard.")

if __name__ == '__main__':
    main()

