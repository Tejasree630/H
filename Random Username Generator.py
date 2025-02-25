



import random
import string
import os

# Predefined lists of adjectives and nouns
adjectives = ['Cool', 'Happy', 'Fast', 'Fierce', 'Swift', 'Brave', 'Silly', 'Wild']
nouns = ['Tiger', 'Dragon', 'Lion', 'Phoenix', 'Eagle', 'Shark', 'Wizard', 'Viking']

def generate_username(include_numbers=False, include_special_chars=False, length=8):
    # Combine a random adjective and noun
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    
    username = f"{adjective}{noun}"

    # Add numbers if specified
    if include_numbers:
        username += str(random.randint(0, 99))  # Append a random number between 0 and 99

    # Add special characters if specified
    if include_special_chars:
        special_chars = string.punctuation  # Get a string of special characters
        username += random.choice(special_chars)  # Append a random special character

    # Ensure the username does not exceed the specified length
    if len(username) > length:
        username = username[:length]

    return username

def save_username_to_file(username):
    # Check if the file exists and read existing usernames
    if os.path.exists("usernames.txt"):
        with open("usernames.txt", "r") as file:
            existing_usernames = file.read().splitlines()
    else:
        existing_usernames = []

    # Check for duplicates
    if username in existing_usernames:
        print(f"Username '{username}' already exists. Not saving.")
    else:
        with open("usernames.txt", "a") as file:
            file.write(username + "\n")
        print("Username saved to usernames.txt")

def main():
    print("Welcome to the Random Username Generator!")
    
    # User input for customization options
    include_numbers = input("Include numbers in username? (yes/no): ").strip().lower() == "yes"
    include_special_chars = input("Include special characters in username? (yes/no): ").strip().lower() == "yes"
    
    # Input validation for length
    while True:
        try:
            length = int(input("Enter the maximum length of the username (positive integer): "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    # Generate a username
    username = generate_username(include_numbers, include_special_chars, length)
    print(f"Generated Username: {username}")
    
    save_option = input("Would you like to save this username to a file? (yes/no): ").strip().lower()
    if save_option == "yes":
        save_username_to_file(username)

if __name__ == "__main__":
    main()

