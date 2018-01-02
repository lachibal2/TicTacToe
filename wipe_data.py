def clearFile(filename='data.txt'):
    fi = open(filename, 'w')
    fi.write('')
    fi.close()
    print("Cleared Data File")
clearFile()
