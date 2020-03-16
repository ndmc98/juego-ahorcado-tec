# -*- coding: utf-8 -*-
''' 
Juego Ahorcado

Autores:
    Brayan Leonardo Sierra Forero # 20151020057
    Camilo Enrique Rocha Calderón # 20151020035
    Norbey Danilo Muñoz Cañón     # 20151020050

    Curso de Gestión Tecnológica
    
    16 Mar 2020
'''

# librerías utilizadas
import simpleguitk
import random

# variables globales
secret_words = ['conocimiento', 'social', 'internacional', 'patentes', 'estrategia'
                , 'registro', 'indeterminado', 'patentes', 'politica'
                , 'publico', 'economica', 'reivindicaciones', 'descriptiva']

questions = ['Que surge como la nueva divisa del poder en términos de una cultura empresarial que trabaja por la propiedad INTELECTUAL', 
             'Para que la propiedad intelectual siga cumpliendo una función ______ efi ciente, es necesario tener claro que el sistema está \nsoportado sobre principios que equilibran el interés particular del creador frente a los intereses SOCIALES', 
             'Los derechos exclusivos de la propiedad intelectual tienen un gran valor en el contexto de la competencia __________', 
             'En el año 2000 se da un hito histórico sobre la propiedad intelectual. Se conoce como el Tratado sobre el Derecho de ________ (PLT)', 
             'La ________ de protección de la propiedad intelectual es el conjunto de principios y políticas que implementa una organización para \napropiarse de los beneficios económicos derivados de sus esfuerzos de investigación y desarrollo', 
             'Los derechos de una patente de invención difiere de los derechos de un modelo de utilidad en cuanto a la duración y en la forma de \nprotección. el primero tiene una forma de protección de patente. Cual corresponde al segundo?', 
             'Los derechos de secretos industriales tienen una forma de protección: contrato de confidencialidad y una duración de plazo _________', 
             'La consideración de que los descubrimientos no son patentables, pues no constituyen una invención, es un fundamento esencial del sistema \nde __________', 
             'La titularidad de la propiedad intelectual debe definirse en una _______ en la que se establezca a quién pertenecerán los resultados de \ninvestigaciones financiadas por una empresa', 
             'Frecuentemente las patentes caen al dominio _______ al poco tiempo de haber sido concedidas por factores como ausencia de solicitudes \nnacionales, falta de explotación y omisión del pago de los derechos anuales', 
             'Según McDonough (1993), el propósito final del sistema de patentes es de naturaleza ____________. El sistema motiva a individuos y \norganizaciones a inventar, ante incentivos que son comercialmente atractivos', 
             'Las partes de la patente son: la información, un resumen, la memoria descriptiva, las figuras ilustrativas y las ____________', 
             'Las partes de la patente son: la información, un resumen, la memoria __________, las figuras ilustrativas y las reivindicaciones']

dictionary = dict(zip(secret_words, questions))

num_misses = 0
the_guess = 0
valid_characters = "abcdefghijklmnopqrstuvwxyz"
user_guesses = ""
the_mask = ""
que = ""

# usado para el ahorcado 
head = "Black"
body = "Black"
left_arm = "Black"
right_arm = "Black"
left_leg = "Black"
right_leg = "Black"
left_palm = "Black"
right_palm = "Black"
left_foot = "Black"
right_foot = "Black"

# usado para mostrar mensaje de victoria/derrota
you_won = "Black"
you_lost = "Black"
you_won_counter = 0
you_lost_counter = 0

# función de ayuda para iniciar el juego
def init():    
    global num_misses
    num_misses = 0
    
    global user_guesses
    user_guesses = ""
    
    global head, body, left_arm, right_arm, left_leg
    global right_leg, left_palm, right_palm, left_foot
    global right_foot, you_won, you_lost
    global you_won_counter, you_lost_counter
    
    head = "Black"
    body = "Black"
    left_arm = "Black"
    right_arm = "Black"
    left_leg = "Black"
    right_leg = "Black"
    left_palm = "Black"
    right_palm = "Black"
    left_foot = "Black"
    right_foot = "Black"
    you_won = "Black"
    you_lost = "Black"
    you_won_counter = 0
    you_lost_counter = 0
    
    # print consola
    # game banner
    print ("\n*** AHORCADO-TECNOLÓGICO ***")
    print ("Numero de errores: ", num_misses, "(6, tú pierdes)")
    
    # set de la palabra aleatoria 
    global the_guess    
    the_guess = random.randint(0, 12) # NUMERO DE PALABRAS!!!
    print_mask()
    
# función para ayudar a imprimir la líneas _
# imprime en pantalla el avance 
def print_mask():
    global the_mask
    global que
    the_mask = ""
    
    for x in range(0,len(secret_words[the_guess])):
        if(user_guesses.find(secret_words[the_guess][x]) >= 0):
           the_mask += " " + secret_words[the_guess][x] + " "
        else:
           the_mask += " _ "
    
    key = secret_words[the_guess]
    que = dictionary[key]
    print ("Palabra clave:", the_mask)
    print ("Pregunta-Pista (?):", que)
    
# función de ayud para revisar si usuario ganó
def user_has_won():
    user_won = True
    for x in range(0,len(secret_words[the_guess])):
        if(user_guesses.find(secret_words[the_guess][x]) < 0):
           user_won = False
    return user_won

