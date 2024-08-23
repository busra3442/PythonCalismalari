agac_kati = int(input("Ağaç kaç katlı olsun?"))

for k in range(agac_kati):
    print(" "* (agac_kati-1-k), end=" ")
    print("*"* (k*2 + 1), end=" ")
    print()