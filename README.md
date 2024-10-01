# Knights Management 

## Description

This Python program allows users to create and manage a collection of knights, each with four attributes: Strength, Agility, Intelligence, and Stamina. Users can create new knights, update their attributes, display their information in a tabulated format, and perform various operations such as sorting, searching, and deleting knights.

## Features

- **Create Knights**: Generate knights with random attributes.
- **Update Attributes**: Modify a knight's attributes (strength, agility, intelligence, stamina).
- **Display Knights**: Show all knights in the list, or in a tabulated format.
- **Sort Knights**: Sort knights alphabetically by name.
- **Find Knight by Name**: Search for a knight by their name.
- **Delete Knights**: Remove a knight from the list after confirmation.
- **Save and Load Knights**: Save knights to a JSON file and load them when the program starts.

## Requirements

- Python 3.x
- `tabulate` library (for displaying knights in tabular form)
  - Install via `pip install tabulate`

## How to Run

1. Clone or download this repository.
2. Navigate to the folder containing `project.py`.
3. Run the script with:
   ```bash
   python project.py

## Usage
Once the program is running, you can:

Create new knights.
Update their attributes.
Display all knights.
Sort knights by name.
Search for a knight by name.
Delete a knight.
Exit the program (which will automatically save the knights to a JSON file).