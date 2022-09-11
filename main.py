def karekok(x,y):

    if(x<=1):
        return("Tanımsız")
    for i in range(x):
        if(i*i >x):
            ilksayi=i-1
            break
    for i in range(1,y+1):
        i=10**i
        for j in range(10):
            if((ilksayi + j/i) **2 > x):
                ilksayi = (ilksayi + (j-1)/i)
                break
    return ilksayi


while True:
    try:
        print(karekok(int(input("Sayı: ")),int(input("Virgülden sonra kaç hane alınacak?"))))
    except ValueError:
        print("Integer bir sayı giriniz.")
        continue