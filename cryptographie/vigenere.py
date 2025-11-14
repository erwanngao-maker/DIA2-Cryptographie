import cesar as cs

def chiffre_vigenere(message, key):
    # Initialisation variable index et resultat
    chars_result = [""] * len(message)
    message_index = 0
    # Parcour message
    
    while message_index < len(message):
        shift = ord(key[message_index%len(key)])
        chars_result[message_index] = cs.chiffre_cesar(message[message_index], shift)
        message_index+=1

    string_result="".join(chars_result)
    return string_result

def dechiffre_vigenere(message, key):
    # Initialisation variable index et resultat
    chars_result = [""] * len(message)
    message_index = 0
    # Parcour message
    
    while message_index < len(message):
        shift = ord(key[message_index%len(key)])
        chars_result[message_index] = cs.dechiffre_cesar(message[message_index], shift)
        message_index+=1

    string_result="".join(chars_result)
    return string_result
print(dechiffre_vigenere(chiffre_vigenere(",c-0é9204897';.","suu"), "suu"))
