from os import close
#import bcrypt
import json
import random as rd

class User():
    
    cont = 0
    
    def __init__(self, usuario, email, senha):
        self.__id = User.contador + 1
        self.__usuario = usuario
        self.__email = email
        self.__senha = senha
        return self.__id,self.__usuario,self.__email,self.__senha
    
    def cadastro():
        usuario = input('Digite um novo usuario:\n')
        email = input('Digite um novo email:\n')
        senha = input('Digite uma nova senha:\n')
        confirm = input('Confirme a senha:\n')
        
        if senha == confirm:
            print('Cadastrado com sucesso!')
            
            menu()
        else:
            print('As senhas não coincidem')
            
    def login():
        usuario = input('Usuário: ')
        senha = input('Senha: ')    
      
def choice1():
    print('Digite [1] para Login')
    print('Digite [2] para Cadastrar uma nova conta')
    print('Digite [0] para Sair\n')
    opt = input('')
    if opt == 1:
        login()
    elif opt == 2:
        cadastro()
    else:
        exit()   

def arquivo():
    try:
        f = open('index.json')
        f.close()
        exists = True
    except:
        exists = False
    return exists

def reading():
    with open('index.json', "r", encoding="utf-8") as dados:
        content = json.load(dados)
    return content

def create(content, contentnow):
    data = content + contentnow
    with open('index.json', "w", encoding="utf-8") as dados:
        salvando = json.dump(data ,dados, indent=2, separators=(",", ": "), sort_keys=True)
        
def menu():
    print('Digite [1] para criar uma nova carteira')
    print('Digite [2] para consultar uma carteira existente')
    print('Digite [3] para excluir uma carteira')
    
    opt = input('')
    if opt == 1:
        createwallet()
    elif opt == 2:
        consultwallet()
    elif opt == 3:
        excluirwallet()
"""
def mdc(n1, n2):
    while(n2 != 0):
        r = n1 % n2
        n1 = n2
        n2 = r
    return n1

def create_public_key(n):
    while True:
        e = rd.randrange(2, n)
        if(mdc(n,e) == 1):
            return e

def create_private_key(totiente, e):
    d = 0
    while((d * e) % totiente != 1):
        d += 1
    return d
  
def encrypt(nome, phrase, e, n):
    newname = ""
    newphrase = ""
    
    for letra in nome:
        k = (ord(letra) ** e) % n
        newname += chr(k)
        
    for letra in phrase:
        k = (ord(letra) ** e) % n
        newphrase += chr(k)
        
    return [newname, newphrase]
    newname = bcrypt.hashpw(nome, bcrypt.gensalt())
    newphrase = bcrypt.hashpw(phrase, bcrypt.gensalt())
    
    return newname, newphrase

def decrypt(nome, phrase, n, d):
    right_name = ""
    right_phrase = ""
    for letra in nome:
        k = (ord(letra) ** d % n)
        right_name += chr(k)
    for letra in phrase:
        k = (ord(letra) ** d % n)
        right_phrase += chr(k)
    return [right_name, right_phrase]



def rsa(name, phrase):
    p = 17
    q = 19
    n = p * q
    y = p - 1
    x = q - 1
    totiente = x * y
    e = create_public_key(totiente)
    print(f"Chave publica: ({e},{n})")
    d = create_private_key(totiente, e)
    print(f"Chave privada: ({d},{n})")
    
    cypher = encrypt(name, phrase, e, n)
    print(f"Name cypher: {cypher[0]}")
    print(f"Phrase cypher: {cypher[1]}")
    namecypher = encrypt(name, e, n)
    print(f"Name cypher: {namecypher}")
    phrasecypher = encrypt(phrase, e, n)
    print(f"Phrase cypher: {phrasecypher}")
    
    decypher = decrypt(name, phrase, n, d)
    print(f"Name Decypher: {decypher[0]}")
    print(f"Phrase Decypher: {decypher[1]}")
    namedecypher = decrypt(name, n, d)
    print(f"Name Decypher: {namedecypher}")
    phrasedecypher = decrypt(phrase, n, d)
    print(f"Phrase Decypher: {phrasedecypher}") 
    #return name, phrase

def decypher(name, phrase):
    rsa(name, phrase) """
    
    
def createwallet():
    nomewallet = input('Digite o nome da wallet:\n')
    phrase = input('Cole sua passphrase:\n')
    walletJSON = {nomewallet: phrase}
    try:
        f = open('./index.json')
        f.close()
        exists = True
    except:
        exists = False
    
    if exists == True:
        with open('./index.json', "r", encoding="utf-8") as dados:
            load = json.load(dados)
            arrWallet = [load, walletJSON]
            dados.close()
        with open('./index.json', "w", encoding="utf-8") as dados:
            json.dump(arrWallet ,dados, indent=2, separators=(",", ": "), sort_keys=True)
            dados.close() 
    else:    
        with open('./index.json', "w", encoding="utf-8") as dados:
            json.dump(walletJSON ,dados, indent=2, separators=(",", ": "), sort_keys=True)
            dados.close()
    
    print(f'Cadastrado com sucesso! seu nome está como: {nomewallet} e sua Phrase está como: {phrase}')

def consultwallet():
    pass

def excluirwallet():
    pass

"""
name = 'brave'.encode('UTF-8')
phrase = 'inner-you-company-nation-exist-base-eight-pact-vanish-weapon-slam-member'.encode('UTF-8')
rsa(name, phrase)

# phrase original = inner you company nation exist base eight pact vanish weapon slam member
# "company" do company da chave
if exists == True:
        
    else:
        
def arquivo(data):
    try:
        f = open('index.json')
        f.close()
        exists = True
    except:
        exists = False
        
    if exists == True:
        with open('index.json', "w", encoding="utf-8") as dados:
            salvando = json.dump(data ,dados, indent=2, separators=(",", ": "), sort_keys=True)
    else:
        with open('index.json', "w", encoding="utf-8") as dados:
            salvando = json.dump(data ,dados, indent=2, separators=(",", ": "), sort_keys=True)
        
reading()        
choice1() """
