print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

turn1 = input("Alright bud take your first turn, Left or Right? Choose wisely...\n").lower()

if turn1 == "left":
    print("Good choice, you turn left and find an ominous kiddie pool.")

    turn2 = input("What do you do, Swim or Wait?\n").lower()

    if turn2 == "wait":
        print("You wait a while... after a few minutes a truck rolls up pulling a tiny house with multiple entrances")
        door = input("The driver of the truck rolls down their window and tells you to pick a door, which do you choose? Red, Blue, Yellow or the Passenger Door of the truck?").lower()

        if door == "red":
            print('''
               (  .      )
         )           (              )
               .  '   .   '  .  '  .
      (    , )       (.   )  (   ',    )
       .' ) ( . )    ,  ( ,     )   ( .
    ). , ( .   (  ) ( , ')  .' (  ,    )
   (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^''')
            print("Welp, wasn't expecting that to be on fire. You died GG")

        elif door == "blue":
            print('''
            / \__
 (    @\___
 /         O
/   (_____/
/_____/ U
''')
            print("Duncan is in here! He licks your face, his breath kills you. Game over.")

        elif door == "yellow":
            print("You open the door... out pops a genie! Wait no, it's just a homeless man.\nHe comes over to you and whispers in your ear... congratulations, you win, you get to take me home with you!!!\n\n\n Wait, you thought there would be treasure in here?")

        elif door == "passenger door" or door == "passenger" or door == "passenger door of truck" or door == "passenger door of the truck":
            print("I did not expect you to actually pick this, it has nothing to do with the mini house that was pulled up.\nYou hop in the car, both you and the driver speed off into the sunset, still game over though")
        else:
            print("Game over, do you need help reading the directions?")
    else:
        print('''
      ><(((('> ''')
        print("You were eaten by a goldfish. It was surprisingly aggressive!")


else:
    print("Game Over! Why would you turn right? Can you not read the sign?")
    print('''
         ________________________________
        /                                \
       /   DO NOT ENTER!!!               \
      /__________________________________\
      |                                  |
      | The all Mighty Bonnie Bell lives |
      |              here                |
      |__________________________________|
             ||               ||
             ||               ||
             ||               ||
             ||               ||
            /__\             /__\
           /____\           /____\
          //    \\         //    \\
         ||      ||       ||      ||
         ||      ||       ||      ||
         ||      ||       ||      ||
         ||      ||       ||      ||
         ||      ||       ||      ||
        (__)    (__)     (__)    (__)
''')