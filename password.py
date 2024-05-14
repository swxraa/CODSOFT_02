import random
import string

def generate_password(length):
    """
    Generate a random password of the specified length.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: The generated password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
