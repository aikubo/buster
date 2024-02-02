import os
import csv

md_directory = "allmd"
csv_file = "moose_markdowndocs.csv"
num_files = 10  # Specify the number of files to iterate over

# Get a list of markdown files in the directory
md_files = [f for f in os.listdir(md_directory) if f.endswith(".md")]

# Open the CSV file for writing
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["title", "content"])  # Write the header row

    # Iterate over each markdown file up to the specified number of files
    for i, md_file in enumerate(md_files[:num_files]):
        with open(os.path.join(md_directory, md_file), "r") as f:
            content = f.read()
            content =(content.split("# "))  # Split content by heading level and join with newline
            for j in range(1, len(content)):
              
                writer.writerow([md_file, content[j]])
