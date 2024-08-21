# WAP to Calculate BMI. Mass in KG, Height in CM. If (BMI < 14):Unhealthy, if (BMI >=14):Healthy.

# User Inputs
weight_kg = float(input("Enter the weight in KG: "))
height_cm = float(input("Enter the height in CM: "))

# BMI Formula Function
BMI = weight_kg / (height_cm/100)**2

# if-else Condition
if (BMI <= 14):
    print(f"Your BMI is: {BMI}.\nYou are Unhealthy.")
else:
    print(f"Your BMI is: {BMI}.\nYou Are Healthy.")
