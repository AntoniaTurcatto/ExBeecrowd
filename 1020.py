
#Read an integer value corresponding to a person's age (in days) and print it in years, months and days, followed by its respective message “ano(s)”, “mes(es)”, “dia(s)”.

#Note: only to facilitate the calculation, consider the whole year with 365 days and 30 days every month. 
#In the cases of test there will never be a situation that allows 12 months and some days, like 360, 363 or 364. This is just an exercise for the purpose of testing simple mathematical reasoning.
def main():
    days = readInput();
    y, m ,d = dateFromDays(days)
    print("\nYears: {}\n Months: {}\nDays: {}".format(y, m, d))

def readInput():
    print("\nSubmit the days of a person's life: ") 
    days = int(input())
    if days >= 0:
        return days

    print("It can not be less than 0")
    readInput()

def dateFromDays(days):
    years = days // 365
    daysLastYear = days % 365
    months = daysLastYear // 30
    finalDays = daysLastYear % 30 
    return years, months, finalDays

if __name__ == "__main__":
    main()
