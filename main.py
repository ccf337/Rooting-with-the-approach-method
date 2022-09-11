def sqrt(x, y):

    if(x<=1):
        return("Undefined")
    for i in range(x):
        if(i*i >x):
            number=i-1
            break
    for i in range(1,y+1):
        i=10**i
        for j in range(10):
            if((number + j/i) **2 > x):
                number = (number + (j-1)/i)
                break
    return round(number,y) # Numbers like 0 and 9 cause the for loop to return too much, so the digit constraint was used.


while True:
    try:
        print(sqrt(int(input("number: ")), int(input("Number of digits after comma"))))
    except ValueError:
        print("Please enter an integer type number.")
        continue
