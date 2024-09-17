from random import choice # import the function choice from the module named random

# Play a game of rock-paper-scissors in Dutch

user = input("Kies een wapen (steen, papier of schaar): ")
comp = choice(["steen", "papier", "schaar"])

print("De gebruiker (jij) koos", user)
print("De computer (ik) koos", comp)

if user == comp: # user en computer kiezen hetzelfde, dus is het gelijkspel.
    print("Het is gelijkspel!")
elif (user == "steen" and comp == "papier") or (user == "papier" and comp == "schaar") or (user == "schaar" and comp == "steen"): #computer wint van user.
    print("Ik heb gewonnen!")
    print("Hopelijk heb je de volgende keer meer geluk...")
elif (user == "steen" and comp == "schaar") or (user == "papier" and comp == "steen") or (user == "schaar" and comp == "papier"): #user wint van computer.
    print("Jij hebt gewonnen!")
else: #als de user nonsense invoert, print dan een error.
    print("error, verkeerde invoer")