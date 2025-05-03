# Assignment 1: Create a string that contains a simple bio data like name, age, and country. Extract each piece of information and print them separately.

# Defining Biodata string

bio_data = "Name: Shamshed Jimmy, Age: 26, Country: Bangladesh"

# Extracting  information using split and strip methods using the shown example in the script

name = bio_data.split(",")[0].split(":")[1].strip()
age = int(bio_data.split(",")[1].split(":")[1].strip())
country = bio_data.split(",")[2].split(":")[1].strip()

# Displaying  the extracted information

print("Name:", name)
print("Age:", age)
print("Country:", country)



# Assignment 2: Create a formatted string that includes data from a list or dictionary. For example, use a dictionary to store a person's information and format a string to include it.


# Defining person's information in a dictionary

person_information = {
    "name": "Ruhit",
    "age": 26,
    "country": "Bangladesh",
    "Number": "013232232236"
}

# Creating a formatted string using dictionary values

formatted_string = f"Hi, my name is {person_information['name']}. I am {person_information['age']} years old. I live in {person_information['country']}. My contact number is {person_information['Number']}."

# Print the formatted string

print(formatted_string)


# Assignment 3: Write a function that takes a string and returns a dictionary with the counts of each character in the string.

def count_characters(input_string):
    # Initializing an empty dictionary to store character counts
    char_counts = {}

    # Looping through each character in the input string
    for char in input_string:
        # Checking if the character is already in the dictionary
        if char in char_counts:
            # If yes, increment its count by 1
            char_counts[char] += 1
        else:
            # If no, add the character to the dictionary with count 1
            char_counts[char] = 1

    return char_counts

# Example usage:
input_string = "Hello, World!"
result = count_characters(input_string)

# Displaying the character counts
print("Character counts:")
for char, count in result.items():
    print(f"'{char}' appears {count} times")



# Assignment: Write a regex to find all the hashtags in a string.

import re

def extract_hashtags(text):
    # Define the regular expression pattern to find hashtags
    regex_pattern = r"#\w+"

    # Use regex to find all hashtags in the text
    hashtag_list = re.findall(regex_pattern, text)

    return hashtag_list

# Example usage:
tweet_text = "I love #Python and #AI! #codinglife"
hashtags = extract_hashtags(tweet_text)

# Display the hashtags found in the text
print("Hashtags found:", hashtags)
# Prompt the user to enter a number and convert it to a floating-point number
user_input = input('Enter a number: ')
num = float(user_input)

# Check if the number is positive, zero, or negative
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

