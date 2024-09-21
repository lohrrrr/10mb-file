# 10mb-file
 

# 10mb-file App
=====================

## Overview
Like https://8mb.video/ but local and without limits.
10mb-file App is a graphical user interface (GUI) application that allows users to compress video and image files to a specified target size. The app is built using the Kivy framework and provides an intuitive interface for selecting files, setting output sizes, and compressing files.

## Features
### Supported File Types
* Video files (MP4)
* Image files (JPG, JPEG, PNG, GIF)

### Functionality
* Select a file to compress
* Specify a target output size in MB
* Browse for files and save locations using a file dialog
* Track compression progress using a progress bar
* Display a success message when compression is complete

## Usage
### Step-by-Step Guide
1. Launch the File Compressor App
2. Select a file to compress by clicking the "Browse" button next to the "Select file" input field
3. Enter a target output size in MB in the "Output Size (MB)" input field
4. Select a save location by clicking the "Browse" button next to the "Select save location" input field
5. Click the "Compress" button to start the compression process
6. Wait for the compression process to complete, tracking progress using the progress bar
7. A success message will be displayed when compression is complete

## Requirements
### Software Requirements
* Python 3.x
* Kivy framework
* tkinter library (for file dialog)
* Pillow library (for image processing)
* FFMPEG, FFPROBE, FFPLAY

## Known Issues
* Currently, the app does not support compression of other file types beyond video and image files
* The app does not provide error handling for cases where the target output size is not achievable

## License
This software is licensed under the MIT License. See LICENSE.txt for details.

## Contributing
Contributions to the File Compressor App are welcome! If you'd like to report an issue or submit a pull request, please use the GitHub issues and pull requests features.