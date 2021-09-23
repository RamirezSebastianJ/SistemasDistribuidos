import threading
from math import ceil


def add_function(position, result, loweLimit, higheLimit):
    total = 0
    for n in range(loweLimit, higheLimit):
        total += n
    
    result[position] = total


if __name__ == "__main__":
    maximunLimit = 100
    minimunLimit = 1
    numberOfThreads = 10
    threads = []
    result = [None] * numberOfThreads
    rank = ceil((maximunLimit-minimunLimit) / numberOfThreads)
    

    for i in range(numberOfThreads):
        t = threading.Thread(target=add_function, args=(i, result, minimunLimit,  min(maximunLimit, minimunLimit + rank)+1))
        threads.append(t)
        t.start()
        minimunLimit += rank + 1
    
    for thread in threads:
        thread.join()
    
    print("SUM", sum(result))



