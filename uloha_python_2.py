#uloha 1
'''
from random import *
meno = input('Ako sa voláš?')
print('Ahoj '+meno+' rád Ťa spoznávam :)')
roknarodenia = input(meno+', v ktorom roku si sa narodil?')
meno2 = choice(('Alena', 'Barbora', 'Eva', 'Sofia'))
print('Á spomínam si, v roku '+roknarodenia+' sa narodila aj '+meno2)
print('Tvoj vek je ',2022-int(roknarodenia),' rokov.')
'''

#uloha3
'''
meno = input('Zadaj svoje meno: ')
vek = int(input('Kolko mas rokov? '))
print('Ahoj ',meno,' do dovŕšenia 100 rokov ti chýba ',100-vek)
'''

#uloha4
'''
meno = input('Zadaj svoje meno: ')
print('***********')
print('*         *')
print('* ',meno,' *')
print('*         *')
print('***********')
'''

#uloha5
'''
meno1 = input('Zadaj meno: ')
meno2 = input('Zadaj meno: ')
retazec = ''
pocet = len(meno1)+len(meno2)
for i in range(pocet):
    if i % 2 == 0:
        retazec += meno1[i//2]
    else:
        retazec += meno2[i//2]
print(retazec)
'''

#uloha6
'''
retazec = input('Zadaj retazec: ')
meno1 = ''
meno2 = ''
for i in range(len(retazec)):
    if i % 2 == 0:
        meno1 += retazec[i]
    else:
        meno2 += retazec[i]
print(meno1)
print(meno2)
'''

#uloha7

#uloha8
'''
veta = input("Zadaj vetu:")
n = len(veta)

for i in range(n):
    
    if veta[i] == ".":
        print("Oznamovacia veta")
    elif veta[i] == "?":
        print("Opytovacia veta")
    elif veta[i] == "!":
        print("Rozkazovacia veta")
'''

#uloha9
'''
import tkinter
import random
canvas = tkinter.Canvas(bg = "white")
canvas.pack()

def vypisovanie():
    canvas.delete("all")
    slovo = entry1.get()
    x = 20
    y = 20
    for i in range(len(slovo)):
        farba = random.choice(("red","green","blue","yellow","black","purple","orange"))
        canvas.create_text(x,y,text = slovo[i],font = "Arial 10 bold", fill=farba)
        x = x+15        

button1 = tkinter.Button(text='píš', command = vypisovanie)
button1.pack()


entry1 = tkinter.Entry()
entry1.pack()
'''

#uloha10
'''
import tkinter
import random
canvas = tkinter.Canvas(bg = "white")
canvas.pack()
'''
#a)
'''
def vypisovanie():
    canvas.delete("all")
    slovo = entry1.get()
    x = 20
    y = 20
    for i in range(len(slovo)):
        if i % 2 == 0:
            canvas.create_text(x,y-10,text = slovo[i],font = "Arial 10 bold")
        else:
            canvas.create_text(x,y+10,text = slovo[i],font = "Arial 10 bold")
            
        x = x+15
'''

#b)
'''
def vypisovanie():
    canvas.delete("all")
    slovo = entry1.get()
    x = 20
    y = 20
    uhol = 0
    for i in range(len(slovo)):
        canvas.create_text(x,y,text = slovo[i],font = "Arial 10 bold", angle = uhol)
        uhol = uhol + (360/(len(slovo)-1))       
        x = x+15     
'''

#c)
'''
def vypisovanie():
    canvas.delete("all")
    slovo = entry1.get()
    x = 20
    y = 20
    for i in range(len(slovo)):
        if i % 2 == 0:
            canvas.create_text(x,y,text = slovo[i],font = "Arial 10 bold", fill = "blue")
        else:
            canvas.create_text(x,y,text = slovo[i],font = "Arial 10 bold", fill = "red")   
        x = x+15
'''
        
#d)
'''
def vypisovanie():
    canvas.delete("all")
    slovo = entry1.get()
    x = 20
    y = 20
    for i in range(len(slovo)):
        if i % 2 == 0:
            canvas.create_text(x,y,text = slovo[i],font = "Arial 10 bold")
        else:
            canvas.create_text(x,y,text = slovo[i],font = "Arial 10 bold", angle = 180)
        x = x+15    
'''
'''
button1 = tkinter.Button(text='píš', command = vypisovanie)
button1.pack()
entry1 = tkinter.Entry()
entry1.pack()
'''

#uloha11
'''
import tkinter
canvas = tkinter.Canvas()
canvas.pack()


def text():
    canvas.delete("all")
    global x,y
    slovo = entry.get()+" "
    x = 10
    y = 100
    for i in range(len(slovo)):
        canvas.create_text(x,y, text = slovo[i], font = "Arial 20 bold", fill = "blue", tags = "st")
        x = x + 30
        canvas.after(1000)
        canvas.update()
    canvas.delete("st")
    canvas.after(3000,text)
    


button = tkinter.Button(text = "OK",command = text)
button.pack()

entry = tkinter.Entry()
entry.pack()
'''

