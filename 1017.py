#Littl John wants to calculate and show the amount of spent fuel liters on a trip, using a car that does 12 Km/L. For this, he would like you to help him through a simple program. 
#To perform the calculation, you have to read spent time (in hours) and the same average speed (km/h).
#In this way, you can get distance and then, calculate how many liters would be needed. Show the value with three decimal places after the point


    
def main():
    spentTime, avgSpeed = readInput();
    km = getDistanceKm(spentTime, avgSpeed)
    print("\nLiters consumed in a vehicle with 12Km/L fuel usage: {}".format(litersConsumed(12, km)))

def readInput():
    print("\nSubmit the spent time (in hours): ")
    spentTime = float(input())
    print("\nSubmit then average speed")
    avgSpeed = float(input())
    return spentTime,avgSpeed

def getDistanceKm(hours, speed):
    return hours * speed

def litersConsumed(kmPerLiterRatio, distance):
    return kmPerLiterRatio * distance

if __name__ == "__main__":
    main()
