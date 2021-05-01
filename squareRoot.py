def average(a,b):
    return (a+b)/2

def squareRoot(num,low,high):
    for i in range(100):
        guess = average(low,high)
        if guess**2 == num:
            print("The square root of",num,"is approximately",guess,".")
            break
        elif guess**2 > num:
            high = guess
        else:
            low = guess
    print("The square root of",num,"is approximately",guess,".")


