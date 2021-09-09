import xmlrpc.client

AMOUNT = 15
array = []

def getList():
    for i in range (AMOUNT):
        number = input(f"Ingresa el datp {i + 1}: ")
        number = int(number)
        array.append(number)
    with open("file.txt", "w") as output:
        for row in array:
            output.write(str(row) + ' ')

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
getList()
with open("file.txt", "rb") as handle:
    print(proxy.python_logo().data)
    #handle.write(proxy.python_logo().data)
proxy.searchInFile()