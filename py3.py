celcius = [int(input('Input temp in celcius \n'))]
fahrenheit = []

for temp in celcius:
    fahrenheit = (9/5*temp+32)

print(f'{fahrenheit}°f')