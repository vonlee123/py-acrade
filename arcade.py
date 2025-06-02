import random
import sys
#Rock paper Scissors
def program_stopper(max_interactions):
    counter = 0
    while True:
        if counter >= max_interactions:
            break
        counter+=1
def get_int_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            # Try to convert the input to an integer
            user_int = int(user_input)
            return user_int
        except ValueError:
            # If a ValueError is raised, it means the input was not a valid integer
            print("Invalid input. Please enter an integer.")
def get_str_input(prompt):
    while True:
        user_input = input(prompt)
        # Check if the input is a string that does not contain only digits
        if user_input.isdigit():
            print("Invalid input. Please enter a string that does not consist solely of digits.")
        else:
            return user_input
def rock_paper_scissors():
    Tie_score = 0
    Player_score = 0
    Computer_score = 0
    player_name = input("\nWelcome to Rock Paper Scissors, what is your name? ")
    times_played = int(get_int_input("\n" + player_name + ", how many times would you like to play? "))
    for i in range(times_played):
        Player_input = get_str_input("\nRock, Paper, or Scissors: ")
        Player_input = Player_input.upper()
        attempts = 0
        while attempts == 0:
            if Player_input == "ROCK":
                Player_input = 1
                attempts+=1
            elif Player_input == "PAPER":
                Player_input = 2
                attempts+=1
            elif Player_input ==  "SCISSORS":
                Player_input = 3
                attempts+=1
            else:
                Player_input = input("\nTry again: ")
                Player_input = Player_input.upper()
        Player_turn = False
        AI_turn = True
        AI_input = random.randint(1,3)
        if AI_input == 1:
            AI_rock = "Rock"
            print("\nThe Computer picked: " + AI_rock)
        elif AI_input == 2:
            AI_paper = "Paper"
            print("\nThe Computer picked: " + AI_paper)
        else:
            AI_scissors = "Scissors"
            print("\nThe Computer picked: " + AI_scissors)
        AI_Turn = False
        if (AI_input == 1 and Player_input == 1) or (AI_input == 2 and Player_input == 2) or (AI_input == 3 and Player_input == 3):
            print("\nThis round is a tie")
            Tie_score += 1
        elif (AI_input == 1 and Player_input == 3) or (AI_input == 2 and Player_input == 1) or (AI_input == 3 and Player_input == 2):
            print("\nThe computer wins this round")
            Computer_score += 1
        else:
            print("\n" + player_name + " wins this round")
            Player_score+=1
    if Computer_score == 0:
        print("\nThe computer won no rounds\n")
    elif Computer_score == 1:
        print("\nThe computer won " + str(Computer_score) + " round\n")
    else:
        print("\nThe computer won " + str(Computer_score) + " rounds\n")
    if Player_score == 0:
        print(player_name + " won no rounds\n")
    elif Player_score== 1:
        print(player_name + " won " + str(Player_score) + " round\n")
    else:
        print(player_name + " won " + str(Player_score) + " rounds\n")
    if Tie_score == 0:
        print("There were no ties")
    elif Tie_score == 1:
        print("There was " + str(Tie_score) + " tied round")
    else:
        print("There were " + str(Tie_score) + " tied rounds")
    program_stopper(0)

#Number Guesser
def NumberGuesser():
    Guesser_name = input("\nWelcome to NumberGuesser, What is your name: ")
    Min_num_range = get_int_input("\nHello " + Guesser_name + ", you lowest guessable number must be between 0 - 100, what number do you choose: ")
    while int(Min_num_range) > 100 or int(Min_num_range) < 0:
        Max_num_range = get_int_input("Please Enter a number: ")
    Max_num_range = get_int_input("\nThe highest guessable number must be between 150 - 500, what number do you choose: ")
    while int(Max_num_range) < 150 or int(Max_num_range) > 500:
        Max_num_range = get_int_input("\nChoose another number from 150 - 500: ")
    print("\nThe guessable range you set is from " + str(Min_num_range) + " - " + str(Max_num_range))
    Rand_num = random.randint(int(Min_num_range),int(Max_num_range))
#determines guess ranges based off of the size of the guessing range
#Highest range
    if (int(Max_num_range)-int(Min_num_range)) >= 400:
        Top_tier_diff =  random.randint(17,20)
        print("\nYou get " + str(Top_tier_diff) + " guesses to get the number")
        Num_of_guesses = 0
        for i in range(Top_tier_diff):
            guess = get_int_input("\nEnter your guess: ")
            if int(guess) > (Rand_num):
                Num_of_guesses+=1
                if int(guess) > (Rand_num + 200):
                    print("That's way too high!")
                elif int(guess) > (Rand_num + 100) and int(guess) <= (Rand_num + 200):
                    print("That's too high!")
                elif int(guess) > (Rand_num + 50) and int(guess) <= (Rand_num + 100):
                    print("That's slightly higher!")
                elif int(guess) > Rand_num and int(guess) <= (Rand_num + 50):
                    print("Lower!")
            elif int(guess) < (Rand_num):
                Num_of_guesses+=1
                if int(guess) < (Rand_num - 200):
                    print("That's way too low!")
                elif int(guess) < (Rand_num - 100) and int(guess) >= (Rand_num - 200):
                    print("That's too low!")
                elif int(guess) < (Rand_num - 50) and int(guess) >= (Rand_num - 100):
                    print("That's slightly lower!")
                elif int(guess) < Rand_num and int(guess) >= (Rand_num - 50):
                    print("Higher!")  
            elif int(guess) == (Rand_num):
                Num_of_guesses+=1
                print("Congratulations you guessed " + str(Rand_num) + " after " + str(Num_of_guesses) + " guesses!")
                break
        if (int(guess)!=Rand_num):
            print("\n" + Guesser_name + " you did not find the number " + str(Rand_num) + " after " + str(Num_of_guesses) + " guesses") 