# función de ayuda para dibujar al ahorcado
def draw_hangman():
    if(num_misses == 1):
        global head
        head = "Red"
    elif(num_misses == 2):
        global body
        body = "Red"
    elif(num_misses == 3):
        global left_arm
        left_arm = "Red"
        global left_palm
        left_palm = "Blue"
    elif(num_misses == 4):
        global right_arm
        right_arm = "Red"
        global right_palm
        right_palm = "Blue"
    elif(num_misses == 5):
        global left_leg
        left_leg = "Red"
        global left_foot
        left_foot = "Blue"
    else:
        global right_leg
        right_leg = "Red"
        global right_foot
        right_foot = "Blue"
        
# define los eventos de la interfaz
def get_input(guess):
    # limpia el textbox
    txtGuess.set_text("")
    
    global user_guesses
    global num_misses
    
    # hace cada entrada como letra minuscula (para evitar error)
    guess = guess.lower()
    
    '''Verifica si la entrada es valida'''
    
    # valida que ingresa solo un caracter
    if len(guess) != 1:
        print ("Por favor ingrese solo una letra")
        return None
    elif valid_characters.find(guess) < 0:
        print ("Por favor ingrese una letra valida (a-z)")
        return None
    elif user_guesses.find(guess) >= 0:
        print ("Ya adivinaste la letra " + guess + ". Por favor intenta con otra.")
        return None
    else:        
        # añadir letra a letras usadas
        user_guesses += guess
        
    # comentario en consola
    print ("Tu dijiste:", guess)
    print ("Numero de errores:", num_misses)
    
    # adivina
    if(secret_words[the_guess].find(guess) >= 0):
        print ("Bien!", "\n")
        print_mask()
        print ("")
    else:
        print ("Lo lamento! Intenta de nuevo!", "\n")
        print_mask()
        
        # update el  numero de errores
        num_misses += 1                      
        
        # dibuja una parte más del monacho
        draw_hangman()
        
        # Si no adivinaste
        if(num_misses >= 6 and not user_has_won()):
            print ("Perdón, perdiste!\nLa palabra a adivinar era: ", secret_words[the_guess])
            global you_lost_counter
            you_lost_counter = 5
            timerLost.start();
            return None
    
    if(user_has_won()):
        print ("Ganaste! Felicitaciones!!")
        global you_won_counter
        you_won_counter = 80
        timerWon.start();
              
# dibujar en canvas
def draw(canvas):
    canvas.draw_text("*** Ahorcado-Tecnológico ***", [50,112], 35, "Red")
    canvas.draw_text("Número de errores: " + str(num_misses) + " (6, tú pierdes)", [50,412], 24, "Red")
    canvas.draw_text("Palabra secreta: " + the_mask, [50, 372], 22, "Green")
    canvas.draw_text("Pregunta-Pista (?): " + que, [50, 520], 10, "Green")
    
    # DIBUJO
    
    canvas.draw_line((300, 150), (300, 325), 2, "Yellow")
    canvas.draw_line((275, 325), (325, 325), 2, "Yellow")
    canvas.draw_line((300, 150), (350, 150), 2, "Yellow")
    canvas.draw_line((350, 150), (350, 170), 2, "Yellow")
    
    canvas.draw_circle((350, 185), 16, 2, head)
    canvas.draw_line((350, 200), (350, 250), 2, body)
    canvas.draw_line((350, 200), (325, 225), 2, left_arm)
    canvas.draw_line((350, 200), (375, 225), 2, right_arm)
    canvas.draw_line((350, 250), (325, 280), 2, left_leg)
    canvas.draw_line((350, 250), (375, 280), 2, right_leg)
    canvas.draw_circle((325, 225), 4, 2, left_palm)
    canvas.draw_circle((375, 225), 4, 2, right_palm)
    canvas.draw_circle((325, 275), 4, 2, left_foot)
    canvas.draw_circle((375, 275), 4, 2, right_foot)
    
    # mensaje gana
    canvas.draw_text("FELICITACIONES, GANASTE!", [50,60], 42, you_won)
    
    # mensaje perdida
    canvas.draw_text("PERDÓN, PERDISTE!", [50,500], 52, you_lost)
    
# timer handler - cuando el usuario gana
def show_you_won():
    global you_won_counter, you_won
    you_won_counter -= 1
    if(you_won == "Black"):
        you_won = "White"
    else:
        you_won = "Black"
    
    if(you_won_counter <= 0):
        timerWon.stop()
        init() # inicia nuevo juego
        
# timer handler - cuando el usuario pierde
def show_you_lost():
    global you_lost_counter, you_lost
    you_lost_counter -= 1
    if(you_lost == "Black"):
        you_lost = "White"
    else:
        you_lost = "Black"
    
    if(you_lost_counter <= 0):
        timerLost.stop()
        init() # inicia nuevo juego
        
# frame
f = simpleguitk.create_frame("Hangman", 1000, 640)

# registro de eventos
txtGuess = f.add_input("Ingresa tu letra:", get_input, 200)
timerWon = simpleguitk.create_timer(100, show_you_won)
timerLost = simpleguitk.create_timer(1000, show_you_lost)
button = f.add_button("Nuevo juego", init)

f.set_draw_handler(draw)

# start frame
f.start()
# start game
init()

