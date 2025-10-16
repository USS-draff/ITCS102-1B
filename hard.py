loan = eval(input("Enter the amount of you want to loan ---->"))
loan2 = eval(input("Enter the loan period in years ---->"))

months = loan2 * 12
principle = loan / months
balance = loan
print("months\t\t|\tprinciple payment\t|\tRemaining Balance\t|\tInterest")

for i in range(1, months + 1, 1):
    balance -= principle
    interest = balance * 0.03
    monthly = principle + interest
    print(f"{i}\t\t|\t{round(principle, 2)}\t\t\t|\t{round(balance,2)}\t\t\t|\t{interest}\t")