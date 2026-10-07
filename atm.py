# Task 2: ATM Withdrawal
balance = 50000
amount = int(input("Enter withdrawal amount (KSh): "))

if amount <= 0:
    print("Error: amount must be greater than zero.")
elif amount > balance:
    print("Error: insufficient funds.")
elif amount % 500 != 0:
    print("Error: amount must be a multiple of KSh 500.")
else:
    balance -= amount
    print(f"Withdrawal successful. Remaining balance: KSh {balance}")
