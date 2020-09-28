# Write your code here
# python cares about white space. be cog
# return vs print - return is an actual value to use it in another . 
# Print 

annual_salary = input("Enter Your Desired Annual Salary Here: ")
portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
monthly_salary_saved = (int(annual_salary)/112) * float(portion_saved)
total_cost = input("Enter the cost of your dream home: ")
portion_down_payment = .25 * int(total_cost)
# print(portion_down_payment)

current_savings = 0


i = 1
while current_savings < portion_down_payment:
    current_savings += monthly_salary_saved
    investment_return = current_savings * (.04/12)
    current_savings += investment_return
    i += 1
print("It will take you", i, "months to save up for the downpayment!" )