import string

def chiffre_cesar(message, shift):
    return "".join([chr((ord(message[index])+shift)%1114112) for index in range(len(message))])

def dechiffre_cesar(message, shift):
    return "".join(chr((ord(message[index]) - shift)%1114111) for index in range(len(message)))

#Fonctionne pour les characters d'unicodes inferieur 'range'
def fast_brute_force(message,range):
    min = ord(message[0])
    for letter in message:
        if ord(letter)< min:
            min = ord(letter)
    for shift in range(min-range if min > range else 0,min):
        print(dechiffre_cesar(message,shift))


def brute_force(message, alphabet):
    for shift in range(0,1114112):
        possible_message = dechiffre_cesar(message,shift)
        if possible_message[0] in alphabet:
            print(possible_message)


fast_brute_force(chiffre_cesar("gao",3289748657),140)