import os
import sys
import hashlib
from os import listdir
from os.path import isfile


BUF_SIZE = 1024 * 1000 # 1 MB

def get_all_files(path):
    files = []
    for file in listdir(path):
        if isfile(file):
            files.append(file)
    return files

def get_hashes(files):
    hashes = {}
    for file_path in files:
        sha256 = hashlib.sha256()
        with open(file_path,'rb') as file:
            while True:
                data = file.read(BUF_SIZE)
                if not data:
                    break
                sha256.update(data)
            hashes[file_path] = sha256.hexdigest()
    return hashes

def get_duplicated_files(hashes):
    unique_hashes = []
    duplicated_files = []
    for file_name,file_hash in hashes.items():
        if file_hash in unique_hashes:
            duplicated_files.append(file_name)
        else:
            unique_hashes.append(file_hash)
    return duplicated_files

def remove_files(files_paths):
    for file_path in files_paths:
        os.remove(file_path)

def main():
    files = get_all_files("./")
    hashes = get_hashes(files)
    duplicated_files = get_duplicated_files(hashes)
    remove_files(duplicated_files)
 

if __name__ == '__main__':
    sys.exit(main())