import re
def camelCaseFour(s):
    if s[0] == "S":
        if s[2] == "M":
            s = s[:-2]
        s = re.findall('.[^A-Z]*', s[4:])
        for i in range(len(s)):
            s[i] = s[i].lower()                        
        return " ".join(s)
    #     s.rstrip("()")
    #     if s[2] == "M":
    #         str[len(str)-1]
    #     lower_str = str.lower()
    #     return " ".join(lower_str)
    # elif s[0] == "C":
    #     str = s[4:].split()
    #     if s[2] == "M":
    #         for i in range(1, len(str)):
    #             str[i].capitalize()
    #         str.append("()")
    #     elif s[2] == "V":
    #         for i in range(1, len(str)):
    #             str[i].capitalize()
    #     elif s[2] == "C":
    #         str.title()
    #     return "".join(str)

print(camelCaseFour("S;M;pictureFrame()"))