#Middle tier range
    elif (int(Max_num_range)-int(Min_num_range)) < 400 and (int(Max_num_range)-int(Min_num_range)) >= 250:
        Mid_tier_diff = random.randint(12,16)
        print("You get " + str(Mid_tier_diff) + " guesses to get the number")
        Num_of_guesses = 0
        for i in range(Mid_tier_diff):
            guess = get_int_input("\nEnter your guess: ")
            if int(guess) > (Rand_num):
                Num_of_guesses+=1
                if int(guess) > (Rand_num + 150):
                    print("That's way too high!")
                elif int(guess) > (Rand_num + 75) and int(guess) <= (Rand_num + 150):
                    print("That's too high!")
                elif int(guess) > (Rand_num + 25) and int(guess) <= (Rand_num + 75):
                    print("That's slightly higher!")
                elif int(guess) > Rand_num and int(guess) <= (Rand_num + 25):
                    print("Lower!")
            elif int(guess) < (Rand_num):
                Num_of_guesses+=1
                if int(guess) < (Rand_num - 150):
                    print("That's way too low!")
                elif int(guess) < (Rand_num - 75) and int(guess) >= (Rand_num - 150):
                    print("That's too low!")
                elif int(guess) < (Rand_num - 25) and int(guess) >= (Rand_num - 75):
                    print("That's slightly lower!")
                elif int(guess) < Rand_num and int(guess) >= (Rand_num - 25):
                    print("Higher!")
            elif int(guess) == (Rand_num):
                Num_of_guesses+=1
                print("Congratulations you guessed " + str(Rand_num) + " after " + str(Num_of_guesses) + " guesses!")
                break
        if (int(guess)!=Rand_num):
            print("\n" + Guesser_name + " you did not find the number " + str(Rand_num) + " after " + str(Num_of_guesses) + " guesses")
#Low range
    elif (int(Max_num_range)-int(Min_num_range)) < 250 and (int(Max_num_range)-int(Min_num_range)) >= 100:
        Low_tier_diff =  random.randint(6,11)
        print("You get " + str(Low_tier_diff) + " guesses to get the number")
        Num_of_guesses = 0
        for i in range(Low_tier_diff):
            guess = get_int_input("\nEnter your guess: ")
            if int(guess) > (Rand_num):
                Num_of_guesses+=1
                if int(guess) > (Rand_num + 100):
                    print("That's way too high!")
                elif int(guess) > (Rand_num + 50) and int(guess) <= (Rand_num + 100):
                    print("That's too high!")
                elif int(guess) > (Rand_num + 25) and int(guess) <= (Rand_num + 50):
                    print("That's slightly higher!")
                elif int(guess) > Rand_num and int(guess) <= (Rand_num + 25):
                    print("Lower!")
            elif int(guess) < (Rand_num):
                Num_of_guesses+=1
                if int(guess) < (Rand_num - 100):
                    print("That's way too low!")
                elif int(guess) < (Rand_num - 50) and int(guess) >= (Rand_num - 100):
                    print("That's too low!")
                elif int(guess) < (Rand_num - 25) and int(guess) >= (Rand_num - 50):
                    print("That's slightly lower!")
                elif int(guess) < Rand_num and int(guess) >= (Rand_num - 25):
                    print("Higher!")
            elif int(guess) == (Rand_num):
                Num_of_guesses+=1
                print("Congratulations you guessed " + str(Rand_num) + " after " + str(Num_of_guesses) + " guesses!")
                break
        if (int(guess)!=Rand_num):
            print("\n" + Guesser_name + " you did not find the number " + str(Rand_num) + " after " + str(Num_of_guesses) + " guesses")
