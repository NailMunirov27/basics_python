import random
proudct_list = []
i = 0

while i < 20:
    proudct_list.append("{0:.2f}".format(random.uniform(10.0, 100.0)))
    i += 1

RubKopList = []
for ind, price in enumerate(proudct_list):
    if ind <= len(proudct_list):
        RubKopList.append(str(price.split(".")[0]) + " руб " + str(price.split(".")[1])+ " коп")
    ind = +1
print(", ".join(RubKopList))

print(sorted(proudct_list))

print(sorted(proudct_list, reverse=True))

print(sorted(proudct_list[:5], reverse=True))



