#!/usr/bin/env python3 
import sys
import os
import re
import subprocess


def get_paths():
    """Get the data to make the path for the elements of the page."""
    try:
        # Get the name introduce by the terminal.
        name = sys.argv[1]
        path = name
        # If the there is a argument for the path of the directory then we will use it.
        if sys.argv[2]:
            path = '{}/{}_page'.format(sys.argv[2], name)
        # Print the name of the page and the name that will have the directory of the page.
        print("Nombre: {name}, Path: {path}".format(name=name, path=path))
        # If the directory does not exist create one.
        if not os.path.exists(path):
            subprocess.run(['mkdir', path])
        # Return the name of the page and the name of the directory        
        return name, path
    except IndexError as e:
        # When a error happend finish the program, with the error message on the screen."
        print("Error: {}".format(e))
        sys.exit(1)


def renaming(name:str, version:int = 1):
    """This function is to rewrite the name with the form that it has to be, example: 'list_detail' => 'ListDetail'"""
    if version == 1:
        names:list[str] = name.split("_")
        result = ''
        for element in names:
            result = '{}{}'.format(result, element.capitalize())
    elif version == 2:
        names:list[str] = name.split("_")
        result = ''
        for element in names:
            if element == names[0]:
                result = '{}{}'.format(result, element)
            else:
                result = '{}{}'.format(result, element.capitalize())
    return result


def create(name: str, path: str, path_placeholder: str, tipo: str):
    """Function to create the file of the page path passed at the arguments."""
    # Pattern to change the names of the classes.
    pattern = r"Placeholder"
    # Pattern to change the names of the imports.
    pattern2 = r"placeholder_"
    # Pattern to change the names of the builders
    pattern3 = r"builder\: \(Placeholder"
    # The path to create the file.
    full_path = "{path}/{name}_{type}.dart".format(path=path, name=name, type=tipo)
    # Check if the file already exists, if the file exists the function does not make any changes
    # to the file.
    if not os.path.exists(full_path):
        # Lines updated of the file.
        rows = []
        # Open the file that make the placeholder.
        with open(path_placeholder, 'r') as placeholder:
            # Read line by line of the file and make the changes.
            for line in placeholder:
                # If the pattern2 exists make the change of the name (imports).
                if re.search(pattern2, line):
                    rows.append(re.sub(pattern2, '{}_'.format(name.lower()), line))
                # If the patter3 of the builders is in the line then the program will change that for the text.
                elif re.search(pattern3, line):
                    rows.append(re.sub(pattern3, 'builder: ({}'.format(renaming(name, 2)), line))
                else:
                    # Changes and rename the names (Classes).
                    rows.append(re.sub(pattern, renaming(name), line))
            # Close the file.
            placeholder.close()
        # Open the file in the path.
        with open(full_path, 'w') as file:
            # Write the lines in the file.
            file.writelines(rows)
            # Close the file.
            file.close()


def main():
    """Automation of the creation of one page in flutter using the State Managment with 'GET'"""
    # The paths of the placeholders.
    placeholder_controller = "/Users/macbook/Documents/Harry/commands/placeholders/lib/src/placeholder_controller.dart"
    placeholder_binding = "/Users/macbook/Documents/Harry/commands/placeholders/lib/src/placeholder_binding.dart"
    placeholder_page = '/Users/macbook/Documents/Harry/commands/placeholders/lib/src/placeholder_page.dart'
    # Get the name and the path of the directory.
    name, path = get_paths()
    # Create the controller for the page.
    create(name=name, path=path, tipo='controller', path_placeholder=placeholder_controller)
    # Create the binding for the page.
    create(name=name, path=path, tipo='binding', path_placeholder=placeholder_binding)
    # Create the visual part of the page.
    create(name=name, path=path, tipo='page', path_placeholder=placeholder_page)
    # Exit the program.
    sys.exit(0)

# Init the progra.
if __name__ == '__main__':
    main()