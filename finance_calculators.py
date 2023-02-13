import math

print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print("\n")
print("investment \t - \t to calculate the amount of interest you'll earn on your investment")
print("bond \t\t - \t to calculate the amount you'll have to pay on a home loan \n")

option = input("Please choose 'investment' or 'bond': \n")

#first block of code calculates investment returns
if option.lower() == "investment":                  
    invest_return = 0.0
    deposit_amount = float(input("How much are you depositing for investment? (in R) \n"))
    interest_rate = float(input("What is the interest rate? (Please enter the percentage as a number) \n"))
    invest_years = float(input("How many years do you plan to invest for? \n"))
    interest = input("Do you want 'simple' or 'compound' interest? \n")

    #calculate simple interest
    if interest.lower() == "simple":
        invest_return = deposit_amount * (1 + (interest_rate/100) * invest_years)
        print(f"You will get R{invest_return} back after {invest_years} years.")

    #calculate compound interest
    elif interest.lower() == "compound":
        invest_return = deposit_amount * math.pow((1 + (interest_rate/100)), invest_years)
        print(f"You will get R{round(invest_return, 2)} back after {invest_years} years.")

    #catch non-pertinent inputs
    else:
        print("Please enter 'simple' or 'compound'")


#second block of code calculates bond repayments
elif option.lower() == "bond":
    monthly_payment = 0.0
    house_value = float(input("What is the current value of the house? (in R) \n"))
    annual_rate = float(input("What is the annual interest rate? (Please enter the percentage as a number) \n"))
    monthly_rate = annual_rate / 12 / 100       #remember to divide annual rate by 12 AND 100 to get a usable monthly float value
    invest_months = float(input("How many months do you plan to repay the bond over? \n"))

    #monthly payment calculation
    monthly_payment = (monthly_rate * house_value) / (1 - ((1 + monthly_rate) ** (-invest_months)))

    print(f"You will need to pay R{round(monthly_payment, 2)} per month.")

#catch non-useful inputs
else:
    print("Please choose 'investment' or 'bond'.")