#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    '''Calculates the fewest number of
    operations needed to result in exactly n H
    characters in the file.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The fewest number of operations needed.
        If n is impossible to achieve, return 0.
    '''
    characters_in_file = 1  # Number of characters currently in the file
    clipboard_contents = 0  # Number of 'H's copied to the clipboard
    operations_counter = 0  # Operations counter

    while characters_in_file < n:
        # If clipboard is empty, copy all characters in the file
        if clipboard_contents == 0:
            clipboard_contents = characters_in_file
            operations_counter += 1  # Increment operations counter

        # If there's only one character in the file, simply paste the clipboard
        if characters_in_file == 1:
            characters_in_file += clipboard_contents
            operations_counter += 1  # Increment operations counter
            continue

        # Calculate remaining characters to paste
        remaining_chars = n - characters_in_file

        # Check if it's impossible to achieve n characters in the file
        if remaining_chars < clipboard_contents:
            return 0

        """ If remaining characters can't be evenly divide
        by the current number of characters in the file,
        paste the clipboard; otherwise, copy all characters and then paste """

        if remaining_chars % characters_in_file != 0:
            characters_in_file += clipboard_contents
            operations_counter += 1  # Increment operations counter
        else:
            clipboard_contents = characters_in_file
            characters_in_file += clipboard_contents
            operations_counter += 2  # Increment operations counter

    # If the desired number of characters 'n' is achieved,
    # return the operations counter; otherwise, return 0
    if characters_in_file == n:
        return operations_counter
    else:
        return 0