#minimum range
    elif (int(Max_num_range)-int(Min_num_range)) < 100:
        Minimum_tier_diff =  random.randint(2,5)
        print("You get " + str(Minimum_tier_diff) + " guesses to get the number")
        Num_of_guesses = 0
        for i in range(Minimum_tier_diff):
            guess = get_int_input("\nEnter your guess: ")
            if int(guess) > (Rand_num):
                Num_of_guesses+=1
                if int(guess) > (Rand_num + 75):
                    print("That's way too high!")
                elif int(guess) > (Rand_num + 35) and int(guess) <= (Rand_num + 75):
                    print("That's too high!")
                elif int(guess) > (Rand_num + 15) and int(guess) <= (Rand_num + 35):
                    print("That's slightly higher!")
                elif int(guess) > Rand_num and int(guess) <= (Rand_num + 15):
                    print("Lower!")
            elif int(guess) < (Rand_num):
                Num_of_guesses+=1
                if int(guess) < (Rand_num - 75):
                    print("That's way too low!")
                elif int(guess) < (Rand_num - 35) and int(guess) >= (Rand_num - 75):
                    print("That's too low!")
                elif int(guess) < (Rand_num - 15) and int(guess) >= (Rand_num - 35):
                    print("That's slightly lower!")
                elif int(guess) < Rand_num and int(guess) >= (Rand_num - 15):
                    print("Higher!")
            elif int(guess) == (Rand_num):
                Num_of_guesses+=1
                print("Congratulations you guessed " + str(Rand_num) + " after " + str(Num_of_guesses) + " guesses!")
                break
        if (int(guess)!=Rand_num):
            print("\n" + Guesser_name + " you did not find the number " + str(Rand_num) + " after " + str(Num_of_guesses) + " guesses")
    program_stopper(0)

