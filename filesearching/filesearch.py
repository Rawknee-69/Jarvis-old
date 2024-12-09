import os
import subprocess
import multiprocessing

EXCLUDED_DIRECTORIES = ["Windows", "Python310"]

def search_for_file(directory, filename, results):
    found_files = []

    for root, _, files in os.walk(directory):
        # Exclude specific directories
        if any(excluded_dir in root for excluded_dir in EXCLUDED_DIRECTORIES):
            continue
        
        if filename in files:
            file_path = os.path.join(root, filename)
            found_files.append(file_path)

    results.extend(found_files)

def open_file_with_default_app(file_path):
    try:
        subprocess.run(['start', '', file_path], shell=True)
        print(f"Opening '{file_path}' with its default application...")
    except Exception as e:
        print(f"Error opening '{file_path}': {e}")

def main():
    search_path = "C:\\Users\\srija\\Downloads\\scan\\"  # Set the initial search path here
    filename_to_search = input("Enter the filename to search for: ")

    num_processes = multiprocessing.cpu_count()
    manager = multiprocessing.Manager()
    results = manager.list()

    processes = []
    for _ in range(num_processes):
        process = multiprocessing.Process(target=search_for_file, args=(search_path, filename_to_search, results))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    found_files = list(results)

    if found_files:
        for file_path in found_files:
            print(f"File found: {file_path}")
            open_file_with_default_app(file_path)
    else:
        print(f"Sir, the file '{filename_to_search}' was not found.")

if __name__ == "__main__":
    main()
