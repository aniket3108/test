name = 'Aniket Anand'
age = 32 # not a lie
height = 69 # inches
weight = 152 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'
i2c= 2.54
p2k=0.45

print(f"Lets talk about {name}.")
print(f"He's {height*i2c} centimeters tall.")
print(f"He's {weight*p2k} kilograms heavy.")
print("Actually that's not too heavy or is it.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height} and {weight} I get {total}")
