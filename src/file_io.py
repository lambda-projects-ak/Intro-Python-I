"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE


# def read_file():
#     text_file = open("foo.txt", "r")
#     history = text_file.read()
#     text_file.close()
#     return history

with open('foo.txt') as foo:
    read_data = foo.read()
    print(read_data)
    print(foo.closed)

print(foo.closed)
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
newString = "This is a string being added to bar.txt\n"
secondString = "This is another string being added to bar.txt\n"


def write_file(content):
    bar = open('bar.txt', 'a+')
    bar.write(str(content))
    bar.close()


write_file(newString)
write_file(secondString)
