incorrectList = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

# correct = []
# for ind, name in enumerate(incorrectList):
#     correct.append(name.split(" "))
#     ind = +1
#
# for i in range(len(correct)):
#     print("Привет, " + correct[i][-1].title() + "!")

for i in incorrectList:
    print("Привет, " + i.split()[-1].title() + "!")


