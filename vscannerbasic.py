import os
import hashlib

# List of known malicious hashes (in real-life, this list would be maintained and updated regularly)
known_malicious_hashes = [
    "e99a18c428cb38d5f260853678922e03",  # Example MD5 hash of a malicious file
    "d41d8cd98f00b204e9800998ecf8427e",  # Example MD5 hash of another malicious file
    # Add more malicious hashes here...
]

def get_file_hash(file_path, hash_algo="sha256"):
    """Generates hash of the file using the specified hashing algorithm."""
    hash_func = hashlib.new(hash_algo)
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def scan_directory_for_viruses(directory_path):
    """Scans all files in the given directory and compares their hashes with known malicious ones."""
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Scanning {file_path}...")
            
            # Get the hash of the current file
            file_hash = get_file_hash(file_path)
            if file_hash and file_hash in known_malicious_hashes:
                print(f"WARNING: Malicious file detected! Hash: {file_hash} - File: {file_path}")
            else:
                print(f"File {file_path} is clean.")

if __name__ == "__main__":
    directory_to_scan = input("Enter the directory to scan: ")
    scan_directory_for_viruses(directory_to_scan)

