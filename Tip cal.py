print("Welcome to the tip calculator !")
tot=float(input("What is the total bill ? $"))
tip=int(input("What percentage tip would you like to give ? 10,12 or 15 ?"))
count=int(input("How many people to split the bill ? "))

bill_total=tot*(100+tip)/100
ep=round(bill_total/count , 2)
print("Each person should pay : $",ep)


