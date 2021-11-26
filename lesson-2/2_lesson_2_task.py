listStr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

def textStr(list):
    result = ""
    for el in list:
        normalStr = el

        if el.isdecimal():
            normalStr = covichka(formatDec(el))

        if ('+' in el):
            substr = el.split('+', 1)[1]
            normalStr = covichka('+' + formatDec(substr))

        result = result + " " + normalStr

    return result

def formatDec(el):
    if (abs(int(el) * 0.1) < 1):
        num = '0' + el
    else:
        num = el
    return num

def covichka(el):
    return "\"" + el + '"'

print(textStr(listStr))





