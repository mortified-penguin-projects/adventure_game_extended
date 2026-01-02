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

print(r'''              , ----.
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

slow_print("Welcome to the world of witchers... You are a new recruit to the School of The Wolf...")
slow_print("You are walking up to Castle Kaer Morhen after your iniation. A witcher greets you at the door...\n")
time.sleep(2.5)
slow_print("SENN says: What's your name Witcher?...\n")
player_name = input("Type your name: ")
time.sleep (2)
slow_print(f"\nRight... {player_name} huh?... Edran told me about you...\n")