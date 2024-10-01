import random
import json
import os
from tabulate import tabulate


class Knight:
    """Represents a knight with attributes such as strength, agility, intelligence, and stamina."""

    def __init__(self, name, strength, agility, intelligence, stamina):
        """
    Initializes a Knight object with the given attributes.

    Args:
        name (str): The knight's name.
        strength (int): The knight's strength attribute.
        agility (int): The knight's agility attribute.
        intelligence (int): The knight's intelligence attribute.
        stamina (int): The knight's stamina attribute.
    """
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.stamina = stamina

    def display_info(self):
        """Displays the knight's attributes."""
        print(f"Knight: {self.name}")
        print(f"Strength: {self.strength}")
        print(f"Agility: {self.agility}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Stamina: {self.stamina}")
        print("-" * 20)

    def update_attribute(self, attribute, value):
        """
    Updates a specific attribute of the knight.

    Args:
        attribute (str): The attribute to update ('strength', 'agility', 'intelligence', 'stamina').
        value (int): The new value for the attribute.
    """
        if attribute == 'strength':
            self.strength = value
        elif attribute == 'agility':
            self.agility = value
        elif attribute == 'intelligence':
            self.intelligence = value
        elif attribute == 'stamina':
            self.stamina = value
        else:
            raise ValueError(f"Invalid attribute: {attribute}")

    def to_dict(self):
        """
    Converts the knight's attributes into a dictionary format.

    Returns:
        dict: A dictionary containing the knight's attributes.
    """
        return {
            'name': self.name,
            'strength': self.strength,
            'agility': self.agility,
            'intelligence': self.intelligence,
            'stamina': self.stamina
        }

    @classmethod
    def from_dict(cls, data):
        """
    Creates a Knight object from a dictionary of attributes.

    Args:
        data (dict): A dictionary containing knight attributes.

    Returns:
        Knight: A new Knight object.
    """
        return cls(
            name=data['name'],
            strength=data['strength'],
            agility=data['agility'],
            intelligence=data['intelligence'],
            stamina=data['stamina']
        )

# Feature : Writing to a JSON file


def save_knights(knights, filename='knights.json'):
    """
    Saves a list of knights to a JSON file.

    Args:
        knights (list): List of Knight objects.
        filename (str): The name of the file to save to (default: 'knights.json').
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump([knight.to_dict() for knight in knights], file)

# Feature : Reading from a JSON file


def load_knights(filename='knights.json'):
    """
Loads a list of knights from a JSON file.

Args:
    filename (str): The name of the file to load from (default: 'knights.json').

Returns:
    list: A list of Knight objects.
"""
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [Knight.from_dict(item) for item in data]
    return []

# Feature : Create Knights


def create_knight(knights):
    """Create a new knight with random attributes."""
    name = input("Enter the name of your knight: ")
    strength = random.randint(50, 100)
    agility = random.randint(50, 100)
    intelligence = random.randint(50, 100)
    stamina = random.randint(50, 100)
    knight = Knight(name, strength, agility, intelligence, stamina)
    knights.append(knight)
    print(f"{name} has been created!")
    return knight

# Feature : View Knights' data


def select_knights(knights):
    """Display all knights and allow the user to select one."""
    if not knights:
        print("No knights available!")
        return None

    print("Available knights:")
    for i, knight in enumerate(knights):
        print(f"{i + 1}: {knight.name}")

    try:
        choice = int(input("Select a knight by number: ")) - 1
        if 0 <= choice < len(knights):
            return knights[choice]
        else:
            print("Invalid selection!")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

# Feature : Modify Knights' data


def change_data(knights):
    """Allow the user to change attributes of a selected knight."""
    knight = select_knights(knights)
    if knight is None:
        return

    knight.display_info()

    try:
        attribute = input(
            "Which attribute do you want to change? \
                (strength/agility/intelligence/stamina): ").lower()
        if attribute in ['strength', 'agility', 'intelligence', 'stamina']:
            value = int(input(f"Enter new value for {attribute}: "))
            if 0 <= value <= 200:
                knight.update_attribute(attribute, value)
                print(f"{attribute.capitalize()} updated successfully!")
            else:
                print("Value must be between 0 and 200.")
        else:
            print(
                "Only these are valid attributes: 'strength', 'agility', 'intelligence', 'stamina'")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except Exception as e:
        print(f"Error: {e}")

# Feature : Tabulate Knights and data


def display_tabulated_knights(knights):
    """Display all knights in a tabulated format."""
    if not knights:
        print("No knights to display!")
        return

    table = []
    headers = ['Name', 'Strength', 'Agility', 'Intelligence', 'Stamina']

    for knight in knights:
        table.append([
            knight.name,
            knight.strength,
            knight.agility,
            knight.intelligence,
            knight.stamina
        ])

    print(tabulate(table, headers=headers, tablefmt='grid'))

# Feature : Sort knights by name


def sort_knights(knights):
    """Sort knights by their names alphabetically."""
    knights.sort(key=lambda knight: knight.name)
    print("Knights sorted by name.")

# Feature : Find knight by name


def find_knight(knights):
    """Find a knight by name."""
    name = input("Enter the name of the knight to find: ")
    found_knight = next(
        (knight for knight in knights if knight.name.lower() == name.lower()), None)

    if found_knight:
        found_knight.display_info()
    else:
        print(f"No knight found with the name: {name}")

# Feature : Delete a knight


def delete_knight(knights):
    """Delete a knight after confirmation."""
    knight = select_knights(knights)
    if knight is None:
        return

    confirm = input(
        f"Are you sure you want to delete {knight.name}? (yes/no): ").lower()
    if confirm == 'yes':
        knights.remove(knight)
        print(f"Knight {knight.name} has been deleted.")
    else:
        print("Deletion cancelled.")


def menu(knights_number):
    knights = load_knights()
    while True:
        print("\n--- Knight Management Menu ---")
        print("1. Create a new knight")
        print("2. Change knight data")
        print("3. Show all knights")
        print("4. Show knights in tabulated format")
        print("5. Sort knights by name")
        print("6. Find knight by name")
        print("7. Delete a knight")
        print("8. Exit")
        choice = input("Choose an option (1-8): ")

        if choice == '1':
            create_knight(knights)
            knights_number += 1
        elif choice == '2':
            change_data(knights)
        elif choice == '3':
            if knights:
                for knight in knights:
                    knight.display_info()
            else:
                print("No knights to display!")
        elif choice == '4':
            display_tabulated_knights(knights)
        elif choice == '5':
            sort_knights(knights)
        elif choice == '6':
            find_knight(knights)
        elif choice == '7':
            delete_knight(knights)
        elif choice == '8':
            print("Exiting the program.")
            save_knights(knights)
            break
        else:
            print("Invalid option. Please try again.")


# Add a main entry point
if __name__ == "__main__":
    # Setting the scene
    knights_number = 0
    menu(knights_number)
