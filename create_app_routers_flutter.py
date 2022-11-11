#!/usr/bin/env python3
import os
import sys
from create_get_page_flutter import renaming


def get_arguments():
    """This function collect the names of the files in the path that have the '_page' at the end."""
    # To know if the number of arguments for the program are the needed.
    if len(sys.argv) == 3:
        # Get the path from the arguments
        path = sys.argv[1]
        # To know if the path exists.
        if os.path.exists(path):
            # The names to return when the function finish.
            names:list[str] = []
            # Walk throught the directory to get the name of all pages.
            walk = os.walk(path, topdown=True)
            # Verify if the pages pass the conditions to put them into the names.
            for minipath in walk:
                # Split the path and see if the path have only 1 directory than the path of the pages.
                splitted = str(minipath[0]).split('/')
                if (len(path.split('/')) + 1) == len(splitted):
                    # folder get the name of the page.
                    folder = splitted[len(splitted) - 1]
                    # Split the name into list.
                    folder_names = folder.split('_')
                    # If the las word of the name directory is 'page' then we add the name folder without
                    # the '_page' string to the names list.
                    if folder_names[len(folder_names) - 1] == 'page':
                        names.append(folder[:-5])
            return names, sys.argv[2]
        else:
            # If the path does not exists.
            print('The path does not exists')
            sys.exit(1)
    else:
        # If the number of arguments are not enough
        print('Introduce all needed the argunemnts.')
        sys.exit(1)


def create_app_routers(names:list[str], path):
    """Create the file 'app_routers.dart' with the names of the pages."""
    app_routers = 'app_routers.dart'
    # Full path of the file app_routers.dart.
    full_path = '{}/{}'.format(path, app_routers)
    # Verify if the directory where the file will be exists.
    if os.path.exists(path):
        # first line of the file.
        first_line = 'abstract class AppRouters {\n'
        # The lines that the file will have.
        lines:list[str] = [first_line]
        # Pass throught the name of the pages.
        for name in names:
            # Add a new line to the lines variable.
            lines.append('  static String get {name} => \'/{name}\';\n'.format(name=renaming(name, version=2)))
        # Add the last line that the file will have.
        lines.append('}')
        # Create the app_routers.dart file.
        with open(full_path, 'w') as file:
            # Add all the lines to the file.
            file.writelines(lines)
            # Close the file.
            file.close()
        # This is when the program finish.
        print('Finish')
        sys.exit(0)
    else:
        # Print the error.
        print('Error: This path does not exists (path ubication)')
        sys.exit(1)


def main():
    names, path = get_arguments()
    # When there is not pages.
    if len(names) == 0:
        print('No names')
        sys.exit(1)
    else:
        # If the path is equal to nothing.
        if path == '':
            # Create the file in the current directory.
            create_app_routers(names, os.getcwd())
        else:
            # Create the file in the path.
            create_app_routers(names, path)


if __name__ == '__main__':
    main()