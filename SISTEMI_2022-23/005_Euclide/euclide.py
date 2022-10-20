def prendiInput():
    running = True
    n1 = int(input("Inserire il primo numero: "))
    while running == True:
        n2 = int(input("Inserire il secondo numero: "))
        if n1 > n2:
            running = False
    return (n1, n2)

def calcolaMCD():
    pass