#Murder Mystery
def Murder_mystery():
    Ta_player = input("\nWelcome to Murder Mystery, what is your name: ")
    Adventure_choice = "MURDER MYSTERY"
    Ta_plays = 0
    while Ta_plays == 0:
        if Adventure_choice == "MURDER MYSTERY":
            Ta_plays+=1
            print("\n" + Ta_player + ", welcome to the Murder Mystery")
            #possible names for victim, business rival, and employee
            M_mens_names = ["Laroon Langmiter", "John Hindleshroom", "Jonny Cox", "Bartholemew Jimone jr", "Fraun Nukiljeb", "Horace Zuckermust", "Owen Helfuvumoocktll" , "Laung'ehtood Aull", "Bushee Naudbouji", "Flurd Witchamum", "Isnod Omplicated", "Staur Uks", "Eigh Miecelfenyu", "Wuzen'eve Allat", "Skerin Hozeh", "Iyel Laydur", "Meindif Shoeyusum", "Stuap Stayrell", "Jum'pon Bousin", "Bill Ywonbirgir"]
            #victime name
            M_victim_name = random.choice(M_mens_names)
            M_mens_names.remove(M_victim_name)
            #business rival name
            M_business_rival_name = random.choice(M_mens_names)
            M_mens_names.remove(M_business_rival_name)
            #Employee name
            M_employee_name = random.choice(M_mens_names)
            M_mens_names.remove(M_employee_name)
            #Family Friend name
            M_family_friend_name = random.choice(M_mens_names)
            #re-adding removed names
            M_mens_names.append(M_victim_name)
            M_mens_names.append(M_business_rival_name)
            M_mens_names.append(M_employee_name)
            #wife and assistant possible names
            M_womens_names = ["Treesha Lagpipe", "Tiffany barlathamoth", "Jonia Coahx", "Sharqueesha Morthon III", "Leesha Leesha", "Loe'ahna Ayeg", "Shiza Pensovian", "Puleiza Kwiez", "Kharda Clyne", "Dragupenna Epps"]
            #wife name
            M_wife_name = random.choice(M_womens_names)
            M_womens_names.remove(M_wife_name)
            #assitant name
            M_assistant_name = random.choice(M_womens_names)
            #re-adding removed name
            M_womens_names.append(M_wife_name)
            #uppercase name lists
            M_upper_mens_names = []
            M_upper_womens_names = []
            for i in M_mens_names:
                M_upper_mens_names.append(i.upper())
            for k in M_womens_names:
                M_upper_womens_names.append(k.upper())
        
            Murder_mystery_game = 0
            if Murder_mystery_game == 0:
                murderer = M_employee_name
                print("\nThere has been a murder in a grand mansion.\nThe victim is a man named " + M_victim_name + ", he is a businessman\nThere are five possible suspects to this murder:")
                #wife's description
                print("The first suspect is " + M_wife_name + ". She is the victims wife and is known for her elegance and grace")
                #business rival's description
                print("The next suspect is " + M_business_rival_name + ". He has been a business rival of the victim for many years")
                #personal assistant description
                print("The next suspect is " + M_assistant_name + ". She is the victims loyal assitant who knows all of his secrets")
                #Family frind description
                print("The next suspect is " + M_family_friend_name + ". He is a close family frind to the victim and has known him for years")
                #Employee description
                print("The final suspect is " + M_employee_name + ". He is a former employee of charles who was wornfully terminated")
                print("\nYou get three guesses to solve this murder.\nYou can learn more about every suspect one time.\nYou get three interrogations, but can only interrogate a suspect once\nYou also have two hints, a max of one per suspect and one including mutiple suspects, but for every hint you loose a guess")
                #capitalizes the murderer so they can be compared to the guess
                Upper_murderer = murderer.upper()
                for murderer in M_mens_names:
                    if Upper_murderer in M_upper_mens_names:
                        pass
                #makes a list with all of the available incorrect names to be compared to answers
                M_upper_wife_name = M_wife_name.upper()
                M_upper_business_rival_name = M_business_rival_name.upper()
                M_upper_assistant_name = M_assistant_name.upper()
                M_upper_family_friend_name = M_family_friend_name.upper()
                M_upper_employee_name = M_employee_name.upper()
                M_upper_suspects = [M_upper_wife_name, M_upper_business_rival_name, M_upper_assistant_name, M_upper_family_friend_name]

                #lists for more information of each suspect
                learnmore_wife = [M_wife_name + " is charming but has a potentially cold and calculating side", M_wife_name + " was a star child actor winning numerous awards, but was also involved in numerous scandals"]
                learnmore_business_rival = [M_business_rival_name + " is known for his ruthless business tactics, and his relationship with " + M_victim_name + " was strictly proffesional but highly competitive", M_victim_name + " just backed out of a deal with " + M_business_rival_name + " and " + M_business_rival_name + " has built up a reputation for holding grudges aginst those who cross him"]
                learnmore_assistant = [M_assistant_name + " is often mistreated and overworked while working for " + M_victim_name, M_assistant_name + " had a troubled past, including financial difficulties and a stint in rehab"]
                learnmore_family_friend = [M_family_friend_name + " is a widowed man who is very close with " + M_wife_name, M_family_friend_name + " had a long illustrious career of solving high-profile cases until he eventually mishandled evidence in the case of " + M_victim_name]
                learnmore_employee = [M_employee_name + " has a history of her tumultouos relationships and is known for her passionate and sometimes erratic behavior ", M_victim_name + " alledgedly stole one of " + M_employee_name + "'s paintings and sold it for a large sum of money, leaving " + M_employee_name + " out of the profit"]

                learn_about_wife = 0
                learn_about_business_rival = 0
                learn_about_assitant = 0
                learn_about_family_friend = 0
                learn_about_employee = 0

                #lists for hints on multiple suspects
                mult_suspect_hints = ["A sketchbook from " + M_employee_name + "'s studio had notes in " + M_family_friend_name + "s handwriting, detailing " + M_victim_name + "'s schedule and movements", "Surveillance video shows " + M_wife_name + " and " + M_business_rival_name + " leaving " + M_victim_name + "'s office seperately on the night of the murder, " + M_wife_name + " leaving shortly before " + M_business_rival_name + " arrived", M_assistant_name + " as " + M_victim_name + "'s assistant had access to sensative information " + M_family_friend_name + " may have needed. There are phone records showing numerous calls between " + M_family_friend_name + " and " + M_assistant_name + " leading up to the time of the murder"]
                #lists for hints on specidic suspects
                wife_hints = [M_wife_name + " was overheard threatening " + M_victim_name + ", saying 'You'll regret ever crossing me!'", "A peice of fabric was found matching the clothes" + M_wife_name + " was wearing on the day of the murder", M_wife_name + "'s phone records show a series of frantic calls to her publicist extrmely shortly after the time of the murder"]
                business_rival_hints = ["Financial records reveal that " + M_business_rival_name + " would gain significantly from " + M_victim_name + "'s death", M_business_rival_name + "'s fingerprints were found on glass in " + M_victim_name  + "'s office, despite the fact he said he had not been there for three weeks", M_business_rival_name + " had an extremely heated argument just a few days before the murder"]
                assistant_hints = [M_assistant_name + "'s handwriting was found on a threatening note addressed to " + M_victim_name + ", discovered on his desk", "Security footage showed " + M_assistant_name + " entering " + M_victim_name + "'s office multiple times on the day of the murder, even though " + M_assistant_name + "claimed to be running errands", "A large sum of money was recently deposited into " + M_assistant_name + "'s account from an unknown source"]
                family_friend_hints = [M_family_friend_name + "'s old case files contained detailed information about " + M_victim_name + ", includng a pshycological profile", M_family_friend_name + " was spotted at the at " + M_victim_name + "'s mansion on the night of the murder, despite his claims of being at his country house", "A retired police badge was spotted at the crime scene, similar to the one " + M_family_friend_name + " carried during his career"]
                employee_hints = ["A recent gallery exhibit featured a painting by " + M_employee_name + " closely resembled the crime scene", "Traces of paint matching those used by " + M_employee_name + " were spotted under the victims fingernails", M_employee_name + " had been seen with a new expensive peice of jewelry recently"]


                num_of_hints = 0
                hint_about_wife = 0
                hint_about_business_rival = 0
                hint_about_assistant = 0
                hint_about_family_friend = 0
                hint_about_employee = 0
                hints_about_mult_suspects = 0

                #interrogation lines for each suspect
                A_Interrogation_wife = ["I was at a charity event at the community center. There were many people there who can confirm my presence, including the event organizers", "I was at home, in the library, reading a book. Our housekeeper saw me around 8:30 PM when she brought me some tea"]
                B_Interrogation_wife = ["Yes, we had been arguing a lot recently about finances. I discovered he was spending money we didn't have, and it was putting a lot of strain on our relationship", "We had a minor disagreement about his late working hours, but nothing serious. We usually resolved our issues quickly"]
                A_Interrogation_business_rival = ["We had a heated discussion about a business deal. He undercut me on a major contract, and I was upset. But that doesn't mean I wanted him dead", "It was about a property deal we were both interested in. He got the upper hand, and I was frustrated. But it was just business; nothing personal"]
                B_Interrogation_business_rival = ["I was at a business conference in another city. You can check the hotel records and the conference attendance list to verify that I was there", "I was having dinner with a client at a restaurant downtown. The client and the restaurant staff can confirm I was there"]
                A_Interrogation_assistant = ["I was working late at the house, finishing up some reports. I didn't see anything unusual, but I did hear some strange noises coming from outside around 9 PM", "I was organizing files and preparing for a meeting the next day. I noticed the security cameras had been turned off, which was odd"]
                B_Interrogation_assistant = ["We had a professional disagreement recently. I was up for a promotion, but he gave it to someone else. I was disappointed, but I wouldn't kill him over it", "He was a demanding boss, but we didn't have any major conflicts. Our relationship was strictly professional"]
                A_Interrogation_family_friend = ["I noticed that the lights in the victim's study were on late. That was unusual because he usually turned in early. I thought it was odd but didn't think much of it at the time", "I saw someone lurking near the back entrance of the house around 9 PM. It seemed suspicious, but I couldn't make out who it was"]
                B_Interrogation_family_friend = ["I was helping my neighbor with an urgent plumbing issue. She can vouch for me; we were fixing her kitchen sink until almost midnight", "I was at home, reviewing some old case files. My wife can confirm I was there the entire evening"]
                A_Interrogation_employee = ["I was closing up the office and then went to a social gathering with friends. I didn't see anyone suspicious, but I did notice that the victim's office door was slightly ajar when I left", "I stayed late to finish some paperwork. I saw a figure in a dark coat leaving the building in a hurry around 9:30 PM"]
                B_Interrogation_employee = ["I felt undervalued and overlooked at work. I had been there for years, but he never seemed to notice my efforts. It was frustrating, but I would never hurt him", "We had a disagreement over a project assignment last week, but it was resolved. I respected him as a boss"]
                num_of_interrogations = 0
                num_of_interrogations_wife = 0
                num_of_interrogations_business_rival = 0
                num_of_interrogations_assistant = 0
                num_of_interrogations_family_friend = 0
                num_of_interrogations_employee = 0

                murder_guesses = 0
                while murder_guesses < 3:
                    M_guess_yn = get_str_input("\nWould you like to guess who the murderer is: ")
                    M_guess_yn = M_guess_yn.upper()
                    if M_guess_yn == "YES":
                        M_guess = get_str_input("\nWho do you think the murderer is: ")
                        M_guess = M_guess.upper()
                        if M_guess == Upper_murderer:
                            murder_guesses+=1
                            if murder_guesses > 1:
                                print("Congratulations " + Ta_player + " you correctly guessed " + M_employee_name + " as the murderer after " + str(murder_guesses) + " guesses!")
                                break
                            else:
                                print("Congratulations " + Ta_player + " you correctly guessed " + M_employee_name + " as the murderer after " + str(murder_guesses) + " guess!")
                                break 
                        elif (M_guess == M_upper_wife_name) or (M_guess == M_upper_business_rival_name) or (M_guess == M_upper_assistant_name) or (M_guess == M_upper_family_friend_name):
                                if M_guess in M_upper_suspects:
                                    print("That is incorrect")
                                    murder_guesses+=1
                                    if M_guess == M_upper_wife_name:
                                        M_upper_suspects.remove(M_upper_wife_name)
                                    elif M_guess == M_upper_business_rival_name:
                                        M_upper_suspects.remove(M_upper_business_rival_name)
                                    elif M_guess == M_upper_assistant_name:
                                        M_upper_suspects.remove(M_upper_assistant_name)
                                    elif M_guess == M_upper_family_friend_name:
                                        M_upper_suspects.remove(M_upper_family_friend_name)
                                else:
                                    Lower_guess = M_guess.lower()
                                    print("You already guessed " + Lower_guess)
                                    continue
                        else:
                            print("Thats not one of the possible suspects")
                    elif M_guess_yn == "NO":
                        learnmore_interrogate_hint = get_str_input("Would you like to 'learn more' about a suspect, 'interrogate' the suspect, or receive a 'hint': ")
                        learnmore_interrogate_hint = learnmore_interrogate_hint.upper()
                        if learnmore_interrogate_hint == "LEARN MORE":
                            who_learnmore = get_str_input("Would you like to learn more about " + M_wife_name + ", " + M_business_rival_name + ", " + M_assistant_name + ", " + M_family_friend_name + ", or " + M_employee_name + ": ")
                            who_learnmore = who_learnmore.upper()
                            if who_learnmore == M_upper_wife_name and learn_about_wife == 0:
                                which_learnmore_wife = random.randint(0,1)
                                print(learnmore_wife[which_learnmore_wife])
                                learn_about_wife+=1
                            elif who_learnmore == M_upper_business_rival_name and learn_about_business_rival == 0:
                                which_learnmore_business_rival = random.randint(0,1)
                                print(learnmore_business_rival[which_learnmore_business_rival])
                                learn_about_business_rival+=1
                            elif who_learnmore == M_upper_assistant_name and learn_about_assitant == 0:
                                which_learnmore_assitant = random.randint(0,1)
                                print(learnmore_assistant[which_learnmore_assitant])
                                learn_about_assitant+=1
                            elif who_learnmore == M_upper_family_friend_name and learn_about_family_friend == 0:
                                which_learnmore_family_friend = random.randint(0,1)
                                print(learnmore_family_friend[which_learnmore_family_friend])
                                learn_about_family_friend+=1
                            elif who_learnmore == M_upper_employee_name and learn_about_employee == 0:
                                which_learnmore_employee = random.randint(0,1)
                                print(learnmore_employee[which_learnmore_employee])
                                learn_about_employee+=1
                            elif who_learnmore == M_upper_wife_name and learn_about_wife == 1:
                                print("You have already learned about " + M_wife_name)
                            elif who_learnmore == M_upper_business_rival_name and learn_about_business_rival == 1:
                                print("You have already learned about " + M_business_rival_name)
                            elif who_learnmore == M_upper_assistant_name and learn_about_assitant == 1:
                                print("You have already learned about " + M_assistant_name)
                            elif who_learnmore == M_upper_family_friend_name and learn_about_family_friend == 1:
                                print("You have already learned about " + M_family_friend_name)
                            elif who_learnmore == M_upper_employee_name and learn_about_employee == 1:
                                print("You have already learned about " + M_employee_name)
                            else:
                                print("That's not one of the possible suspects")
                        
                        elif learnmore_interrogate_hint == "HINT" and murder_guesses == 2 and num_of_hints < 2:
                                print("Why would you use your last guess on a hint?")
                        elif learnmore_interrogate_hint == "HINT" and murder_guesses == 2 and num_of_hints == 2:
                                print("Your out of hints")
                        elif learnmore_interrogate_hint == "HINT" and murder_guesses < 3 and num_of_hints < 2:
                            which_hint = get_str_input("Do you want a more specific hint on an 'individual' or a broader hint including 'mulitple suspects': ")
                            which_hint = which_hint.upper()
                            if which_hint == "INDIVIDUAL" and num_of_hints < 2 and murder_guesses < 2:
                                Which_suspect_hint = get_str_input("Would you like a hint on " + M_wife_name + ", " + M_business_rival_name + ", " + M_assistant_name + ", " + M_family_friend_name + ", or " + M_employee_name + ": ")
                                Which_suspect_hint = Which_suspect_hint.upper()
                                if Which_suspect_hint == M_upper_wife_name and hint_about_wife < 1:
                                    which_hint_wife = random.randint(0,2)
                                    print(wife_hints.pop(which_hint_wife))
                                    num_of_hints+=1
                                    murder_guesses+=1
                                    hint_about_wife+=1
                                elif Which_suspect_hint == M_upper_business_rival_name and hint_about_business_rival < 1:
                                    which_hint_business_rival = random.randint(0,2)
                                    print(business_rival_hints.pop(which_hint_business_rival))
                                    num_of_hints+=1
                                    murder_guesses+=1
                                    hint_about_business_rival+=1
                                elif Which_suspect_hint == M_upper_assistant_name and hint_about_assistant < 1:
                                    which_hint_assistant = random.randint(0,2)
                                    print(assistant_hints.pop(which_hint_assistant))
                                    num_of_hints+=1
                                    murder_guesses+=1
                                    hint_about_assistant+=1
                                elif Which_suspect_hint == M_upper_family_friend_name and hint_about_family_friend < 1:
                                    which_hint_family_friend = random.randint(0,2)
                                    print(family_friend_hints.pop(which_hint_family_friend))
                                    num_of_hints+=1
                                    murder_guesses+=1
                                    hint_about_family_friend+=1
                                elif Which_suspect_hint == M_upper_employee_name and hint_about_employee < 1:
                                    which_hint_employee = random.randint(0,2)
                                    print(employee_hints.pop(which_hint_employee))
                                    num_of_hints+=1
                                    murder_guesses+=1
                                    hint_about_employee+=1
                                elif Which_suspect_hint == M_upper_wife_name and hint_about_wife == 1:
                                    print("You have already gotten a hint about " + M_wife_name)
                                elif Which_suspect_hint == M_upper_business_rival_name and hint_about_business_rival == 1:
                                    print("You have already gotten a hint about " + M_business_rival_name)
                                elif Which_suspect_hint == M_upper_assistant_name and hint_about_assistant == 1:
                                    print("You have already gotten a hint about " + M_assistant_name)
                                elif Which_suspect_hint == M_upper_family_friend_name and hint_about_family_friend == 1:
                                    print("You have already gotten a hint about " + M_family_friend_name)
                                elif Which_suspect_hint == M_upper_employee_name and hint_about_employee == 1:
                                    print("You have already gotten a hint about " + M_employee_name)
                                else:
                                    print("That's not one of the possible suspects")
                            elif which_hint == "MULTIPLE SUSPECTS" and num_of_hints < 2 and hints_about_mult_suspects < 1:
                                which_hint_mult_suspects = random.randint(0,2)
                                print(mult_suspect_hints.pop(which_hint_mult_suspects))
                                num_of_hints+=1
                                murder_guesses+=1
                                hints_about_mult_suspects+=1
                            elif which_hint == "MULTIPLE SUSPECTS" and num_of_hints < 2 and hints_about_mult_suspects == 1:
                                print("You already got a guess about multiple suspects")
                            else:
                                print("Enter whether you want an 'individual' hint or a hint including 'multiple suspects'")
                        elif learnmore_interrogate_hint == "INTERROGATE" and num_of_interrogations == 3:
                            print("Sorry you are out of interrogations")
                        elif learnmore_interrogate_hint == "INTERROGATE" and num_of_interrogations < 3:
                            which_interrogate = get_str_input("Who would you like to interrogate: ")
                            which_interrogate = which_interrogate.upper()
                            if which_interrogate == M_upper_wife_name and num_of_interrogations_wife == 0:
                                Interrogation_option_wife = get_str_input("You can choose between option 'A' and option 'B' for interrogation\nOption A: Where were you last night during the time of the murder?\nOption B: Have you and your husband had any disgreements lately?\nDo you choose 'A' or 'B': ")
                                Interrogation_option_wife = Interrogation_option_wife.upper()
                                interrogation_random_response_wife = random.randint(0,1)
                                if Interrogation_option_wife == "A":
                                    print(A_Interrogation_wife.pop(interrogation_random_response_wife))
                                    num_of_interrogations+=1
                                    num_of_interrogations_wife+=1
                                elif Interrogation_option_wife == "B":
                                    print(B_Interrogation_wife.pop(interrogation_random_response_wife))
                                    num_of_interrogations+=1
                                    num_of_interrogations_wife+=1
                                else:
                                    print("You have to type either 'A' or 'B'")
                            elif which_interrogate == M_upper_business_rival_name and num_of_interrogations_business_rival == 0:
                                Interrogation_option_business_rival = get_str_input("You can choose between option 'A' and option 'B' for interrogation\nOption A: Can you explain why you were seen arguing with the victim earlier this week?\nOption B: Where were you at the time of the murder, and can anyone confirm your alibi?\nDo you choose 'A' or 'B': ")
                                Interrogation_option_business_rival = Interrogation_option_business_rival.upper()
                                interrogation_random_response_business_rival = random.randint(0,1)
                                if Interrogation_option_business_rival == "A":
                                    print(A_Interrogation_business_rival.pop(interrogation_random_response_business_rival))
                                    num_of_interrogations+=1
                                    num_of_interrogations_business_rival+=1
                                elif Interrogation_option_business_rival == "B":
                                    print(B_Interrogation_business_rival.pop(interrogation_random_response_business_rival))
                                    num_of_interrogations+=1
                                    num_of_interrogations_business_rival+=1
                                else:
                                    print("You have to type either 'A' or 'B'")  
                            elif which_interrogate == M_upper_assistant_name and num_of_interrogations_assistant == 0:
                                Interrogation_option_assistant = get_str_input("You can choose between option 'A' and option 'B' for interrogation\nOption A: What were your duties on the night of the murder, and did you notice anything unusual?\nOption B: Did you have any personal or professional conflicts with the victim?\nDo you choose 'A' or 'B': ")
                                Interrogation_option_assistant = Interrogation_option_assistant.upper()
                                interrogation_random_response_assistant = random.randint(0,1)
                                if Interrogation_option_assistant == "A":
                                    print(A_Interrogation_assistant.pop(interrogation_random_response_assistant))
                                    num_of_interrogations+=1
                                    num_of_interrogations_assistant+=1
                                elif Interrogation_option_assistant == "B":
                                    print(B_Interrogation_assistant.pop(interrogation_random_response_assistant))
                                    num_of_interrogations+=1
                                    num_of_interrogations_assistant+=1
                                else:
                                    print("You have to type either 'A' or 'B'")
                            elif which_interrogate == M_upper_family_friend_name and num_of_interrogations_family_friend == 0:
                                Interrogation_option_family_friend = get_str_input("You can choose between option 'A' and option 'B' for interrogation\nOption A: As an ex-detective, did you notice anything out of the ordinary that night\nOption B: Where were you during the time of the murder, and can anyone verify your whereabouts?\nDo you choose 'A' or 'B': ")
                                Interrogation_option_family_friend = Interrogation_option_family_friend.upper()
                                interrogation_random_response_family_friend = random.randint(0,1)
                                if Interrogation_option_family_friend == "A":
                                    print(A_Interrogation_family_friend.pop(interrogation_random_response_family_friend))
                                    num_of_interrogations+=1
                                    num_of_interrogations_family_friend+=1
                                elif Interrogation_option_family_friend == "B":
                                    print(B_Interrogation_family_friend.pop(interrogation_random_response_family_friend))
                                    num_of_interrogations+=1
                                    num_of_interrogations_family_friend+=1
                                else:
                                    print("You have to type either 'A' or 'B'")
                            elif which_interrogate == M_upper_employee_name and num_of_interrogations_employee == 0:
                                Interrogation_option_employee = get_str_input("You can choose between option 'A' and option 'B' for interrogation\nOption A: As an ex-detective, did you notice anything out of the ordinary that night\nOption B: Where were you during the time of the murder, and can anyone verify your whereabouts?\nDo you choose 'A' or 'B': ")
                                Interrogation_option_employee = Interrogation_option_employee.upper()
                                interrogation_random_response_employee = random.randint(0,1)
                                if Interrogation_option_employee == "A":
                                    print(A_Interrogation_employee.pop(interrogation_random_response_employee))
                                    num_of_interrogations+=1
                                    num_of_interrogations_employee+=1
                                elif Interrogation_option_employee == "B":
                                    print(B_Interrogation_employee.pop(interrogation_random_response_employee))
                                    num_of_interrogations+=1
                                    num_of_interrogations_employee+=1
                                else:
                                    print("You have to type either 'A' or 'B'")
                            elif which_interrogate == M_upper_wife_name and num_of_interrogations_wife == 1:
                                print("You have already interrogated " + M_wife_name)
                            elif which_interrogate == M_upper_business_rival_name and num_of_interrogations_business_rival == 1:
                                print("You have already interrogated " + M_business_rival_name)
                            elif which_interrogate == M_upper_assistant_name and num_of_interrogations_assistant == 1:
                                print("You have already interrogated " + M_assistant_name)
                            elif which_interrogate == M_upper_family_friend_name and num_of_interrogations_family_friend == 1:
                                print("You have already interrogated " + M_family_friend_name)
                            elif which_interrogate == M_upper_employee_name and num_of_interrogations_employee == 0:
                                print("You have already interrogated " + M_employee_name)
                            else:
                                print("That is not one of the possible suspects")
                        else:
                            pass
                    else:
                        print("You must enter either 'Yes' or 'No'")
                        continue
                if M_guess == Upper_murderer:
                    break
                else:
                    print("\nsorry you are out of guesses, the murderer was ...")

