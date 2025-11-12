import string

def chiffre_cesar(message, shift):
    message = message.lower()
    # Initialisation du resultat
    chars_result = ['']* len(message)
    # Parcour du message
    for index in range(len(message)):
        # Application du decalage
        char_value = ord(message[index]) + shift
        # Recalage
        while (char_value > 1114111):
            char_value -= 1114111
        chars_result[index] = chr(char_value)
        
    # Recuperation du resultat sous forme de string
    string_result="".join(chars_result)
    return string_result

def dechiffre_cesar(message, shift):
    # Initialisation du resultat
    chars_result = ['']* len(message)
    # Parcour du message
    for index in range(len(message)):
        # Desapplication du decalage
        char_value = ord(message[index]) - shift
        # Recalage dans les caractere autorise entre 32 (SPACE) et 126 (TILDE)
        while (char_value < 0):
            char_value += 1114111
        chars_result[index] = chr(char_value)
        
    # Recuperation du resultat sous forme de string
    string_result="".join(chars_result)
    return string_result

def brute_force(message):
    for shift in range(1114111):
        print(dechiffre_cesar(message, shift))
#brute_force(chiffre_cesar("Oui bonsoir",3))