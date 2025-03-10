###Lab 7 (March 7th, 2025) ###Copied my code from notebook file to this python file. 
import os
import hashlib

def menu():
    while True:
        print("\n File Duplicate Finder.")
        print("1. Enter directory to find.")
        print("2. Exit.")

        try:
            choice = int(input("Choose an option: ")) 
            if choice == 1:
                directory= input("Enter Directory Path: ")
                if os.path.isdir(directory):
                    find_duplicates(directory)
                else:
                    print("Invalid directory. Please enter a valid path.")
            elif choice == 2:
                break
            else:
                print("Invalid option. Please choose an option 1 or 2.")
        except ValueError:
            print("Please enter a valid number.")

def find_duplicates(directory): ###Recursive search for duplicates. 
    hashes = {}  ###Learned this from the internet to save the file in here while checking for duplicates. 
    duplicates = [] ### Same as above. 
    for root,_, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root,file)
            file_hash = get_checksum(file_path)

            if file_hash in hashes:
                duplicates.append((file_path, hashes[file_hash]))
            else:
                hashes[file_hash] = file_path
    
    if duplicates:
        print("\n Duplicate Files Found:")
        for duplicates, existing_file in duplicates:
            print(duplicates, "is a duplicate of", existing_file)
    else:
        print("\n No duplicate files found.") 


def get_checksum(file_path):
    hash_obj = hashlib.md5()  # Change to hashlib.sha256() if desired
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except FileNotFoundError:
        print("Error accessing file: ", file_path)

if __name__ == "__main__":
    menu()
