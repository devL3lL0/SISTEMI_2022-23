class RSAPrivateKey:

    p: int
    q: int
    d: int
    e: int
    
    def __init__(self, p, q, e):
        self.p = p
        self.q = q
        self.e = e

    def SET_valori_input():
        p = int(input("inserisci p: "))
        q = int(input("inserisci q: "))
        k = RSA(p, q, e)
        return k

    def get_public_key():
    

    def modexp(e, x, n):
        acc = 1
        while e > 0:
            if e % 2 == 1:
                acc = (acc*x) % n
            x = (x*x) % n
            e = e // 2
        return acc

    def cifratura(m, n):
        #p = potenza(m,e)
        #c = p%n
        #c = (m**e)%n #funziona
        c = self.modexp(self.e, m, n) #LERDA
        return c

    def decifratura(c, d, n):
        #p = potenza(c,d)
        #m2 = p%n
        #m2 = (c**d)%n #funziona
        m2 = self.modexp(c, d, n) #LERDA
        return m2


def equazione_diofantea(e, fi, ris):
    q, r = divmod(e, fi)
    if r == 0:
        return([0, ris//fi])
    else:
        sol = equazione_diofantea(fi, r, ris)
        u = sol[0]
        primo_valore = sol[1]
    return([primo_valore, u - q * primo_valore])


    