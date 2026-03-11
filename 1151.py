def internalFib(targetNum, numArr):
    if(len(numArr) == targetNum):
        return numArr

    
    if(len(numArr) == 0):
        numArr.append(0) 
    elif(len(numArr) == 1):
        numArr.append(1)
    else:
        high = len(numArr)-1
        numArr.append(numArr[high] + numArr[high-1])
    return internalFib(targetNum, numArr)

def fib(n):
    return internalFib(n, [])

def readInput():
    print("\nInforme o número de números de elementos do fibonacci:")
    n = int(input())
    if(0 < n < 46):
        return n

    print("Valor invalido: deve ser entre 0 e 46")
    readInput()

def main():
    fibRes = fib(readInput())
    print(fibRes)    

if __name__ == "__main__":
    main()
