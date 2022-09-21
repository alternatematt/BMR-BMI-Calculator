maleBMR = 0
femaleBMR = 0
userBMI = 0
targetBMI = 0

# VALIDATING WEIGHT IS VALID
weight = int(input("Enter weight between 30 and 250kg: "))

while weight > 250 or weight < 30:
    weight = int(input("Enter weight between 30 and 250kg: "))

# VALIDATING HEIGHT IS VALID
height = int(input("Enter height between 120 and 210cm: "))

while height > 210 or height < 120:
    height = int(input("Enter height between 120 and 210cm: "))

# VALIDATING AGE IS VALID
age = int(input("Enter Age between 14 and 100 years old: "))

while age > 100 or age < 14:
    age = int(input("Enter Age between 14 and 100 years old: "))

# VALIDATING GENDER IS VALID
gender = ''

while gender != "Male" or gender != "male" or gender != "female" or gender != "Female":
    gender = str(input("Are you Male or Female?: "))

    if gender == "Male" or "male":
        maleBMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)

        height = (height / 100)
        userBMI = weight / (height * height)

        #Underweight
        if userBMI < 18.5:
            format_maleBMR = "{:.2f}".format(maleBMR)
            print(f"Your BMR is {format_maleBMR}")
            format_userBMI = "{:.1f}" .format(userBMI)
            print(f"Your BMI is {format_userBMI}")
            print("Your target is 18.5 BMI")
        #Normal weight
        elif userBMI < 24.9 or userBMI > 18.5:

            format_maleBMR = "{:.2f}".format(maleBMR)
            print(f"Your BMR is {format_maleBMR}")
            format_userBMI = "{:.1f}" .format(userBMI)
            print(f"Your BMI is {format_userBMI}")
            print("No target")
        #Over weight
        elif userBMI < 29.9 or userBMI > 25:

            format_maleBMR = "{:.2f}".format(maleBMR)
            print(f"Your BMR is {format_maleBMR}")
            format_userBMI = "{:.1f}" .format(userBMI)
            print(f"Your BMI is {format_userBMI}")
            print("Your target is 24.9 BMI")
        #Obese
        elif userBMI > 30:

            format_maleBMR = "{:.2f}".format(maleBMR)
            print(f"Your BMR is {format_maleBMR}")
            format_userBMI = "{:.1f}" .format(userBMI)
            print(f"Your BMI is {format_userBMI}")
            print("Your target is 24.9")
        break

    elif gender == "Female" or "female":
        femaleBMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    
        height = (height / 100)
        userBMI = weight / (height * height)
        #underweight
        if userBMI < 18.5:

            format_femaleBMR = "{:.2f}".format(femaleBMR)
            print(f"Your BMR is {format_femaleBMR}")
            format_userBMI = "{:.1f}" .format(userBMI)
            print(f"Your BMI is {format_userBMI}")
            print("Your target is 18.5 BMI")
        #normal weight
        elif userBMI < 24.9 or userBMI > 18.5:

            format_femaleBMR = "{:.2f}".format(femaleBMR)
            print(f"Your BMR is {format_femaleBMR}")
            format_userBMI = "{:.1f}" .format(userBMI)
            print(f"Your BMI is {format_userBMI}")
            print("No target")
        #over weight
        elif userBMI < 29.9 or userBMI > 25:

            format_femaleBMR = "{:.2f}".format(femaleBMR)
            print(f"Your BMR is {format_femaleBMR}")
            format_userBMI = "{:.1f}" .format(userBMI)
            print(f"Your BMI is {format_userBMI}")
            print("Your target is 24.9 BMI")
        #obese
        elif userBMI > 30:
 
            format_femaleBMR = "{:.2f}".format(femaleBMR)
            print(f"Your BMR is {format_femaleBMR}")
            format_userBMI = "{:.1f}" .format(userBMI)
            print(f"Your BMI is {format_userBMI}")
            print("Your target is 24.9 BMI")
        break

