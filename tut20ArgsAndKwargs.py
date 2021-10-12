def toprint(one, *aa, **kwargsb):
    for i in one:
        print(i)
    for i in aa:
        print(i)
    for i in kwargsb:
        print(i)

har=[1, 2, "hello buddy"]
har1=[ "Love the way you lie"]
toprint( har, *har1, **har1)