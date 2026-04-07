#Conditional ststements (if, elif, else)

temperature= int(input('Enter the tempertaure in Celsius":'))

if temperature <0:
    print("Its's freezing, wear a heavy coat!")
elif temperature<15:
    print("It's chilly! You might need a jacket!")
elif temperature <27:
    print("The weather is mild. A light sweater should be enough.")

else:
    print("It's hot! Stay cool and hydrated")

temperature = 10
