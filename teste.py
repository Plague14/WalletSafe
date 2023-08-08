#-*- encoding: utf-8 -*-
from os import write
import random as rd
import json

"""def mdc(n1, n2):
    while(n2 != 0):
        r = n1 % n2
        n1 = n2
        n2 = r
    return n1

def gerar_chave_publica(n):
    while True:
        e = rd.randrange(2, n)
        if(mdc(n,e) == 1):
            return e
        
def gerar_chave_privada(totiente, e):
    d = 0
    while((d *e) % totiente != 1):
        d += 1
    return d

def cifrar(mensagem, e, n):
    msg_cifrada = ""
    #mensagem = bytes(mensagem)
    for letra in mensagem:
        k = (ord(letra) ** e) % n
        msg_cifrada += chr(k)
    return msg_cifrada

def decifrar(mensagem, n, d):
    msg_decifrada = ""
    for letra in mensagem:
        k = (ord(letra) ** d % n)
        msg_decifrada += chr(k)
    return msg_decifrada

def rsa():
    msg = "teste"
    p = 349#17
    q = 353#19
    n = p * q
    y = p - 1
    x = q - 1
    totiente = x * y
    while True:
        e = gerar_chave_publica(totiente)
        print(f"Chave publica: ({e},{n})")
        d = gerar_chave_privada(totiente, e)
        print(f"Chave privada: ({d},{n})")
        if e != d:
            break
    print(msg)
    msg = cifrar(msg, e, n)
    bytes_data = [112,52,52]
    now = "".join(map(chr,bytes_data))
    print(now)
    f = open('index.txt', 'w')
    f.write(msg)

    #print("MENSAGEM CIFRADA: " + bytes(msg,'latin1'))

    msg = decifrar(msg, n, d)
    print("MENSAGEM DECIFRADA: " + msg)

rsa()"""

with open('./index.json', "r", encoding="utf-8") as dados:
    load = json.load(dados)
    
print(load)