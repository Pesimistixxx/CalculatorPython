def countBigNums(x):
    if 5 <= x <= 20:
        return 2
    if x % 10 == 1:
        return 0
    if 2 <= (x % 10) <= 4:
        return 1
    return 2


def inputCalculations(inp):
    c = None
    maxlen = 0
    isfrac = False
    iszero = False
    nums = []
    temp = []
    for elem in inp:
        if elem == "и":
            isfrac = True
        elif elem in bignumtoint:
            if elem in strtoint:
                c = 1
            elif c == None:
                return "Неправильный Ввод"
            c = c * bignumtoint[elem]
            temp.append(c)
            c = 0
            if "тысяч" in elem:
                c = sum(temp)
                temp = []
        elif elem in strtoint:
            if elem == "открывается":
                nums.append("(")
            elif elem == "закрывается":
                if c != None:
                    nums.append(c)
                    c = None
                nums.append(")")
            elif type(strtoint[elem]) == int:
                if strtoint[elem] == 0:
                    iszero = True
                if not isfrac:
                    if c == None:
                        c = 0.0
                    c += strtoint[elem]
                else:
                    if c == None:
                        c = 0.0
                    maxlen = max(len(str(strtoint[elem])), maxlen)
                    c += strtoint[elem] / (10 ** (maxlen))
            elif elem == "плюс" or elem == "минус" or elem == "умножить" or elem == "делить" or elem == "остаток" or elem == "разделить" or elem == "степени":
                if c != None:
                    nums.append(c)
                isfrac = False
                maxlen = 0
                nums.append(strtoint[elem])
                c = None
        elif elem in ignorelist or elem in fracword2 or elem in fracword or elem in fracword3:
            continue
        else:
            return "Неправильный Ввод"
    if nums.count("(") != nums.count(")"):
        return "Неправильный Ввод"
    if c == None and nums[-1] != ")":
        return "Неправильный Ввод"
    elif c != None:
        nums.append(c)
    if iszero:
        if len([item for item in nums if item != 0]) <= 1:
            return "Неправильный Ввод"
    else:
        if len([item for item in nums if item != 0]) <= 2:
            return "Неправильный Ввод"
    strnums = ''.join(map(str, nums))
    strnums.replace("--", "+")
    try:
        return eval(strnums)
    except:
        if "/0" in strnums:
            return "Ошибка деления на 0"
        else:
            return "Неправильный ввод"


