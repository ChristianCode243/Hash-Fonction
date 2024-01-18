from Crypto import *

iv = b'1b14c45d98cea45c1b14c45d98cea45c'

mdp = ""
verify = b""

print("-------------------------------------------------------------------------")
print("|                    TEST DE HASHAGE DE MOT DE PASSE                    |")
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")

mdp = input("Saisissez un nouveau mot de passe : ")

mdpSH = Hasher(mdp, iv)

# print("Le mot de passe hashé : ", mdpSH)
# print("Sa longueur est de    : ",len(mdpSH))
# print("\n")

while verify != mdpSH:

    mdp = input("Ressaisissez votre mot de passe : ")
    print("--- Quitter : CTL+C")

    verify = Hasher(mdp, iv)
    

print("-----------------------------------------------------")
print("|>>>>>>         MOT DE PASSE VALIDE !         <<<<<<|")
print("-----------------------------------------------------")