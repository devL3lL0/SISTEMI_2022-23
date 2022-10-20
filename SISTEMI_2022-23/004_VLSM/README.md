## ESERCIZIO COMPITO
### ROUTING e VLSM


192.168.5.0

5 sottoreti da 14, 28, 2, 7, 28

si parte dalla più grande


B♦per 28 host servono 5 bit

net1 = 192.168.5.0/27

broadcast1 = 192.166.5.31

subnet1 = 255.255.255.224


E♦per 28 host servono 5 bit

net2 = 192.168.5.32/27

broadcast2 = 192.168.5.63

subnet2 = 255.255.255.224


A♦per 14 host servono 4 bit

net3 = 192.168.5.64/28

broadcast3 = 192.168.5.79

subnet3 = 255.255.255.240


D♦per 7 host servono 4 bit

net3 = 192.168.5.80/28

broadcast3 = 192.168.5.95

subnet3 = 255.255.255.240


C♦per 2 host servono 2 bit

net3 = 192.168.5.96/30

broadcast3 = 192.168.0.99

subnet3 = 255.255.255.252