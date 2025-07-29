#FITNESS CHALLENGE APP 
def calculate_bmi(weight, height):
    return weight / (height/100)**2

def classify_bmi(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "fit, Congratulations!!"
    else:
        return "overweight"
#User details
name = input("What is your name?                     = ")
age = int(input("What is your age?                      = "))
gender = input("What is your gender?                   = ")
height_cm = float(input("What is your height in centimeters?    = "))
weight_kg = float(input("What is your weight in kilograms?      = "))

bmi = calculate_bmi(weight_kg, height_cm)
classification = classify_bmi(bmi)

print(f"\nHello {name}.\nYour BMI is {bmi:.2f}. \nYou are {classification}.")
#Using BMI representation of user's health condition
if classification == "underweight":
    print("\nHere are 5 challenges to help you become fit \n Choose any one of the following:")
    print("\n1. Increase your daily calorie intake with nutrient-rich foods.")
    print("\n2. Start a strength training routine to build muscle mass.")
    print("\n3. Incorporate healthy fats into your diet, such as avocados and nuts.")
    print("\n4. Strength training to build muscle mass.")
    print("\n5. 30-minute gentle yoga for relaxation.")

elif classification == "fit, Congratulations!!":
    print("\nHere are 5 ways to keep your body fit \n Choose any one of the following:")
    print("\n1. Maintain a balanced diet rich in fruits, vegetables, and whole grains.")
    print("\n2. Engage in regular physical activity, such as cardio and strength training.")
    print("\n3. Stay hydrated by drinking plenty of water throughout the day.")
    print("\n4. Get enough sleep each night to support overall health and well-being.")
    print("\n5. Practice stress-reducing techniques like meditation or yoga.")

elif classification == "overweight":
    print("\nHere are 5 challenges to help you become fit \n Choose any one of the following:")
    print("\n1. Reduce your daily calorie intake by avoiding sugary drinks and processed foods.")
    print("\n2. Running for 30 minutes (daily).")
    print("\n3. Skipping ropes for 30 minutes (daily).")
    print("\n4. Brisk walking for 40 minutes (daily).")
    print("\n5. Cycling for 45 minutes (daily).")

options = 5
if classification in ["underweight", "overweight"]:
    options = int(input("\nWhich option would you like to choose within 5? (1-5)      = "))
    if options < 1 or options > 5:
        print("Invalid option count. Defaulting to 5.")
        options = 5

# Track user's progress for one month
target_weight = weight_kg
if classification == "underweight":
    target_weight += float(input("\nHow many kilograms would you like to gain in one month?     ="))
    print(f"\nTracking your progress to gain {target_weight - weight_kg} kg in one month...")

elif classification == "overweight":
    target_weight -= float(input("\nHow many kilograms would you like to lose in one month?     = "))
    print(f"\nTracking your progress to lose {weight_kg - target_weight} kg in one month...")

print("\nOne month later...")

# Update user's weight based on progress
weight_kg = target_weight

print(f"\n{name}, your weight after one month is {weight_kg:.2f} kg.")

if options < 1 or options > 5:
    print("Invalid option count. Defaulting to 5.")
    options = 5
#User's selected choice for health improvement
if classification == "underweight":
    print("\n You have choosed following option:")
    if options == 1:
        print("\n1. Increase your daily calorie intake with nutrient-rich foods.")
    if options == 2:
        print("\n2. Start a strength training routine to build muscle mass.")
    if options == 3:
        print("\n3. Incorporate healthy fats into your diet, such as avocados and nuts.")
    if options == 4:
        print("\n4. Strength training to build muscle mass.")
    if options == 5:
        print("\n5. 30-minute gentle yoga for relaxation.")

elif classification == "fit, Congratulations!!":
    print("\nYou have choosed following option:")
    if options == 1:
        print("\n1. Maintain a balanced diet rich in fruits, vegetables, and whole grains.")
    if options == 2:
        print("\n2. Engage in regular physical activity, such as cardio and strength training.")
    if options == 3:
        print("\n3. Stay hydrated by drinking plenty of water throughout the day.")
    if options == 4:
        print("\n4. Get enough sleep each night to support overall health and well-being.")
    if options == 5:
        print("\n5. Practice stress-reducing techniques like meditation or yoga.")

elif classification == "overweight":
    print("\n You have choosed following option:")
    if options == 1:
        print("\n1. Reduce your daily calorie intake by avoiding sugary drinks and processed foods.")
    if options == 2:
        print("\n2. Running for 30 minutes (daily).")
    if options == 3:
        print("\n3. Skipping ropes for 30 minutes (daily).")
    if options == 4:
        print("\n4. Brisk walking for 40 minutes (daily).")
    if options == 5:
        print("\n5. Cycling for 30 minutes (daily).")
        
print("\nComplete this task for one month and report us after every 10 days!!!")

# Define the motivational lines
motivational_lines = [
    "\n  HURREY!!!! You have completed the choosen task for given time! \n Here are some motivational lines for your HARD WORK and CONSULTANCY!!!\n"
    "\nEvery step you take brings you closer to your goals!",
    "\nSuccess is the sum of small efforts, repeated day in and day out.",
    "\nBelieve you can and you're halfway there!"
    "\n\n STAY LOYAL WITH YOUR HEALTH AND YOU WILL BE FINE FOREVER!!!"
    ]

# Ask user if they completed the task for the first 10 days
first_10_days = input("\nDid you complete the task for the first 10 days? (yes/no): ")

if first_10_days.lower() == "yes":
    # Ask user if they completed the task for the next 20 days
    next_20_days = input("\nDid you complete the task for the next 20 days? (yes/no): ")
    
    if next_20_days.lower() == "yes":
        # Ask user if they completed the task for the final 30 days
        final_30_days = input("\nDid you complete the task for the final 30 days? (yes/no): ")
        
        if final_30_days.lower() == "yes":
            # Print motivational lines
            print("\n".join(motivational_lines))
        else:
            print("\nThat's okay! Remember, every day is a new opportunity to start fresh.")
    else:
        print("\nRemember, consistency is key. Let's start fresh and commit to the next 30 days!")
else:
    print("\nNo worries! It's never too late to start. Let's begin from the first 10 days again.")
   