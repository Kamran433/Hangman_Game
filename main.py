# import random
# import hangman_stages
# import hangman_logo
# import hangman_words
# from replit import clear
# print(hangman_logo.logo)
# print("Welcome to the hangman game")
# j=input("Type 'YES' for playing: ").lower()
# if j=="yes":
#  chosen=random.choice(hangman_words.word_list)
#  c=len(chosen)
#  original=[]
#  a=0
#  lk=0
#  display=[]
#  letter=""
#  lives=6
#  z=lives-1
#  for lk in range(1,c+1):
#    display+="_"
#  for a in range(0,1):
#    original+=chosen
#  while "_" in display:
#    guess=input("guess the letter: ").lower()
#    clear()
#    if guess in display:
#      print(f"You already guessed {guess},try another alphabet")
#    for lt in range(c):
#       letter=chosen[lt]
#       if letter==guess:
#         display[lt]=letter
#    print(display)
#    if display==original:
#     print("you win.")
#     break
#    if guess not in chosen:
#     print(f"Your guessed alphabet {guess} is wrong.You have {z} lifes left.")
#     z-=1
#     print(hangman_stages.stages[lives])
#     lives-=1
   
#     if lives==0:
#      print("you lose.")
#      print(hangman_stages.stages[0])
#      print("your character died. Try again!")
#      print(f"The correct word was {original}")
#      print("Thank you for playing")
#      break
# else:
#   print("Thank You for visiting.")
