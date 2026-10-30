prices = [100, 500, 200, 250, 100]
quantities = [2, 2, 5, 4, 15]

for i in range(5):
    total = prices[i] * quantities[i]

    if total >= 1000:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    print("Test Case:", i + 1)
    print("Total:", total)
    print("Discount:", discount)
    print("Final Bill:", final_bill)