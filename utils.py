def slurp(file):
    fh = open(file, mode="r")
    contents = fh.read()
    fh.close()
    #teste
    return contents