# Calculate the monthly payments of a fixed term mortgage,
# over given Nth terms at a given interest rate.
# Also figure out how long it will take the user to pay back the loan.
# For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually)

# Fixed Term Mortgage, aka Vanilla Wafer
print "\nFixed Term Morgage"
interest_rate = float(raw_input("Percent Interest Rate: "))
amount = float(raw_input("Mortgage amount: "))
duration = float(raw_input("How many years: "))

monthly = (amount * (1 + interest_rate/100.0)) / (12.0 * duration)
print "Monthly payments are: $%.2f" % monthly
