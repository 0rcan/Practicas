def durvey(num):
    n = 0
    woman = 0
    men = 0
    men_mio = 0
    men_vehicle = 0
    men_bike = 0
    woman_mio = 0
    woman_vehicle = 0
    woman_bike = 0
    for e in range(0,num):
        n += 1
        try:
            print(f"\n ============Person {n}============")
            sex1 = int(input(f"""\n [1] WOMAN
    [2] MEN \n    Choose a sex: """))
            if sex1 == 1:
                woman += 1
            elif sex1 == 2:
                men += 1
            transport1 = int(input(f"""\n [1] MIO \n [2] Vehiculo particular
    [3] Bike
        Selec a tranport: """))

            if transport1 == 1:
                #print(men_bike)
                if sex1 == 2 and transport1 == 1:
                    men_mio += 1
                elif sex1 == 1 and transport1 == 1:
                    woman_mio += 1
            if transport1 == 2:
                #print(men_bike)
                if sex1 == 2 and transport1 == 2:
                    men_vehicle += 1
                elif sex1 == 1 and transport1 == 2:
                    woman_vehicle += 1
            if transport1 == 3:
                #print(men_bike)
                if sex1 == 2 and transport1 == 3:
                    men_bike += 1
                elif sex1 == 1 and transport1 == 3:
                    woman_bike += 1
        except ValueError:
            print("\n Enter a number")
            e -= 1
            n -= 1

    print(f"\n Number of womens {woman} who use MIO: {woman_mio}")
    percentage = round((men_bike * 100) / num)
    print(f"""\n Number of mens {men} who use Bike: {men_bike}
    and their percentage is: {percentage}%""")

if __name__ == '__main__':
    i = 0
    while i < 1:
        try:
            num = int(input("\n Enter a nuber of people: "))
            i += 1
        except ValueError:
            print("\n Enter a number")
            i = 0
        else:
            if num <= 0:
                print("\n Enter a number positive")
                i = 0
    durvey(num)