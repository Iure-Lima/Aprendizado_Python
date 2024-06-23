def titulo(msg):
    print("-=" * 15)
    print(msg)
    print("-=" * 15)


#titulo("     Curso em vídeo     ")
#titulo("     Aprenda Python     ")
#titulo("     Iure Lima     ")

def soma(a, b):
    print(a + b)


#soma(4, 5)
#soma(8, 9)
#soma(2, 1)

def contador(i, *num):
    print(i)
    for n in num:
        print(n)


contador(2, 4, 5, 6, 7, 7, 8, 9, 8, 7, 6, 5, 4)
