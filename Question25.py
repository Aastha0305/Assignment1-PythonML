def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print("Contents copied successfully from '{}' to '{}'.".format(source_file, destination_file))
    except FileNotFoundError:
        print("Error: One or both files not found.")

# Example usage:
source_file = input("Enter the path of the source text file: ")
destination_file = input("Enter the path of the destination text file: ")

copy_file(source_file, destination_file)
