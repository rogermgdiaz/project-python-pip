import os
import random

def choose_options():
    options=('piedra','papel','tijeras')
    user_option=input('Elije entre piedra, papel o tijeras ==>  ').lower()
    computer_option= random.choice(options)
    return user_option, computer_option

def check_rules(user_option,computer_option):
    if user_option==computer_option:
        return 0
    elif (user_option=='piedra'and computer_option=='tijeras') or (user_option=='papel'and computer_option=='piedra')or(user_option=='tijeras'and computer_option=='papel'):
        return 1
    elif (computer_option=='piedra'and user_option=='tijeras') or (computer_option=='papel'and user_option=='piedra')or(computer_option=='tijeras'and user_option=='papel'):
        return 2

def winner(ruler):
    if ruler ==0:
        print("Es un empate")
    elif ruler == 1:
        print("Ganaste.")
    elif ruler == 2:
        print("La computadora gano.")
        
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title():
    print("""
    [ 🤖 Bienvenido al juego Piedra, Papel o tijera 🙋]
           _______
      ---'   ____)____
                _______)
                _______)
                _______)
      ---.___________.'
    """)


def runner():
    options=('piedra','papel','tijeras')
    looper=input('Desea jugar piedra, papel o tijeras?(y/n)==>  ').lower()
    
    round=1
    user_wins = 0
    computer_wins = 0
    while looper=="y":
        clear_screen()
        print_title()
        print(f"ROUND ==> {round}   |User wins ==> {user_wins}   |Computer wins ==> {computer_wins}")
        print('-'*50)
        user_option, computer_option=choose_options()
        if user_option not in options:           
            print("elije una opcion entre: 'piedra','papel','tijeras' " )
            continue
        print(f"Elegiste {user_option} y la computadora eligio {computer_option}")
        ruler=check_rules(user_option,computer_option)
        winner(ruler)
        if ruler == 0:
            pass
        elif ruler == 1:
            user_wins+=1
        elif ruler == 2:
            computer_wins+=1
        round+=1
        looper=input('Desea seguir jugando?(y/n)==>').lower()
    
runner()
        
        
    
        