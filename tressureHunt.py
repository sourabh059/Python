print('''     
               _.---._
             .'       `.
             :)       (:
             \ (@) (@) /
              \   A   /
               )     (
               \.""""/
                `._.'
                 .=.
         .---._.-.=.-._.---.
        / ':-(_.-: :-._)-:` \.
       / /' (__.-: :-.__) `\ \.
      / /  (___.-` '-.___)  \ \.
     / /   (___.-'^`-.___)   \ \.
    / /    (___.-'=`-.___)    \ \.
   / /     (____.'=`.____)     \ \.
  / /       (___.'=`.___)       \ \.
 (_.;       `---'.=.`---'       ;._)
 ;||        __  _.=._  __        ||;
 ;||       (  `.-.=.-.'  )       ||;
 ;||       \    `.=.'    /       ||;
 ;||        \    .=.    /        ||;
 ;||       .-`.`-._.-'.'-.       ||;
.:::\      ( ,): O O :(, )      /:::.
|||| `     / /'`--'--'`\ \     ' ||||
''''      / /           \ \      ''''
         / /             \ \.
        / /               \ \.
       / /                 \ \.
      / /                   \ \.
     / /                     \ \.
    /.'                       `.\.
   (_)'                       `(_)
    \ \.                       .//
     \ \.                     .//
      \ \.                   .//
       \ \.                 .//
        \ \.               .//
         \ \.             .//
          \ \.           .//
          / / /)         (\ \ \.
        ,///'           `\ \ \,
       ///'               `\ \ \.
      ""'                   '""
      ''')

print("welcome to tressure Island")
print("your mission is to find the tresure.")
choice1=input('you\'re at crossroad , where do you want to go ? Type "left" or "right".').lower()
if choice1 == "left":
    choice2= input('You\'ve come to a lake.there is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if choice2 == "wait":
        choice3=input("you arrived at the island Unharmed. There is house with 3 doors. one red ,one yellow and One blue.which colour do you choose?").lower()
        if(choice3== "red"):
           print("its room of fire. Game Over")
        elif(choice3=="yellow"):
            print("You enter room of Monster Game Over")
        elif(choice3=="blue"):
            print("You Won the Tressur,YOU WIN")
        else:
            print("You are to smart that's why game Over")
    else:
        print("You got attack by crocodile.GAME OVER")
else:
    print("YOu fell into Hole.\ngameOver")