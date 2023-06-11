def gross_salary(amount, bonus, allowance):
    grossSalary= amount+bonus+allowance
    return grossSalary

amt=int(input("Enter the amount: "))
bon=int(input("Enter the bonus: "))
all=int(input("Enter the allowance: "))
print(gross_salary(amt, bon, all))
