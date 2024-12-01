# Steganography project

This project is part of the academic subject named **steganography**. The requirement was to create **7 algorithms** that allow hiding information in a given medium. In our case, these were html and css files.

A simple window application was created to handle the algorithms, which loads the message to be encrypted and the document in which it is to be placed, and also reverses this operation, recovering the password from the loaded file.

The application contains a *HELP* tab, which informs the user about the available algorithms and how to use them.

## Tests

There are tests that verify whether hiding an information in various files and retrieving it gives the same result. They can be run with `python test.py`.