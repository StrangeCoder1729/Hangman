import os





if os.path.isfile("result.txt"):
    import random
    try:
        user_name = input("Enter Your Name : ")
        with open('result.txt','a') as f:
            f.write(f"\nName of the Player : {user_name}\n")

        HANGMANPICS = ['''
         +---+
         |   |
             |
             |
             |
             |
        =========''', '''
         +---+
         |   |
         O   |
             |
             |
             |
        =========''', '''
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|\  |
             |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|\  |
        /    |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
        =========''']

        # lst_words = ['apple', 'samsung','nokia','blackberry','htc','Xaiomi','huwaie']
        lst_words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
                'coyote crow deer dog donkey duck eagle ferret fox frog goat '
                'goose hawk lion lizard llama mole monkey moose mouse mule newt '
                'otter owl panda parrot pigeon python rabbit ram rat raven '
                'rhino salmon seal shark sheep skunk sloth snake spider '
                'stork swan tiger toad trout turkey turtle weasel whale wolf '
                'wombat zebra ').split()

        

        # print(random.randint(0,len(lst_words)-1))
        words = lst_words[random.randint(0,len(lst_words)-1)]
        print(words)

        print(f"Clue : There are {len(words)} letters in the word")
        count = -1
        for letter in words:

            if count == 6:
                break
        
            letters = input("Enter the letter : ")
            letters = letters.lower()
        
            if letters == letter:
                # print("Outside while loop")
                print("Correct Letter !")
            
            

            elif letters != letter:
                count +=1
                print(f"Chance {count+1}")
                print(HANGMANPICS[count])

                
                while letters != letter:
                    if count == 6:
                        print("Game Over !!")
                        break
                    letters = input("Enter the letter : ") 
                    letters = letters.lower()
                    
    
                    if letters == letter:
                        print("Correct Letter !")
                    
                    elif letters != letter:
                        # print("its working")
                        count +=1
                        print(f"Chance {count+1}")
                        print(HANGMANPICS[count])
                        # print(count)
            
                
            
                
            
        
        if count < 6:
            print("\n")
            print("******************************************************||_Result_||****************************************************************")
            print(f"Congrats 😊 !!! You have won the game ")
            print(f"You took {count+1} chance(s) to get the right letter")    
            with open ("result.txt","a") as f:
                f.write(f'Chances taken : {count+1}\n\n')   

        else:
            # print(f"{count}")
            print("Ohh, you lost the the game")
            print("Dont lose hope, try again !!")
                
            with open ("result.txt",'a') as f:
                f.write(f'Chances taken : {count}\n\n')   
    except Exception as e:
        print("Invalid Input !!")

else:
    print('File got Created ..')
    print('Run the Program again !!')
    with open("result.txt",'wt') as f:
        f.write(f"                                                              {'Score Board'}                                                         ")




 