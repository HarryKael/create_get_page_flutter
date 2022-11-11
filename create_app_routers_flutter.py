#!/usr/bin/env python3
import os
import sys


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
            return names
        else:
            # If the path does not exists.
            print('The path does not exists')
            sys.exit(1)
    else:
        # If the number of arguments are not enough
        print('Introduce all needed the argunemnts.')
        sys.exit(1)


def main():
    names = get_arguments()
    # When there is not pages.
    if len(names) == 0:
        print('No names')
        sys.exit(1)
    else:
        print(names)


if __name__ == '__main__':
    main()