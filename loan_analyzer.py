# coding: utf-8
import csv
from pathlib import Path

# Part 1: Automate the Calculations.

# # Automate the calculations for the following loan portfolio summaries.
loan_costs = [500, 600, 200, 1000, 450]

# Used the `len` function to calculate the total number of loans in the list.
# Then printed the number of loans from the list
number_of_loans = len(loan_costs)
print(f"The number of loans being issued are {number_of_loans}")

# Used the `sum` function to calculate the total of all loans in the list.
# Then printed the total value of the loans
sum_of_loans = sum(loan_costs)
print(f"The total value of the all loans are ${sum_of_loans}")

# Using the sum of all loans and the total number of loans, calculated the average loan price.
# Then printed the average loan amount
average_loan_price = sum_of_loans / number_of_loans
print(f"The average loan amount is ${average_loan_price}")


# """Part 2: Analyze Loan Data.

# Analyze the loan to determine the investment evaluation.

# 1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
#     a. Save these values as variables called `future_value` and `remaining_months`.
#     b. Print each variable.

#     **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
#     **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

# 2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
# 3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#     a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#     b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

#     If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
# """

# Given the following loan data, calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Used get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Printed each variable.
remaining_months = loan.get("remaining_months")
future_value = loan.get("future_value")
print(f"The are, {remaining_months} months remaining on the loan")
print(f"The future value of the loan will be ${future_value}")

# Used the formula for Present Value to calculate a "fair value" of the loan.
# Used a minimum required return of 20% as the discount rate.
discount_rate = .20
fair_value = future_value / (1 + discount_rate/12) ** remaining_months
print(f"The fair value of the loan is ${round(fair_value,2)}") 

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# Wrote a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
if fair_value >= loan.get("loan_price"):
    print("The loan is at least the cost to but it.")
elif fair_value < loan.get("loan_price"):
    print("The loan is too expensive and not worth the price.")


# """Part 3: Perform Financial Calculations.

# 1. Define a new function that will be used to calculate present value.
#     a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#     b. The function should return the `present_value` for the loan.
# 2. Use the function to calculate the present value of the new loan given below.
#     a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# """

# Given the following loan data, calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Defined a new function that will be used to calculate present value.
#    This function includes parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function returns the `present_value` for the loan.
annual_discount_rate=0.20
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate/12)**remaining_months
    return present_value

# Used the function to calculate the present value of the new loan given below.
#     Used an `annual_discount_rate` of 0.2 for this new loan calculation.
present_value = calculate_present_value(new_loan["future_value"],new_loan["remaining_months"],annual_discount_rate)
print(f"The present value of the loan is ${round(present_value,2)}")


# """Part 4: Conditionally filter lists of loans.

# In this section, used a loop to iterate through the series of loans and selected only the inexpensive loans.

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Created an empty list called `inexpensive_loans`
inexpensive_loans = []

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

# Print the `inexpensive_loans` list
print("These loans are priced at $500 or less", inexpensive_loans)


# """Part 5: Save the results.

# Output this list of inexpensive loans to a csv file
#     1. Use `with open` to open a new CSV file.
#         a. Create a `csvwriter` using the `csv` library.
#         b. Use the new csvwriter to write the header variable as the first row.
#         c. Use a for loop to iterate through each loan in `inexpensive_loans`.
#             i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

# Set the output header
header = ["Loan_Price", "Remaining_Months", "Repayment_Interval", "Future_Value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Used the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
with open(output_path, "w", newline='') as csvfile:
    csvwiter = csv.writer(csvfile)
    csvwiter.writerow(header)
    for row in inexpensive_loans:
        csvwiter.writerow(row.values())
