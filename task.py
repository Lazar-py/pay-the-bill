print('Welcome to the tip calculator!')
bill = float(input('What was the total bill? $'))
tip = int(input('How much tip would you like to give? $'))
people = int(input('How many people are there?'))
percentage = bill * (tip / 100)
total = (bill + percentage) / people
print(f'Each person should pay: ${round(total,2)}')