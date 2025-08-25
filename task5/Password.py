import random
import string

def generate_password(length=12):
    """Generate a random password of a given length."""
    if length < 4:
        return "Password length should be at least 4 characters."
    # Define character pools
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password has at least one of each type
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest with random choices from all pools
    all_chars = letters + digits + symbols
    password += random.choices(all_chars, k=length - 3)

    # Shuffle the result to avoid predictable order
    random.shuffle(password)

    return ''.join(password)

def main():
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
