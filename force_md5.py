from itertools import product
import hashlib

chars = [chr(i) for i in range(97, 123)]
chars += [chr(i) for i in range(65, 91)]
chars += [chr(i) for i in range(48, 58)]


chars1 = [chr(i) for i in range(97, 123)]
chars2 = [chr(i) for i in range(65, 91)]
chars3 = [chr(i) for i in range(48, 58)]

print(f'''
Esses são os caracteres usados:
{', '.join(chars1)}
{', '.join(chars2)}
{', '.join(chars3)}

''')


# Ou descomente a linha abaixo para incluir todos os caracteres geralmente usados em um password
# chars  += [chr(i) for i in range(32, 127)]

# password = '60aed9608a2e4acf1a70fd3d83069a7c'
# exemplo de hash MD5: 0fbad99b54653d68264ce51ae1fad0f8
tentativa = 0
password = input('Cole sua hash MD5: ')

def bruteForce_1(chars, password, lenPass):
    tentativa = 0

    for i in product(chars, repeat=lenPass):
        combina = ''.join(i)
        tentativa += 1
        bb = str.encode(combina)

        acha = hashlib.md5(bb).hexdigest()
        bb = bb.decode('utf-8')
        #print(acha)
        if tentativa % 500000 == 0:
            print('%10i --> %s' % (tentativa, combina))

        if password == acha:
            encontrada = 'Senha encontrada é "{}", após {} tentativas.'.format(combina, tentativa)
            print(encontrada)
            arquivo = open('senha.txt', 'w')
            arquivo.writelines(encontrada)
            arquivo.close()
            exit()


    return 'Senha NÃO encontrada'


# Estudar depois como funciona ele
def bruteForce_2(chars, password, lenPass, comb_anterior = ''):

    global tentativa

    for LETRA in chars:
        combina = comb_anterior + LETRA
        tentativa += 1
        if tentativa % 500000 == 0:
            print('%10i --> %s' % (tentativa, combina))

        if password == combina:
            print('Senha encontrada é "{}", após {} tentativas.'.format(combina, tentativa))
            #return 'ok'
            exit()

        elif lenPass != 1:
            # E aqui a chamada da recursividade
            bruteForce_2(chars, password, lenPass-1, combina)


for ttt in range(1, 11):
    print(f'senha de {ttt} caracters')
    print(bruteForce_1(chars, password, lenPass=ttt))
    print('*' * 60 + '\n')


#
# print(bruteForce_2(chars, password, len(password)))
# print('*' * 60 + '\n')


# print(bruteForce_2(chars, 'cabo', 4))
# print('*' * 60 + '\n')

# print(bruteForce_2(chars, 'cabo', 5))

# Fim
