def emi_calculator():
    principal = float(input("Enter the principal amount: "))
    annual_rate = float(input("Enter the annual rate (in %): "))
    tenure = int(input("Enter the tenure in months: "))
    monthly_rate = annual_rate / (12 * 100)

    emi_type = input("Enter the EMI type you want (fixed/reducing): ").lower()

    if emi_type == "fixed":
        total_interest = principal * monthly_rate * tenure
        total_payable = principal + total_interest
        emi = total_payable / tenure
        print(f"Your fixed EMI is Rs {emi:.2f}")

    elif emi_type == "reducing":
        emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure) / ((1 + monthly_rate) ** tenure - 1)
        print(f"Your reducing EMI is Rs {emi:.2f}")

    else:
        print("Please enter a valid EMI type.")
        

emi_calculator()





