def convert_temp(temp):
    fahren=(temp*9)/5+32
    return fahren

temperature=int(input("Enter the temperature in celsius: "))
print(convert_temp(temperature))