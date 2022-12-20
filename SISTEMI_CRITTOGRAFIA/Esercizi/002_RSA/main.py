from RSA import RSAPrivateKey

if __name__ == "__main__":
    m = int(input("inserisci m: "))
    e = int(input("inserisci e: "))
    k = RSAPrivateKey.SET_valori_input()
    n = k.p * k.q
    fi = (k.p-1) * (k.q-1)
    c = k.cifratura(m, n)
    print(f"Messaggio cifrato: {c}")
    e = k.e
    d = RSA.Equazione_Diofantea(e, fi, 1)


    # ED % PHI=1
    if (e*d) %fi == 1:
        print(f"Valori originari: {d}")
        if d[0] < 0:
            d_pos = d[0] + fi
        else:
            d_pos = d[0]
        print(d_pos)
        print(f"Chiave di decifratura: {d_pos}")
        m2 = RSA.decifratura(c, d_pos, n)
        print(f"Messaggio decifrato: {m2}")
