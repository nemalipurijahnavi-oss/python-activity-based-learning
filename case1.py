test_cases = [50, 100, 150, 200, 250]

for units in test_cases:
    if units < 0:
        print("Invalid Units")
    elif units <= 100:
        bill = units * 2 + 50
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3 + 50
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5 + 50

    if units >= 0:
        print("Units:", units, "Bill:", bill)