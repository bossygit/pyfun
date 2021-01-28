print("Ca fait Tic Tac Toe")
print(" | | ")
print("-----")
print(" | | ")
print("-----")
print(" | | ")
def drawboard(place):
    cols = 5
    rows = 3
    for i in range(rows):
        index = 0
        for o in range(cols):
            if o%2 == 0:
                print("{}".format(place[i][index]),end='')
                index += 1
            if o%2 != 1 and o != cols-1:
                print('|',end='')
            if o == cols-1:
                print("")

        if i != rows-1:
            print("-----")
cc = [[" "," "," "],[" "," "," "],[" "," "," "]]
player = 1
jouer1 = ""
jouer2 = ""
while(True):
    if(player == 1):
        if jouer1 == "":
            jouer1 = input("Joueur 1 votre nom : ")
        print("{} joue".format(jouer1))
        ligne = int(input("Saisis ta ligne 1,2,3 : "))
        colonne = int(input("Saisis ta colonne 1,2,3 : "))
        cc[ligne-1][colonne-1] = "x"
        drawboard(cc)
        player = 2
        print(" Changement de jouer ... "+str(player))
    if(player == 2):
        if jouer2 == "":
            jouer2 = input("Joueur 2 votre nom : ")
        print("{} joue".format(jouer2))
        ligne = int(input("Saisis ta ligne 1,2,3 : "))
        colonne = int(input("Saisis ta colonne 1,2,3 : "))
        cc[ligne - 1][colonne - 1] = "o"
        drawboard(cc)
        player = 1
        print(" Changement de jouer ... " + str(player))
