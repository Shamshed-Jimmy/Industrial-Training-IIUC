# Assignment 1: Write a Python script that determines if a number is positive, negative, or zero using if-elif-else.

# Prompt for the user to enter a number and convert it to a floating-point number

user_input = input('Enter a number: ')
num = float(user_input)

# Check if the number is positive, zero, or negative

if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")


# Assignment 2: Create a script that checks if a person is eligible for a senior citizen discount based on age and residency.

# Defining the age and residency eligibility criteria
senior_age = 60
residency = "Bangladesh"

# Prompt for  the user to enter age and country of residency
age = int(input("Enter your age: "))
country = input("Enter your country of residency: ")

# Checking if the person is eligible for the senior citizen discount
if age >= senior_age and country.lower() == residency.lower():
    print("Congratulations! You are eligible for a senior citizen discount.")
else:
    print("Sorry, you are not eligible for a senior citizen discount.")


# Assignment 3: Write a script that simulates a basic login system. Check username and password correctness.

# Initializing an empty dictionary to store user credentials (username: password)

user_credentials = {}

def register_user():
    """
    Register a new user by prompting for a username and password.
    """
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    user_credentials[username] = password
    print("User registered successfully!")

def login():
    """
    Log in with existing credentials.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_credentials and user_credentials[username] == password:
        print(f"Welcome, {username}!")
    else:
        print("Invalid username or password. Please try again.")

def main():
    # Main menu loop
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")




# Assignment 4: Implement a system that categorizes a day based on temperature and weather conditions.

def categorize_day(temperature, weather):
    
    # Categorizing a day based on temperature and weather conditions
    
    if temperature >= 30 and weather == "Sunny":
        return "Hot and Sunny"
    elif temperature >= 30 and weather == "Cloudy":
        return "Warm and Cloudy"
    elif temperature < 10 and weather == "Snowy":
        return "Cold and Snowy"
    else:
        return "Normal Day"

