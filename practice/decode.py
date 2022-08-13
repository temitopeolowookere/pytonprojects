def celsius_to_fah(celsius_float):
    return celsius_float * 1.8 + 32
celsius_float = float(input("enter a celsius temperature"))
fah_float = celsius_to_fah(celsius_float)
print(celsius_float, "converts to " , fah_float, " fahrenheit")

