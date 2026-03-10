# File Organizer

A simple Python automation tool that automatically organizes files in a folder based on their file extensions.

## What this program does

This script scans a folder and sorts files into different folders according to their extensions.

Example:

Images(jpg/png) → .jpg .png  
Documents(pdf/txt) → .pdf .txt  
Python Files(py) → .py

## Features

- Automatically scans a directory
- Creates folders based on file extensions
- Moves files into the correct folders
- Helps keep folders clean and organized

## Technologies Used

Python

Modules:
- os
- shutil

## How to Use

1. Run the script.
2. Enter the folder path.
3. The program will automatically organize files into separate folders based on their extensions.

## Example

Before running the script:

folder/
file1.jpg  
file2.pdf  
file3.py  

After running the script:

folder/
jpg/file1.jpg  
pdf/file2.pdf  
Py/file3.py