#uloha12
'''
veta = input("Napíš vetu a ukonči ju bodkov:")
p=0
poradie = 0
j = ''
slovo = ''
for i in veta:
    if i == ' ' or i=='.':
        p+=1
        if len(slovo) > len(j):
            print(slovo)
            j = slovo
            poradie = p
        slovo = ''
    else:
        slovo += i

print('Počet slov vo vete je:', p)
print(len(j),' ',poradie)
print(j)
'''

#uloha13
'''
import tkinter
canvas = tkinter.Canvas(height = 100, width = 100)
canvas.pack()

def posun():
    canvas.delete("all")
    global slovo
    slovo = entry1.get()
    x = 10
    y = 10
    for i in range(len(slovo)):
        canvas.create_text(x,y, text = slovo[i])
        x = x + 10
        y = y + 10

button1 = tkinter.Button(text = "Potvrď", command = posun)
button1.pack()

entry1 = tkinter.Entry()
entry1.pack()
'''

#uloha14
'''
retazec = input('Zadaj retazec: ')
meno1 = retazec[::2]
meno2 = retazec[1::2]
print(meno1)
print(meno2)
'''

#uloha15
'''
s = input('Zadaj slovo: ')
for i in range(len(s)):
    ns = '.'*(len(s)-i)+s[:i+1]
    print(ns)
'''

#uloha16
'''
s = input('Zadaj slovo: ')
s1 = s[::-1]
for i in range(len(s)):
    ns = '.'*(len(s)-i)+s1[len(s)-i-1:]+s[:i+1]+'.'*(len(s)-i)
    print(ns)
'''

#uloha17
'''
email = input("Zadajte email:")
poc = 0
for i in range(len(email)):
    if email[i] == ".":
        poc = poc + 1


for j in range(len(email)):
    if (email[j] == ".") and (poc == 1):
        print("TLD:", email[j:])
        dom1 = email[j+1:]
    elif email[j] == ".":
        poc = poc - 1
    if email[j] == "@":
        print("Server:", email[j+1:])
        print("User:", email[:j])

print("Domény:")
print("Doména 1. úrovne je: ",dom1)

z = 0
pb = 0
for k in range(len(email)):
    if (email[k] == "@"):
        z = 1
    if (z == 1) and (email[k] == "."):
        pb += 1

if pb == 2:
    z = 0
    p = pb
    dom2 = " "
    for l in range(len(email)):
        if (email[l] == "@"):
            z = 1

        if (z == 1) and (email[l] == "."):
            pb = pb -1

        if (pb == 1) and not (email[l] == "."):
            dom2 = dom2 + email[l]
            
        if (email[l] == ".") and (pb + p == p):
            print("Doména 2. úrovne je:", dom2)
    pb = 0
    z = 0
    dom3 = " "
    x = 0
    for m in range(len(email)):
        if (z == 1) and not (email[m] == "."):
            dom3 = dom3 + email[m]
        
        if (email[m] == "@"):
            z = 1
            pb = pb + 1
        
        if (email[m] == ".") and (pb == 1):
            print("Doména 3. úrovne je:", dom3)
            x = x + 1
        if x == 1:
            pb = 2

elif pb == 1:
    z = 0
    p = pb
    dom2 = " "
    for l in range(len(email)):
        if (z == 1) and not (email[l] == "."):
            dom2 = dom2 + email[l]
        
        if (email[l] == "@"):
            z = 1
            pb = pb - 1

        if (email[l] == ".") and (pb + p == p):
            print("Doména 2. úrovne je:", dom2)    
'''

#uloha18
'''
rc = input("Napíš rodné číslo:")
r = rc[0:2]
m = rc[2:4]
d = rc[4:6]

if int(m) > 12:
    m = int(m) - 50
    poh = "Žena"
else:
    poh = "Muž"
    

if int(r) > 21:
    datum = d+" ."+str(m)+" ."+"19"+r
else:
    datum = d+" ."+m+" ."+"20"+r
 
print("Rodné číslo:", rc)
print("Dátum narodenia:", datum)
print("Pohlavie:", poh)

'''

#uloha19
'''
url = input("Zadaj URL adresu:")


for i in range(len(url)):
    if url[i] == ":":
        print(url[0:i])
    
p = " "
poc = 0
p_bod = 0
for j in range(len(url)):
    if url[j] == "/":
        poc = poc + 1

    if (url[j] == "/") and (poc == 3):
        print(p)

    if (poc == 2) and not (url[j] == "/"):
        p = p + url[j]

    if (poc == 2) and (url[j] == "."):
        p_bod = p_bod + 1
 
dn = " "
poc_b = 0
for k in range(len(url)):
    if url[k] == ".":
        poc_b = poc_b + 1
        
    if (url[k] == "/") and (poc_b == p_bod):
        print(dn)

    if (poc_b == p_bod) and not (url[k] == "."):
        dn = dn + url[k]
'''

