import os
import re

def list_and_rank_files(directory, output_file):
    try:
        # Get the list of all files and directories in the specified directory
        files = os.listdir(directory)
        
        # Filter the list to only include files
        files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
        
        # Regular expression to match date format in filenames
        date_pattern = re.compile(r'(\d{1,2})_(\d{1,2})_(\d{4})')

        # Dictionary to hold files by year
        files_by_year = {}
        total_files = 0

        for file in files:
            match = date_pattern.search(file)
            if match:
                day, month, year = match.groups()
                if year not in files_by_year:
                    files_by_year[year] = []
                files_by_year[year].append((file, (int(day), int(month))))
                total_files += 1
            else:
                print(f"File '{file}' does not match the expected date pattern and will be ignored.")
        
        # Open the output file for writing
        with open(output_file, 'w') as f:
            # Sort and write files by year
            for year in sorted(files_by_year.keys()):
                f.write(f"Files from {year}:\n")
                sorted_files = sorted(files_by_year[year], key=lambda x: (x[1][1], x[1][0]))  # Sort by month, then day
                for index, (file, date) in enumerate(sorted_files, start=1):
                    f.write(f"{index}. {file}\n")
                f.write('\n')
        
        print(f"Sorted file names with ranking have been written to '{output_file}'.")
        print(f"Total files processed: {total_files}")
        print(f"Total files in directory: {len(files)}")
        
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"You do not have permission to access the directory '{directory}'.")




def list_files_in_directory(directory):
    try:
        # Get the list of all files and directories in the specified directory
        files = os.listdir(directory)
        
        # Filter the list to only include files
        files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
        
        # Print the list of files
        print("Files in '{}':".format(directory))
        i = 1
        for file in files:
            print(f"{file}")
            # i+=1
    except FileNotFoundError:
        print("The directory '{}' does not exist.".format(directory))
    except PermissionError:
        print("You do not have permission to access the directory '{}'.".format(directory))


your_directory_path = r'C:\Users\HP\Desktop\NewBatteryData'
output_file_path = r'C:\Users\HP\Desktop\Sorted_K2_039.txt'
list_and_rank_files(your_directory_path, output_file_path)