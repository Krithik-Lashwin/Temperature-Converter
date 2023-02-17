celcius = float(input("Enter the temperature:"))
farenheit = (celcius*1.8) + 32
print("%0.1f°C = %0.1f°F"%(celcius,farenheit))
if(farenheit>104):
    print("The temperature is too hot!")
elif(farenheit<50):
    print("The temperature is too cold!")
else:
    print("The Temperature is normal")