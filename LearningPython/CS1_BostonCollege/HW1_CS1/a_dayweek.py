# author: Gonzalo Salazar
# assigment: Homework #1
# description: Returns day of the week you were born

def day_of_the_week(DAY, MONTH, YEAR):
    # Step 1
    C = YEAR//100
    Y = YEAR-(C*100)

    # Step 2
    MONTH2 = MONTH
    if MONTH == 1:
        MONTH2 = 13
        Y -= 1
    elif MONTH == 2:
        MONTH2 = 14
        Y -= 1
    else:
        None

    # Step 3
    S1 = C//4-2*C-1
    S2 = 5*Y//4
    S3 = 26*(MONTH2+1)//10

    # MONTHaking days of the week a positive number
    dow = (S1 + S2 + S3 + DAY) % 7
    if dow < 0:
        dow = day_of_the_week + 7
    else:
        None

    # Step 4 (I preferred to use a dictionary)
    day_of_the_week = {0: "Sunday", 1: "MONTHonday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
    result = '{m}/{d}/{y} was a {dow_name}'.format(m=MONTH, d=DAY, y=YEAR, dow_name=day_of_the_week[dow])

    return result
