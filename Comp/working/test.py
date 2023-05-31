from random import randint

f = open("/Users/alexandrtotskiy/Developer/Distributed-processing-systems/Comp/working/input.txt", 'w')
i = 0
while i < 500:
    n = randint(1000000, 2000000)
    k = randint(1, n)
    f.write(str(n) + " " + str(k) +"\n")
    i += 1
f.close()