import random

def generate_password(length):
    # Define character sets for each type of character
    symbols = ["~","!","@","$","%","^","&","*","(",")","{","}","[","]"]  # symbols
    small_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    # Ensure the password starts with a capital letter
    password = random.choice(capital_letters)
    
    # Fill the rest of the password with a mix of characters 
    for _ in range(length - 1):
        # Randomly choose from all character sets
        char_set = random.choice([symbols, small_letters, numbers, capital_letters])
        password += random.choice(char_set)
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        # Prompt user for the desired length of the password
        length = int(input("Enter the length of the password: "))
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print("Generated Password:", password)
    
    except ValueError:
        print("Error: Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
    