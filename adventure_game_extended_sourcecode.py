import time
import sys


def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # new line at the end

def fast_print(text, delay=0.005):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # new line at the end


#Game variable library
senn_favor = 50

#Title screens

fast_print(r'''              , ----.
                              -  -     `
                        ,__.,'           \
                      .'                 *`
                     /       |   |     / **\
                    .                 / ****.
                    |    mm           | ****|
                     \                | ****|
                      ` ._______      \ ****/
                               \      /`---'
                                 \___(
                                 /~~~~\
                                /      \
                               /      | \
                              |       |  \
                    , ~~ .    |, ~~ . |  |\
                   ( |||| )   ( |||| )(,,,)`
                  ( |||||| )-( |||||| )    | ^
                  ( |||||| ) ( |||||| )    |'/
                  ( |||||| )-( |||||| )___,'-
                   ( |||| )   ( |||| )
                    ` ~~ '     ` ~~ '
''')
slow_print("made by mortified_penguin_projects...\n\n")
input("Press the enter key to continue... ")

fast_print('''
                           ___
                          ( ((
                           ) ))
  .::.                    / /(
 'M .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
(J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
 `P `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
  `::'                    \ \(
                           ) ))
                          (_(()
      '                )                  (                     )       (     
'      *   )  ( /(        (  (      )\ )  *   )   (    ( /(       )\ )  
'    ` )  /(  )\()) (     )\))(   '(()/(` )  /(   )\   )\()) (   (()/(  
'     ( )(_))((_)\  )\   ((_)()\ )  /(_))( )(_))(((_) ((_)\  )\   /(_)) 
'    (_(_())  _((_)((_)  _(())\_)()(_)) (_(_()) )\___  _((_)((_) (_))   
'    |_   _| | || || __| \ \((_)/ /|_ _||_   _|((/ __|| || || __|| _ \  
'      | |   | __ || _|   \ \/\/ /  | |   | |   | (__ | __ || _| |   /  
'      |_|   |_||_||___|   \_/\_/  |___|  |_|    \___||_||_||___||_|_\  \n\n''')
time.sleep(2)
slow_print("Press the enter key to continue...")
input()

#Game start

slow_print("Welcome to the world of witchers... You are a new recruit to the School of The Wolf...")
slow_print("You are walking up to Castle Kaer Morhen after your iniation. A witcher greets you at the door...\n")
time.sleep(2.5)
slow_print("SENN says: What's your name Witcher?...\n")
player_name = input("Type your name: ")
time.sleep (2)
slow_print(f"\nSENN says: Right... {player_name} huh?... Edran told me about you...\n")
time.sleep(1)
slow_print('''Listen... I know your new around here, but I need you to do something for me...\n
Your response:
1. What can I help you with Master?"
2. Sheesh... already? I just got here...
           
For responses, simply type '1' '2' '3' etc and then hit the enter key...''')
dialogue_senn_1 = input(f"Your response: ")
if dialogue_senn_1 == "1":
    time.sleep(1)
    slow_print("\nI like your attitude kid... ready to get your hands dirty...\nYou gained 5 favor points with SENN.")
    time.sleep(1)
    senn_favor += 5
elif dialogue_senn_1 == "2":
    time.sleep(1)
    slow_print("\n..... SENN stares at you...")
    time.sleep(2)
    slow_print("SENN speaks sharply: You make a great first impression... What is with these new recruits... We're just letting anyone in here nowadays...")
    senn_favor -= 20

slow_print(f"[Your current favor with SENN is {senn_favor}/100]")
time.sleep(1)
slow_print("\nSENN: Anyways, here's the situation...\nA few of our bladesmiths went into town to get supplies... but haven't come back. I'm thinking this is a good opportunity for you to get your feet wet...")
slow_print("Meet Edran by the stables... he'll get you set up with a horse.")
time.sleep(2)
slow_print('''\n\nYou walk to the stables and greet Edran...''')
time.sleep(1)
slow_print('''Your greeting:
1. Greetings Master Edran... I'm here for a horse. Duties from Senn.
2. Get me a horse ready damnit!''')

