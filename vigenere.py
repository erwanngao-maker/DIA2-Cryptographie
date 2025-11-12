import cesar as cs

def chiffre_vigenere(message, key):
    # Initialisation variable index et resultat
    chars_result = [""] * len(message)
    message_index = 0
    key_index = 0
    # Parcour message
    while message_index < len(message):
        # Parcour de la key et du message simultanement
        while key_index < len(key) and message_index < len(message):
            shift = ord(key[key_index])
            chars_result[message_index] = cs.chiffre_cesar(message[message_index], shift)
            key_index+=1
            message_index+=1
        key_index=0

    string_result="".join(chars_result)
    return (str(string_result))

def dechiffre_vigenere(message, key):
    # Initialisation variable index et resultat
    chars_result = [""] * len(message)
    message_index = 0
    key_index = 0
    # Parcour message
    while message_index < len(message):
        # Parcour de la key et du message simultanement
        while key_index < len(key) and message_index < len(message):
            shift = ord(key[key_index])
            chars_result[message_index] = cs.dechiffre_cesar(message[message_index], shift)
            key_index+=1
            message_index+=1
        key_index=0

    string_result="".join(chars_result)
    return (str(string_result))
print(dechiffre_vigenere(chiffre_vigenere(",c-0é9204897';.","suu"), "suu"))