#uloha21
from random import *
heslo = " "
for i in range(8):
    x = randrange(97, 122)
    heslo = heslo + chr(x)

#uloha22
'''
from random import *
heslo = " "
for i in range(8):
    x = randrange(97, 122)
    heslo = heslo + chr(x)

print(heslo)

pismeno = randrange(len(heslo))
for i in range(len(heslo)):
    if i == pismeno:
        pis = chr(ord(heslo[i])-32)
        nove_heslo = heslo[:i] + pis + heslo[i+1:]
        
print(nove_heslo)
'''

#uloha23
'''
pismeno =" "
p = 97
for i in range(26):
    if p < 122:
        pismeno = pismeno + chr(p) + ","
    else:
        pismeno = pismeno + chr(p)
        
    p += 1

print(pismeno)
'''

#uloha24
'''
cislo = " "
cislo2 = " "
c = 48
for i in range(10):
    if i < 9:
        cislo = cislo + chr(c) + ","
    else:
        cislo = cislo + chr(c)
    c += 1

for i in range(10):
    if i < 9:
        cislo2 = cislo2 + str(i) + ","
    else:
        cislo2 = cislo2 + str(i)
    
    

print(cislo)
print(cislo2)
'''

#uloha25
'''
vstup = input('Zadaj text:')
sifra = ''
for znak in vstup:
    novyznak = znak
    if 'a' <= znak <= 'x':
        novyznak = chr(ord(znak)+2)
    if znak == 'z':
        novyznak = 'b'
    if znak == 'y':
        novyznak = 'a'    
    sifra = sifra+novyznak
print(sifra)
sifra = ''
for znak in vstup:
    novyznak = znak
    if 'a' <= znak <= 'w':
        novyznak = chr(ord(znak)+3)
    if znak == 'z':
        novyznak = 'c'
    if znak == 'y':
        novyznak = 'b'
    if znak == 'x':
        novyznak = 'a'        
    sifra = sifra+novyznak
print(sifra)
'''

#uloha26
'''
vstup = input('Zadaj text:')
sifra = ''
d_sifra = " "
for znak in vstup:
    novyznak = znak
    if 'a' <= znak <= 'y':
        novyznak = chr(ord(znak)+1)
    if znak == 'z':
        novyznak = 'a'
    sifra = sifra+novyznak

print(sifra)


for znak in sifra:
    novyznak = znak
    if 'a' <= znak <= 'y':
        novyznak = chr(ord(znak)-1)
    if znak == 'a':
        novyznak = 'z'
    d_sifra = d_sifra+novyznak

print(d_sifra)    
'''

#uloha27
#posun o 2
'''
vstup = input('Zadaj text:')
sifra = ''
for znak in vstup:
    novyznak = znak
    if 'a' <= znak <= 'x':
        novyznak = chr(ord(znak)+2)
    if znak == 'z':
        novyznak = 'b'
    if znak == 'y':
        novyznak = 'a'    
    sifra = sifra+novyznak
    
print(sifra)

d_sifra = ""
for znak in sifra:
    novyznak = znak
    if 'a' <= znak <= 'x':
        novyznak = chr(ord(znak)-2)
    if znak == 'b':
        novyznak = 'z'
    if znak == 'a':
        novyznak = 'y'    
    d_sifra = d_sifra+novyznak
    
print(d_sifra)
'''
#posun o 3
'''
vstup = input('Zadaj text:')
sifra = ''
for znak in vstup:
    novyznak = znak
    if 'a' <= znak <= 'w':
        novyznak = chr(ord(znak)+3)
    if znak == 'z':
        novyznak = 'c'
    if znak == 'y':
        novyznak = 'b'
    if znak == 'x':
        novyznak = 'a'        
    sifra = sifra+novyznak
    
print(sifra)

d_sifra = ""
for znak in sifra:
    novyznak = znak
    if 'a' <= znak <= 'w':
        novyznak = chr(ord(znak)-3)
    if znak == 'c':
        novyznak = 'z'
    if znak == 'b':
        novyznak = 'y'
    if znak == 'a':
        novyznak = 'x'    
    d_sifra = d_sifra+novyznak
    
print(d_sifra)
'''

#uloha29 a 30
'''
from random import*
s = input('Zadaj retazec: ')
p = input('Zadaj pocet nahodnych zmiesani: ')
s1 = s
for j in range(int(p)):
    novy = ''
    s = s1
    for i in range(len(s)):
        ktory = randrange(len(s))
        print('Odstranujem znak', s[ktory])
        novy = novy+s[ktory]
        print('Zatial som vytvoril:', novy)
        s = s[:ktory] + s[ktory+1:]
        print('Este ostali tieto znaky:', s)
    print('                                  Zmiesane slovo: ', novy)
'''       





  






    
    






        
    


    





        
        
        
        