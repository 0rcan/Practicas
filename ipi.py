
def ipi(income):

    if income <= 85528:
      total = (income * (18/100)) - 556.2

    elif income > 85528:
      total = ((income - 85528) * (32/100)) + 14839.2

    print(f"\n Your budget is: {round(total)}")


if __name__ == '__main__':
    i = 0
    while i < 1:
        try:
            income = float(input("\n Entry your Income: "))
            i += 1
        except Exception:
            print("\n ====ERROR Enter a float value=====")
            i = 0
        else:
            if income <= 0:
                print("\n ====Enter a value positive or greather that 0=====")
                i = 0
    ipi(income)
