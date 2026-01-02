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
player_health = 100
player_gold = 20
senn_favor = 50
edran_favor = 50

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
slow_print('''Listen... I know you're new around here, but I need you to do something for me...\n
Your response:
1. What can I help you with Master?"
2. Sheesh... already? I just got here...
           
For responses, simply type '1' '2' '3' etc and then hit the enter key...\nYour response:\n''')
dialogue_senn_1 = input()
if dialogue_senn_1 == "1":
    time.sleep(1)
    slow_print("\nSENN replies warmly: I like your attitude kid... ready to get your hands dirty...")
    time.sleep(1)
    senn_favor += 5
elif dialogue_senn_1 == "2":
    time.sleep(1)
    slow_print("\n..... SENN stares at you...")
    time.sleep(2)
    slow_print("SENN speaks sharply: You make a great first impression... What is with these new recruits?... We're just letting anyone in here nowadays...")
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
2. Get me a horse ready damnit!\n''')
dialogue_edran_1 = input()

if dialogue_edran_1 == "1" and dialogue_senn_1 == "1":
    time.sleep(1)
    edran_favor += 20
    slow_print("\nEDRAN greets you warmly: Hey kid! I can get you setup right over here! And by the way... thanks for not giving SENN any lip... He's grumpy in the morning on occassion.")
elif dialogue_edran_1 == "1" and dialogue_senn_1 == "2":
    time.sleep(1)
    edran_favor += 10
    slow_print("\nEDRAN greets you warmly: Hey kid!... At least you're not giving me that attitude you gave to SENN...")
elif dialogue_edran_1 == "2" and dialogue_senn_1 == "1":
    time.sleep(1)
    edran_favor -= 20
    slow_print("\nEDRAN: What the hell kid...? You kiss SENN's ass and then talk to me like some peasant?... Do you know who I am kid?")
elif dialogue_edran_1 == "2" and dialogue_senn_1 == "2":
    time.sleep(1)
    edran_favor -= 30
    slow_print("\nEDRAN: Dear lord kid... giving both of your elders a hard time... you're gonna be a dream...")

slow_print(f"[Your favor with EDRAN is {edran_favor}/100]")
time.sleep(1)
if edran_favor >= 50:
    slow_print("EDRAN: Alright kid... Here's a horse ready for ya. Be sure to tip the stablemaster on the way out... and here's some coin for the road.")
    player_gold += 20
    slow_print(f"EDRAN hands you 20 pieces of gold.")
    slow_print(f"Your satchel has {player_gold} pieces of gold.")

elif edran_favor < 50:
    slow_print("EDRAN: The sooner you're gone, the better, kid... Here's a horse... Be sure to tip the stablemaster on the way out...")
    slow_print(f"Your satchel now has {player_gold} pieces of gold.")

time.sleep(2)
slow_print("\nYou mount up your horse and trot over to the stablemaster...")
time.sleep(1)