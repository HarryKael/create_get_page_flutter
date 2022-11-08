#!/usr/bin/env python3 
import sys
import os
import re
import subprocess


def get_paths():
    try:
        name = sys.argv[1]
        print("Nombre: {name}, Path: {name}_page".format(name=name))
        if not os.path.exists("{}_page".format(name)):
            subprocess.run(['mkdir', "{}_page".format(name)])
        return name, "{}_page".format(name)
    except IndexError as e:
        print("Error: {}".format(e))
        sys.exit(1)


def create(name: str, path: str, path_placeholder: str, tipo: str):
    pattern = r"Placeholder"
    pattern2 = r"placeholder_"
    full_path = "{path}/{name}_{type}.dart".format(path=path, name=name, type=tipo)
    if not os.path.exists(full_path):
        rows = []
        with open(path_placeholder, 'r') as placeholder:
            for line in placeholder:
                if re.search(pattern2, line):
                    rows.append(re.sub(pattern2, '{}_'.format(name.lower()), line))
                else:
                    rows.append(re.sub(pattern, name.capitalize(), line))
            placeholder.close()
        with open(full_path, 'w') as file:
            file.writelines(rows)
            file.close()


def main():
    """Automation of the creation of one page in flutter using the State Managment with 'GET'"""
    placeholder_controller = "/Users/macbook/Documents/Harry/commands/placeholders/lib/src/placeholder_controller.dart"
    placeholder_binding = "/Users/macbook/Documents/Harry/commands/placeholders/lib/src/placeholder_binding.dart"
    placeholder_page = '/Users/macbook/Documents/Harry/commands/placeholders/lib/src/placeholder_page.dart'
    name, path = get_paths()
    create(name=name, path=path, tipo='controller', path_placeholder=placeholder_controller)
    create(name=name, path=path, tipo='binding', path_placeholder=placeholder_binding)
    create(name=name, path=path, tipo='page', path_placeholder=placeholder_page)
    sys.exit(0)


main()
