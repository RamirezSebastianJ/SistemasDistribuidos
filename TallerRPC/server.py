from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

def python_logo():
    print("entra")
    with open("file.txt", "rb") as handle:
        return xmlrpc.client.Binary(handle.read())

def searchInFile():
    f = open("file.txt", "r")
    while(True):
        linea = f.readline()
        linea = str(linea)
        numbers = [int(temp)for temp in linea.split() if temp.isdigit()]
        arrayReverse(numbers)
        if not linea:
            break
    f.close()

def arrayReverse(array):
    auxiliarArray = []
    lenArray =  len(array)-1
    while lenArray >= 0:
        auxiliarArray.append(array[lenArray])
        lenArray -= 1
    print(auxiliarArray)


server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(python_logo, 'python_logo')
server.register_function(searchInFile, 'searchInFile')
server.serve_forever()