#Print statements
total_plays = 0
while total_plays == 0:
    Game_to_play = get_str_input("\nWould you like to play 'Rock Paper Scissors', 'NumberGuesser', 'Murder Mystery', or quit: ")
    Game_to_play = Game_to_play.upper()
    Game_attempts = 0
    while Game_attempts == 0:
        #Rock paper scissors
        if Game_to_play == "ROCK PAPER SCISSORS":
            rock_paper_scissors()
            Play_rps_again = get_str_input("\nWould you like to play again: ")
            Play_rps_again = Play_rps_again.upper()
            if Play_rps_again == "YES":
                rock_paper_scissors()
                break
            elif Play_rps_again == "NO":
                Game_to_play = get_str_input("\nWould you like to play 'Rock Paper Scissors', 'NumberGuesser', 'Murder Mystery', or quit: ")
                Game_to_play = Game_to_play.upper()
                if Game_to_play == "ROCK PAPER SCISSORS":
                    rock_paper_scissors()
                    break
                elif Game_to_play == "NUMBERGUESSER":
                    NumberGuesser()
                    break
                elif Game_to_play == "MURDER MYSTERY":
                    Murder_mystery()
                    break
                elif Game_to_play == "QUIT":
                    print("\nLeaving the game...")
                    sys.exit()
            Game_attempts+=1
        #NumberGuesser
        elif Game_to_play == "NUMBERGUESSER":
            NumberGuesser()
            Play_ng_again = get_str_input("\nWould you like to play again: ")
            Play_ng_again = Play_ng_again.upper()
            if Play_ng_again == "YES":
                NumberGuesser()
                break
            elif Play_ng_again == "NO":
                Game_to_play = get_str_input("\nWould you like to play 'Rock Paper Scissors', 'NumberGuesser', 'Murder Mystery', or quit: ")
                Game_to_play = Game_to_play.upper()
                if Game_to_play == "ROCK PAPER SCISSORS":
                    rock_paper_scissors()
                    break
                elif Game_to_play == "NUMBERGUESSER":
                    NumberGuesser()
                    break
                elif Game_to_play == "MURDER MYSTERY":
                    Murder_mystery()
                    break
                elif Game_to_play == "QUIT":
                    print("\nLeaving the game...")
                    sys.exit()
            Game_attempts = 0
        #Murder Mystery
        elif Game_to_play == "MURDER MYSTERY":
            Murder_mystery()
            Play_ta_again = get_str_input("\nWould you like to play again: ")
            Play_ta_again = Play_ta_again.upper()
            if Play_ta_again == "YES":
                Murder_mystery()
                break
            elif Play_ta_again == "NO":
                Game_to_play = get_str_input("\nWould you like to play 'Rock Paper Scissors', 'NumberGuesser', 'Murder Mystery', or quit: ")
                Game_to_play = Game_to_play.upper()
                if Game_to_play == "ROCK PAPER SCISSORS":
                    rock_paper_scissors()
                    break
                elif Game_to_play == "NUMBERGUESSER":
                    NumberGuesser()
                    break
                elif Game_to_play == "MURDER MYSTERY":
                    Murder_mystery()
                    break
                elif Game_to_play == "QUIT":
                    print("\nLeaving the game...")
                    sys.exit()
            Game_attempts = 0
        #Quit
        elif Game_to_play == "QUIT":
            print("\nLeaving the game...")
            sys.exit()
        #Re-enter game
        else:
            Game_to_play = get_str_input("\nName a game or type 'quit': ")
            Game_to_play = Game_to_play.upper()