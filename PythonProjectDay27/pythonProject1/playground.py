def calc(*args, summ=0, aver=0):  # data that i dont want to be changed need to be at the end
    for n in args:
        summ += n
        aver += 1
    return summ / aver


result = calc(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

print(result)


# This is ilso possible to get a dictionary as an input using **

def blah(**kwargs):
    print(kwargs)


blah(moshe=5, sean=10, egor=11)
