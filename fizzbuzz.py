def fizzbuzz(val):
    if(val%3 == 0 and val%5 == 0):
        return "FizzBuzz"
    elif(val %3 == 0):
        return "Fizz"
    elif (val %5 == 0):
        return "Buzz"
    else:
        return val

def iterate():
    for i in range(1, 101):
        print(fizzbuzz(i))