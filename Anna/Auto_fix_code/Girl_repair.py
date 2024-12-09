import os
import shutil

def replace_file_with_stock_code(file_path, stock_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.readlines()

        with open(stock_path, 'r') as stock_file:
            stock_content = stock_file.readlines()

        if file_content != stock_content:
            with open(file_path, 'w') as file:
                file.writelines(stock_content)
            print(f'Replaced {file_path} with stock code.')

    except FileNotFoundError:
        print(f'File not found: {file_path}')
    except Exception as e:
        print(f'An error occurred while processing {file_path}: {str(e)}')

def copy_missing_files(folder_path, stock_folder_path):
    for file_name in os.listdir(stock_folder_path):
        stock_path = os.path.join(stock_folder_path, file_name)
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(stock_path) and not os.path.isfile(file_path):
            shutil.copy(stock_path, folder_path)
            print(f'Successfully added the missing file {file_name} to {folder_path}')

def fixGirl():
        # Path to the folder containing files to check
    folder_path = "Girlfriend"

    # Path to the folder containing stock files
    stock_folder_path = "Backup\\GirlfriendBackup"

    copy_missing_files(folder_path, stock_folder_path)
    error_found = False  # Track if any errors were found

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        stock_path = os.path.join(stock_folder_path, file_name)

        if os.path.isfile(file_path) and os.path.isfile(stock_path):
            try:
                replace_file_with_stock_code(file_path, stock_path)
            except Exception as e:
                error_found = True
                print(f'Error processing {file_name}: {str(e)}')

    if not error_found:
        print('No errors found.')


