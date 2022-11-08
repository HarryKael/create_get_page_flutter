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
        # Print the name of the page and the name that will have the directory of the page.
        print("Nombre: {name}, Path: {name}_page".format(name=name))
        # If the directory does not exist create one.
        if not os.path.exists("{}_page".format(name)):
            subprocess.run(['mkdir', "{}_page".format(name)])
        # Return the name of the page and the name of the directory
        return name, "{}_page".format(name)
    except IndexError as e:
        # When a error happend finish the command, with the error message on the screen."
        print("Error: {}".format(e))
        sys.exit(1)

