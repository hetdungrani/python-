def fahrenheit_to_celsius(fahrenheit):
 celsius = (5 * (fahrenheit - 32)) / 9.0
 return celsius
fahrenheit = 100
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"The temperature in Celsius is: {celsius:.2f}°C")
