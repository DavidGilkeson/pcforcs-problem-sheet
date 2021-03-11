# Author: David Gilkeson

# Write a program that reads in a text file and outputs the number of e's it contains.

# The program should take the filename from an argument on the command line.

with open('moby-dick.txt', 'r', encoding='utf-8') as file:      # opens the txt file and 'r' reads the file. Encoding stops the error I was having with is referenced at the bottom
    print(file.read().count('e'))


# References

# GeeksforGeeks. 2021. with statement in Python - GeeksforGeeks. [ONLINE] Available at: https://www.geeksforgeeks.org/with-statement-in-python/. [Accessed 22 February 2021].

# Python File Open. 2021. Python File Open. [ONLINE] Available at: https://www.w3schools.com/python/python_file_open.asp. [Accessed 22 February 2021].

# Real Python. 2021. Working With Files in Python – Real Python. [ONLINE] Available at: https://realpython.com/working-with-files-in-python/. [Accessed 22 February 2021].

# Stack Overflow. 2021. python - How to fix ''UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 29815: character maps to ''? - Stack Overflow. [ONLINE] Available at: https://stackoverflow.com/questions/49562499/how-to-fix-unicodedecodeerror-charmap-codec-cant-decode-byte-0x9d-in-posit. [Accessed 22 February 2021].
