# Assignment 1: Write a script that processes a list of temperature readings. If any temperature is above a certain threshold, print a warning.

# List of temperature readings
temperatures = [22, 35, 28, 31, 40]

# Threshold temperature (you can change this)
threshold = 30

# Check each temperature
for temp in temperatures:
    if temp > threshold:
        print("Warning: Temperature is too high!")
        


# Assignment 2: Given a list of users with their subscription status, write a loop that sends an email to all subscribed users.

friends = [
    {"email": "user1@example.com", "subscribed": True},
    {"email": "user2@example.com", "subscribed": False},
    {"email": "user3@example.com", "subscribed": True}
]

for friend in friends:
    if friend["subscribed"] == True:
        print(f"Hi {friend['email']}! We're sending you an email!")
        print("We need grown-up help to send the email, but we'll try our best!")
    else:
        print(f"Hi {friend['email']}! We noticed you aren't signed up for our emails. That's totally fine!")



# Assignment 1: Create a script that processes a dictionary of products, checking stock levels and generating restock alerts if necessary.

products = {
    "laptop": {"stock": 4, "min_required": 10},
    "smartphone": {"stock": 15, "min_required": 5}
}

for product, details in products.items():
    if details["stock"] < details["min_required"]:
        print(f"Alert: {product.capitalize()} stock is low. Please restock.")
    else:
        print(f"{product.capitalize()} stock is sufficient.")

