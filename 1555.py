#In the last math class, Rafael, Beto and Carlos learned some new math functions. Each one of them liked one particular function, and they decided to compete to see which function had the higher outcome.
#The function that Rafael chose is r(x, y) = (3x)² + y².
#Beto chose the function b(x, y) = 2(x²) + (5y)².
#Carlos, however, chose the function c(x, y) = -100x + y³.
#Given the values of x and y, say who chose the function with higher outcome.
import math as m

def main():
    testAmount = readTestsAmount()
    winners = test(testAmount)
    printWinners(winners)


def readTestsAmount():
    print("\nSubmit the number of tests")
    times = int(input())
    if times > 0: 
        return times

    print("\nNumber of tests must be more than 0")
    readTestsAmount()

def readXY():
    print("\nX: ")
    x = float(input())
    print("\nY: ")
    y = float(input())
    return x,y

def test(testAmount):
    winners = []
    for _ in range(testAmount):
        x, y = readXY()
        resRafael = testRafael(x,y)
        resBeto = testBeto(x,y)
        resCarlos = testCarlos(x,y)
        if (resRafael >= resBeto) and (resRafael >= resCarlos):
            winners.append((x,y,"Rafael"))
        elif (resBeto >= resRafael) and (resBeto >= resCarlos):
            winners.append((x,y,"Beto"))
        else:
            winners.append((x,y,"Carlos"))
    return winners

def testRafael(x,y):
    return m.pow(3*x, 2) + y * y

def testBeto(x,y):
    return 2*(x*x) + m.pow(5*y, 2)

def testCarlos(x,y):
    return -100 * x + m.pow(y,3)

def printWinners(winners):
    print("\nWinners:")
    for i in range(len(winners)):
        x,y,winner = winners[i]
        print(f"\n{winner} [x={x}, y={y}]")

if __name__ == "__main__":
    main()
