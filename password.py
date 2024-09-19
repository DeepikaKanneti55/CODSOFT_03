import random
import string

def generate_password(length):
    """Generate a random password with the given length."""
    if length < 4:
        print("Password length should be at least 4 characters for complexity.")
        return None

    # Define character sets
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password has at least one character from each character set
    password = [
        random.choice(string.ascii_uppercase),  # At least one uppercase letter
        random.choice(string.ascii_lowercase),  # At least one lowercase letter
        random.choice(string.digits),           # At least one digit
        random.choice(string.punctuation)       # At least one special character
    ]

    # Fill the rest of the password length with random characters
    password += [random.choice(all_characters) for _ in range(length - 4)]
    
    # Shuffle the characters to ensure randomness
    random.shuffle(password)
    
    # Join the list into a string and return
    return ''.join(password)

def main():
    try:
        # Prompt the user to enter the desired password length
        length = int(input("Enter the desired length of the password (minimum 4): "))
        if length < 4:
            print("Error: Password length must be at least 4 characters.")
            return

        # Generate the password
        password = generate_password(length)

        # Display the generated password
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Error: Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
