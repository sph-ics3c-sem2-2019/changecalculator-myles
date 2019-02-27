#Change Calculator
# Read in a cost
# Read in the amount given
# Calculate the change
# Break the change into how many nickels, dimes, quarters
# loonies, toonies, $5s, $10s, $20s, $50s, $100s
# If amount is below the cost, say how much more they owe.
cost=float(input("Aye bruh how much does the item cost?"))
amount=float(input("And how much did you pay???"))
change=amount-cost
print("Here's your change my guy", change)
#how many 100s
num100=change//100
print(num100,"x $100")
change=change%100
#how many 50s
num50=change//50
print(num50, "x $50")
change=change%50
#how many 20s
num20=change//20
print(num20, "x $20")
change=change%20
#how many 10s
num10=change//10
print(num10, "x $10")
change=change%10
#how many 5s
num5=change//5
print(num5, "x $5")
change=change%5
#how many 2s
num2=change//2
print(num2, "x $2")
change=change%2
#how many 1s
num1=change//1
print(num1, "x $1")
change=change%1
