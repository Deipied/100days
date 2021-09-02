import re
import sys

def camelCaseFour(s):
    if s[0] == "S":
        if s[2] == "M":
            s = s[:-2]
        s = re.findall('.[^A-Z]*', s[4:])
        for i in range(len(s)):
            s[i] = s[i].lower()                        
        return " ".join(s)
    elif s[0] == "C":
        str = s[4:].split()
        if s[2] == "M":
            for i in range(1, len(str)):
                str[i] = str[i].capitalize()
            str.append("()")
        elif s[2] == "V":
            for i in range(1, len(str)):
                str[i] = str[i].capitalize()
        elif s[2] == "C":
            for i in range(0, len(str)):
                str[i] = str[i].capitalize()
        return "".join(str)


# if __name__ == '__main__':
    
#     input_data = sys.stdin.read()
#     input_list = list(map(str, input_data.rstrip().split("\n")))
    
#     for line in input_list:
#         print(camelCaseFour(line))

print(camelCaseFour("S;M;sweatTea()"))
print(camelCaseFour("S;V;epsonPrinter"))
print(camelCaseFour("C;M;santa claus"))
print(camelCaseFour("C;C;mirror"))