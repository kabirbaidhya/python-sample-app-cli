
def write(filename, data):
    '''
    Writes the data (string) to the file.
    '''
    # Open file for Writing
    f = open(filename, 'w')
    # Write the data to the file
    f.write(data)
    # Close the file
    f.close()
