import pandas as pd
import json

def json_to_csv(input_file, output_file):
    # Open the JSON file and read it line by line
    with open(input_file, 'r', encoding='utf-8') as file:
        data_lines = file.readlines()

    # Initialize an empty list to store JSON objects
    json_objects = []

    # Parse each line as a JSON object and append it to the list
    for line in data_lines:
        try:
            json_object = json.loads(line)
            json_objects.append(json_object)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

    # Convert the list of JSON objects to a Pandas DataFrame
    df = pd.json_normalize(json_objects)

    # Save the DataFrame to a CSV file
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Specify the input and output file paths
    input_json_file = '/Users/mihir/Downloads/yelp_dataset/yelp_academic_dataset_business.json'
    output_csv_file = '/Users/mihir/Desktop/yelp_dataset.csv'

    # Convert JSON to CSV
    json_to_csv(input_json_file, output_csv_file)
