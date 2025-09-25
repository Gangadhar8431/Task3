
import random
import string

def generate_password(length):
    # Characters to use: letters, digits, punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== 🔐 Password Generator ===")

    try:
        # Step 1: Ask user for password length
        length = int(input("Enter desired password length: "))

        if length < 4:
            print("❌ Password length should be at least 4 characters.")
            return

        # Step 2: Generate password
        password = generate_password(length)

        # Step 3: Display the result
        print(f"\n✅ Generated Password: {password}")

    except ValueError:
        print("❌ Invalid input! Please enter a number.")

# Run the program
if __name__ == "__main__":
    main()
