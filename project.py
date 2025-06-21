import pygame
from keyboard import Keyboard
from Plugboard import Plugboard
from Rotor import Rotor
from Reflector import Reflect
from Enigma import Enigma
from draw import draw
#setup pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma simulator")
WIDTH=1600
HEIGHT=900
SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))
MARGINS={"top":200,"bottom":100,"left":100,"right":100}
GAP=100
INPUT=""
OUTPUT=""
PATH=[]
#create fonts
MONO=pygame.font.SysFont("FreeMono",25)
BOLD=pygame.font.SysFont("FreeMono",25,bold=True)


#Historical enigma componenets
I=Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II=Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III=Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV=Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V=Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A=Reflect("EJMZALYXVBWFCRQUONTSPIKHGD")
B=Reflect("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C=Reflect("FVPJIAOYEDRZXWGCTKUQSBNMHL")
#keyboard and plugboard
KB=Keyboard()
PB=Plugboard(["AB","CD","EF"])

#defining Enigma Machine
ENIGMA=Enigma(B,I,II,III,PB,KB)
ENIGMA.set_rings([1,1,1])
#set message key
ENIGMA.set_key("CAT")
""""
#Encipher message
message="TESTINGTESTINGTESTINGTESTING"
cipher_text=""
for letter in message:
    cipher_text=cipher_text+ENIGMA.encipher(letter)
print(cipher_text)
"""
animating=True
while animating:
    #bgcolor
    SCREEN.fill("#333333")
    draw(ENIGMA,PATH,SCREEN,WIDTH,HEIGHT,MARGINS,GAP,BOLD)
    #text input
    text=BOLD.render(INPUT,True,"White")
    text_box=text.get_rect(center=(WIDTH/2,MARGINS["top"]/3))
    SCREEN.blit(text,text_box)

    #text output
    text=MONO.render(OUTPUT,True,"White")
    text_box=text.get_rect(center=(WIDTH/2,MARGINS["top"]/3+25))
    SCREEN.blit(text,text_box)

    pygame.display.flip()
    #track user input
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            animating=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                II.rotate()
            elif event.key==pygame.K_SPACE:
                INPUT=INPUT +" "
                OUTPUT=OUTPUT+" "
            else:
                key=event.unicode
                if key in "abcdefghijklmnopqrstuvwxyz":
                    letter=key.upper()
                    INPUT=INPUT+letter
                    PATH,cipher=ENIGMA.encipher(letter)
                    print(PATH)
                    OUTPUT=OUTPUT+cipher









    
 