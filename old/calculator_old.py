from settings_controller import SettingsController
from math import factorial, pi, e, sin, cos, tan, log10
SettingsController.loadFrom("settings.json")

class Calculator():
    DEFAULT     = 0
    EQUALITY    = 1
    INEQUALITY  = 2

    replacement = {
        "**"    : ['^'],
        "=="    : ["="],
        "<="    : ["<=="],
        ">="    : [">=="],
        "pi"    : ["π"],
        "sin"   : ['5in'],
        "cos"   : ['c05', 'co5', 'c0s'],
        "lg"    : ['e9', 'eg', 'l9'],
        "ln"    : ['en'],
        "log"   : ['e09', 'l09', 'l0g', 'lo9', 'eo9', 'eog', 'e0g'],
    }



    @staticmethod
    def calc(str):

        for i in Calculator.replacement.keys():
            for j in Calculator.replacement[i]:
                print(i, j)
                str = str.replace(j, i)
                print(str)


        while (str.find("!") != -1):
            findex = str.find("!")
            ans, start, stop = Calculator.replaceFactorial(str[:findex+1], findex)
            str = str.replace(str[start:stop]+"!", "factorial("+ans+")")

        res = ""
        mode = Calculator.DEFAULT
        for char in str:
            if char in ["<", ">", "="]:
                mode = Calculator.INEQUALITY
                break
            else:
                try:
                    res = eval(str)
                    mode = Calculator.EQUALITY
                except Exception:
                    mode = Calculator.DEFAULT
        return res, mode



    @staticmethod
    def replaceFactorial(str, findex):
        newStr = ""
        bracket = 0
        pointer = findex-1

        while True:
            char = str[pointer]
            if char == ")":
                bracket += 1
                newStr = char + newStr
                pointer -= 1
            elif char == "(" and bracket > 1:
                bracket -= 1
                newStr = char + newStr
                pointer -= 1
            elif char == "(" and bracket == 1:
                newStr = char + newStr
                pointer -= 1
                break
            elif (char.isdigit()) or (not char.isdigit() and bracket != 0):
                newStr = char + newStr
                pointer -= 1
            else:
                break
        return [newStr, pointer+1, findex]
