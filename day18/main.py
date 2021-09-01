import re
def camelCaseFour(s):
    if s[0] == "S":
        str = re.findall('[A-Z][A-Z]*', s[4:])
        return s[4:]
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

print(camelCaseFour("S;V;pictureFrame"))