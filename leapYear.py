def isLeapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            pass
        else:
            return True
    else:
        return False
