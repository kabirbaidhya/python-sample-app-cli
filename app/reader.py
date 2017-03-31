
def read(filename):
    '''
    Reads the contents of the given file and returns it.
    '''
    # Open file for reading
    f = open(filename, 'r')
    # Read the contents
    data = f.read()
    # Close the file
    f.close()

    return data
