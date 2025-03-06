
import os
import json

# File to store passwords
PASSWORD_FILE = "passwords.json"

# Function to load passwords from the file
def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as f:
            return json.load(f)
    return {}

# Function to save passwords to the file
def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as f:
        json.dump(passwords, f, indent=4)

# Function to display the main menu
def display_menu():
    print("\nPassword Manager")
    print("1. Add a new password")
    print("2. View all passwords")
    print("3. Search for a password")
    print("4. Delete a password")
    print("5. Exit")

# Function to add a new password
def add_password(passwords):
    service = input("Enter the service name (e.g., Gmail, Instagram): ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    passwords[service] = {"username": username, "password": password}
    save_passwords(passwords)
    print(f"Password for {service} added successfully!")

# Function to view all passwords
def view_passwords(passwords):
    if passwords:
        print("\nStored passwords:")
        for service, data in passwords.items():
            print(f"Service: {service}, Username: {data['username']}")
    else:
        print("No passwords stored yet!")

# Function to search for a password by service name
def search_password(passwords):
    service = input("Enter the service name to search for: ")
    if service in passwords:
        print(f"Service: {service}")
        print(f"Username: {passwords[service]['username']}")
        print(f"Password: {passwords[service]['password']}")
    else:
        print(f"No password found for {service}!")

# Function to delete a password by service name
def delete_password(passwords):
    service = input("Enter the service name to delete: ")
    if service in passwords:
        del passwords[service]
        save_passwords(passwords)
        print(f"Password for {service} deleted successfully!")
    else:
        print(f"No password found for {service}!")

# Main function to run the password manager
def main():
    passwords = load_passwords()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_password(passwords)
        elif choice == "2":
            view_passwords(passwords)
        elif choice == "3":
            search_password(passwords)
        elif choice == "4":
            delete_password(passwords)
        elif choice == "5":
            print("Exiting Password Manager. Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
