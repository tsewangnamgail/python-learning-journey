def atm_withdrawals(withdrawals, balance):
    for amount in withdrawals:
        if amount <= balance:
            balance -= amount
            print("Withdrawal possible")
            print("Remaining balance:", balance)
        else:
            print("Withdrawal not possible")
            print("Balance:", balance)

    return balance


# Single input containing withdrawal amounts  ex:200 300 400   
withdrawals = list(map(int, input().split()))     #use to take multiple input in single line
# ATM balance  ex:5000
balance = int(input())

atm_withdrawals(withdrawals, balance)