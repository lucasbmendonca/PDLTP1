def slurp(file):
    fh = open(file, mode="r")
    contents = fh.read()
    fh.close()
    return contents