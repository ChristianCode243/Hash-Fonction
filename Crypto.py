# 
# Les fonctions basiques qui vont nous permettre de réaliser notre fonction de Hashage
# 

# Conversion d'une chaine de longueur N en binaire :
def texte_en_binaire(text_input):
    output = ''.join(format(ord(char), '08b') for char in text_input)
    return output


# Formalisation de la chaine en 32 bits
def pad_Binaire_texte(binaire_string):
    rema = len(binaire_string) % 32
    if rema != 0:
        padding_length = 32 - rema
        padded_string = '0' * padding_length + binaire_string
        return padded_string
    else:
        return binaire_string
    

# 
# Fonction de Hashage
# 
def Hasher(donnee, iv):

    # Convertir la chaine en binaire :
    texte_binaire = texte_en_binaire(donnee)
    # print("La chaine binaire de sortie est     : ", texte_binaire)

    # Formaliser la chaine en 32 bits
    chaine_en_32b = pad_Binaire_texte(texte_binaire)
    # print("La chaine formalisée en 32 bits est : ", chaine_en_32b)

    # Changer la représentation en Byte
    donnee_a_crypter = bytes(chaine_en_32b, 'utf-8')

    # Vérification de la taille des données pour le mode CBC
    if len(donnee_a_crypter) % 32 != 0:
        raise ValueError("La taille des données doit être un multiple de 32 pour respecter le mode CBC")

    # Chiffrement basé sur le AES en mode CBC
    text_hasher = b""
    block_precedant = iv
    
    # print("\n")

    for i in range(0, len(donnee_a_crypter), 32):

        # Division du block principal en sous-block de 32 bits
        block = donnee_a_crypter[i:i+32]
        
        # print("Block entré       : ", block)

        # Chiffrement du block
        block = bytes(b1 ^ b2 for b1, b2 in zip(block, block_precedant))
        
        # print("Iv utilisé        : ", iv)
        # print("Block chiffré     : ", block)
        # print("Longueur du block : ", len(block))

        # print("\n")

        # Itération et permutation sur les blocks
        iv = block
        block_crypter = block

        text_hasher = block_crypter
        block_precedant = block_crypter
        

    return text_hasher