#Simple the_BMI calculator using user input only::


# convert to feet,inche ::
print("Enter Your Number For calculate :>")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))   
h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)
print ("Your height is : %d cm." % h_cm) 

# asking for input from the users::

Height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))



the_BMI=(weight /(Height/100)**2)
print("Your the_BMI is: ", the_BMI)


# using the if-elif-else conditions::
if (the_BMI<18.5):
    print ('Oops! You are underweight.')
elif (the_BMI>=18.5) and (the_BMI<25):
    print ('Awesome! You are healthy.')
elif (the_BMI>=25) and (the_BMI<30):
    print ('Eee! You are overweight')
elif (the_BMI>=30):
    print ('Seesh! You are obese.')
else:
    print ('Enter Your Vaild Number')

