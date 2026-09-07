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


# Single input containing withdrawal amounts
withdrawals = list(map(int, input().split()))

# ATM balance
balance = int(input())

atm_withdrawals(withdrawals, balance)