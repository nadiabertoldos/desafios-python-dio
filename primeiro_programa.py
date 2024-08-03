#Operadores de associação

#nome = "Nadia Bertoldo" 
#print ("nadia" in nome)

#-------------------------------------
#Estrutura de condição

#saldo = 1000
#saque = float(input("Informe o valor para saque: "))

#status = "Sucesso" if saque <= saldo else "Falha"

#print(f"{status} ao realizar o saque!")

#-------------------------------------
#Laços de repetição: for

# texto = input ("Informe um texto: ")
#VOGAIS = "AEIOU"

#for letra in texto:
#	if letra.upper() in VOGAIS:
#		print (letra, end="")

#print() # adiciona uma quebra de linha

#-------------------------------------
#Interpolação de string

#nome = "nadia"
#idade = 22
#prof = "medica"
#altura = 1.58

# %
#print ("Olá, meu nome é %s, tenho %d anos, sou %s e minha altura é %f" % (nome, idade, prof, altura))

# .format
#print ("Olá, meu nome é {}, tenho {} anos, sou {} e minha altura é {}" .format(nome, idade, prof, altura))
#print ("Olá, meu nome é {3}, tenho {0} anos, sou {1} e minha altura é {2}" .format(idade, prof, altura, nome))
#print ("Olá, meu nome é {name}, tenho {age} anos, sou {career} e minha altura é {height}" .format(name=nome, age=idade, career=prof, height=altura))
#print ("Olá, meu nome é {name}, tenho {age} anos, sou {career} e minha altura é {height}" .format(**pessoa))

#f-string
#print (f"Olá, meu nome é {nome}, tenho {idade} anos, sou {prof} e minha altura é {altura}")
#formatar string com f-string

#PI = 3.14159

#print(f"O valor de PI é: {PI: .2f}")
#>>> O valor de PI é:  3.14

#print(f"O valor de PI é: {PI: 10.3f}")
#>>> O valor de PI é:      3.142

#-------------------------------------
#Fatiamento de string

#nome = "Nadia Bertoldo Germano dos Santos"

#print(nome[0])
#N

#print(nome[-1])
#s

#print(nome[:9])
#Nadia Ber

#print(nome[10:])
#oldo Germano dos Santos

#print(nome[10:15])
#oldo 

#print(nome[10:16:2])
#od 

#print(nome[:])
#Nadia Bertoldo Germano dos Santos

#print(nome[::-1])
#sotnaS sod onamreG odlotreB aidaN

#-------------------------------------
#Funções

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    "Quinta-feira, 24 de Abril de 2024",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)