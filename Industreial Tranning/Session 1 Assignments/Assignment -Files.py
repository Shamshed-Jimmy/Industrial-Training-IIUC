# Assignment 1: Write a script that reads a CSV file containing product information and converts it into a JSON file.

import csv
import json

def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r', newline='') as csvfile:
        products = list(csv.DictReader(csvfile))

    with open(json_file, 'w') as jsonfile:
        json.dump(products, jsonfile, indent=4)

    print(f"CSV file '{csv_file}' converted to JSON file '{json_file}'.")

csv_file = input("Enter the path to the CSV file: ")
json_file = input("Enter the path for the output JSON file: ")
csv_to_json(csv_file, json_file)


# Assignment 2: Create a log file writer that appends log messages to a file with timestamps.

import datetime

def write_log_message(log_file, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_message = f"[{timestamp}] {message}\n"

    with open(log_file, 'a') as file:
        file.write(formatted_message)

log_file = "app.log"
message = "This is a log message."

write_log_message(log_file, message)
print(f"Log message appended to '{log_file}' with timestamp.")
