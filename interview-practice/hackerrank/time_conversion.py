import os

def timeConversion(s):
    if s[-2:] == "AM":
        if s[:2] == "12":
            return "00" + s[2:-2]
        else:
            return s[:-2]
    else:
        new_hours = int(s[:2])
        new_hours += 12
        return str(new_hours) + s[2:]

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result + '\n')