def printCalculations(res):
    resbybit = [[], []]
    c = 0
    res = round(res, 4)
    res2 = str(res).split(".")
    for i in range(2):
        lc = len(res2[i])
        for elem in res2[i]:
            lc -= 1
            sym = int(elem) * 10 ** (lc)
            if sym > 999 and i == 0:
                c += int(elem) * 10 ** (lc % 3)
                bit = lc // 3
                bitlife = lc % 3
                if bitlife == 0:
                    cnt = countBigNums(c)
                    resbybit[i].append(sym // 1000 ** bit)
                    if len(resbybit[i]) >= 2:
                        if resbybit[i][-2] == 10:
                            resbybit[i][-2] = 10 + resbybit[i][-1]
                            resbybit[i].pop()
                    resbybit[i].append(bignumtostr[bit - 1][cnt])
                    c = 0
                else:
                    resbybit[i].append(sym // 1000 ** bit)
            else:
                resbybit[i].append(sym)
        if len(resbybit[i]) >= 2:
            if resbybit[i][-2] == 10:
                resbybit[i][-2] = 10 + resbybit[i][-1]
                resbybit[i].pop()
    i = -1
    j = -1
    if "тысячи" in resbybit[0]:
        j = resbybit[0].index("тысячи")
    if "тысяча" in resbybit[0]:
        j = resbybit[0].index("тысяча")
    for elem in resbybit[0]:
        i += 1
        if elem == 0 and len(resbybit[0]) == 1:
            print(inttostr[elem], end=" ")
        if elem == 0:
            continue
        elif type(elem) == str:
            print(elem, end=" ")
        elif 1 <= elem <= 2 and j != -1 and j - i == 1:
            print(doubletostr[elem], end=" ")
        else:
            print(inttostr[elem], end=" ")
    if len([item for item in resbybit[1] if item != 0]) != 0:
        print("и", end=" ")
        for elem in resbybit[1]:
            if elem == 0:
                continue
            elif type(elem) == str:
                print(elem, end=" ")
            else:
                print(doubletostr[elem], end=" ")
        if res2[1][-1] == "1":
            print(fracword2[len(str(res2[1])) - 1])
        elif res2[1][-1] == "2":
            print(fracword3[len(str(res2[1])) - 1])
        else:
            print(fracword[len(str(res2[1])) - 1])

ignorelist = ["деления", "от", "на", "скобка","в"]
fracword = ["десятых", "сотых", "тысячных", "десятитысячных", "статысячных", "миллионых"]
fracword2 = ["десятая", "сотая", "тысячная", "десятитысячная", "статысячная", "миллионая"]
fracword3 = ["десятые", "сотые", "тысячные", "десятитысячные", "статысячные", "миллионые"]
bignumtoint = {"тысяча": 1_000,
               "тысячи": 1_000,
               "тысяч": 1_000,
               "миллион": 1_000_000,
               "миллиона": 1_000_000,
               "миллионов": 1_000_000,
               "миллиард": 1_000_000_000,
               "миллиарда": 1_000_000_000,
               "миллиардов": 1_000_000_000
               }
bignumtostr = [["тысяча", "тысячи", "тысяч"], ["миллион", "миллиона", "миллионов"],
               ["миллиард", "миллиарда", "миллиардов"]]
strtoint = {
    "ноль": 0,
    "один": 1,
    "одна": 1,
    "два": 2,
    "две": 2,
    "три": 3,
    "четыре": 4,
    "пять": 5,
    "шесть": 6,
    "семь": 7,
    "восемь": 8,
    "девять": 9,
    "десять": 10,
    "одиннадцать": 11,
    "двенадцать": 12,
    "тринадцать": 13,
    "четырнадцать": 14,
    "пятнадцать": 15,
    "шестнадцать": 16,
    "семнадцать": 17,
    "восемнадцать": 18,
    "девятнадцать": 19,
    "двадцать": 20,
    "тридцать": 30,
    "сорок": 40,
    "пятьдесят": 50,
    "шестьдесят": 60,
    "семьдесят": 70,
    "восемьдесят": 80,
    "девяносто": 90,
    "сто": 100,
    "двести": 200,
    "триста": 300,
    "четыреста": 400,
    "пятьсот": 500,
    "шестьсот": 600,
    "семьсот": 700,
    "восемьсот": 800,
    "девятьсот": 900,
    "тысяча": 1000,
    "две тысячи": 2000,
    "три тысячи": 3000,
    "четыре тысячи": 4000,
    "пять тысяч": 5000,
    "шесть тысяч": 6000,
    "семь тысяч": 7000,
    "восемь тысяч": 8000,
    "девять тысяч": 9000,
    "десять тысяч": 10000,
    "плюс": "+",
    "минус": "-",
    "умножить": "*",
    "делить": "/",
    "разделить": "/",
    "остаток": "%",
    "открывается": "(",
    "закрывается": ")",
    "степени": "**"
}

doubletostr = {
    1: "одна",
    2: "две",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять",
    10: "десять",
    11: "одиннадцать",
    12: "двенадцать",
    13: "тринадцать",
    14: "четырнадцать",
    15: "пятнадцать",
    16: "шестнадцать",
    17: "семнадцать",
    18: "восемнадцать",
    19: "девятнадцать",
    20: "двадцать",
    30: "тридцать",
    40: "сорок",
    50: "пятьдесят",
    60: "шестьдесят",
    70: "семьдесят",
    80: "восемьдесят",
    90: "девяносто",
    100: "сто",
    200: "двести",
    300: "триста",
    400: "четыреста",
    500: "пятьсот",
    600: "шестьсот",
    700: "семьсот",
    800: "восемьсот",
    900: "девятьсот",
    1000: "тысяча",
    2000: "две тысячи",
    3000: "три тысячи",
    4000: "четыре тысячи",
    5000: "пять тысяч",
    6000: "шесть тысяч",
    7000: "семь тысяч",
    8000: "восемь тысяч",
    9000: "девять тысяч",
    10000: "десять тысяч",
}

inttostr = {
    0: "ноль",
    1: "один",
    2: "два",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять",
    10: "десять",
    11: "одиннадцать",
    12: "двенадцать",
    13: "тринадцать",
    14: "четырнадцать",
    15: "пятнадцать",
    16: "шестнадцать",
    17: "семнадцать",
    18: "восемнадцать",
    19: "девятнадцать",
    20: "двадцать",
    30: "тридцать",
    40: "сорок",
    50: "пятьдесят",
    60: "шестьдесят",
    70: "семьдесят",
    80: "восемьдесят",
    90: "девяносто",
    100: "сто",
    200: "двести",
    300: "триста",
    400: "четыреста",
    500: "пятьсот",
    600: "шестьсот",
    700: "семьсот",
    800: "восемьсот",
    900: "девятьсот",
    1000: "тысяча",
    2000: "две тысячи",
    3000: "три тысячи",
    4000: "четыре тысячи",
    5000: "пять тысяч",
    6000: "шесть тысяч",
    7000: "семь тысяч",
    8000: "восемь тысяч",
    9000: "девять тысяч",
    10000: "десять тысяч",
}


def main():
    inp = input().lower().split()
    res = inputCalculations(inp)
    while res == "Неправильный Ввод" or res == "Ошибка деления на 0":
        if res == "Неправильный Ввод":
            print("Неправильный Ввод")
        elif res == "Ошибка деления на 0":
            print("Ошибка деления на 0, введите число заново")
        inp = input().split()
        res = inputCalculations(inp)
    printCalculations(res)

if __name__ == "__main__":
    main()

# двести пятьдесят два миллиона триста двадцать три тысячи сто двадцать три минус восемь
# девятнадцать и восемьдесят две сотых разделить на девяносто девять
# us and mys i agree you max because your father worker of alfa bank
# триста двадцать две тысячи тридцать один плюс один
# сорок четыре тысячи минус пять тысяч
# тысяча плюс одиннадцать тысяч
