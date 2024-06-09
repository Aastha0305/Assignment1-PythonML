import csv
def read_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(', '.join(row))

# Example usage
file_path = input("Enter the path to your CSV file: ")
read_csv(file_path)
