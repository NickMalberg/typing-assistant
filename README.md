# Keylogger

## Overview
This is a simple keylogger built in Python using the `pynput` library. It logs the keys pressed on the keyboard and saves the data in CSV files. The project aims to provide basic keylogging functionality and later extend it to visualize the logged data.

## Features
- Records single keys and words typed.
- Saves logged data in CSV files.
- Allows customization and extension for future enhancements.

## Requirements
- Python 3.x
- `pynput` library

## Usage
1. Clone this repository to your local machine.
2. Install the required dependencies using pip:
   ```
   pip install pynput
   ```
3. Run the `main.py` script:
   ```
   python main.py
   ```
4. The keylogger will start running and log the keys pressed.
5. Press `ESC` key three times consecutively to stop the keylogger.

## Data
- The logged data is stored in CSV files located in the `data/` directory.
- `key_map.csv`: Contains the count of individual keys pressed.
- `key_map_words.csv`: Contains the count of words typed.

## Future Enhancements
- **Visualization:** Implement visualization features to analyze and present the logged data graphically.
- **Daily and Weekly Logging:** Enhance logging functionality to record keys and words on a daily and weekly basis.
- **Improved Data Storage:** Utilize databases for efficient storage and retrieval of logged data.

## Disclaimer
This keylogger is intended for educational and research purposes only. Please use it responsibly and ensure that you have the necessary permissions before running it on any system.
