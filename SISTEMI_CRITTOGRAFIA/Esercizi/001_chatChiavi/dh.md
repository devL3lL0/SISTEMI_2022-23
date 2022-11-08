# DIFFIE - HELLMAN 
1) ottengo numero random sia server che client
2) calcolo il modexp tra (g, a{Client}(b{Server}), P) = ga/gb
3) client invia il numero ottenuto al server => ga -> server
4) server riceve il numero e fa il modexp tra (gb, a, P)
5) il server invia gb -> client
6) il client fa il modexp (ga, b, P)
7) Dovrebbero stampare a schermo lo stesso numero