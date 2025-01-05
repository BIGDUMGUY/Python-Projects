import random
"""
File:    pytzee.py
Author:  SETH LESLIE
Date:    11/1/24
Description:
  This program is designed to replicate the game yahtzee, but slightly altered. (Various comments describe the purpose of functions.)
"""



"""
Function to play the game:
"""
"""
1) Ask the user for the number of rolls they want to make.


2) In the end, the values for the number of 1's, 2's, 3's, 4's, 5's, and 6's are added
    - If the total is at least 63, add a bonus of 35.
"""
"""
:param num_rounds: The number of rounds the user wishes to play.
:return: The total score of the entire game.
"""
def play_game(num_rounds):
     total_score = 0

     #Plays the game however many times the user chooses to play
     for turn in range(1, num_rounds + 1):

         print("***Beginning Round", turn, "***")

         score = game_play()

         total_score += score

         print("Your score for this round is: ", score)


     print("Your total score is: ", total_score)

     if total_score >= 63:
          total_score += 35
          print("Your score is 63 or above! You get a bonus of 35 points!!! Your new score is :", total_score)
     
     return total_score
"""
3) If the user selects to count 1's, 2',s 3's, 4's, 5's, or 6's, count the number of dice with that n
umber and then give the user the number of points equal to the value of the die times the number of t
imes it occurs.

4) The user must be able to skip if they have already used an option previously.
    - ex. If "three of a kind" is already used, the user must skip.

Function to carry out the process of playing the game.
:return: The individual values of all the moves.
"""
def game_play():

    user_roll_values = []

    ones_value = 0

    twos_value = 0

    threes_value = 0

    fours_value = 0

    fives_value = 0

    sixes_value = 0

    pytzee_value = 0

    pytzee_counter = 0

    three_of_kind_value = 0

    three_of_kind_counter = 0

    four_of_kind_counter = 0

    four_of_kind_value = 0

    small_straight_value = 0

    small_straight_counter = 0

    large_straight_value = 0

    large_straight_counter = 0

    full_house_value = 0

    full_house_counter = 0

    chance_counter = 0

    chance_value = 0

    QUIT_STRING = "quit"

    COUNT_INDEX_DECIDER = -3

    COUNT_STRING_DECIDER = "t"

    COUNT_NUMBER_INDEX = -1

    PYTZEE_STRING = "pytzee"

    THREE_OF_KIND_STRING = "three of a kind"

    FOUR_OF_KIND_STRING = "four of a kind"

    SMALL_STRAIGHT_STRING = "small straight"

    LARGE_STRAIGHT_STRING = "large straight"

    FULL_HOUSE_STRING = "full house"

    CHANCE_STRING = "chance"

    #A random number form 1-6 is chosen five times to fulfill the number of dice.
    for roll in range(5):
        user_roll_values.append(random.choice([1, 2, 3, 4, 5, 6]))

    print(user_roll_values)
    user_count_choice = input("How would you like to count this dice roll? (Enter 'quit' to skip\
.)>> " )

    if user_count_choice.lower() != QUIT_STRING:

         #If statement determining which number to count based on input.
         if user_count_choice[COUNT_INDEX_DECIDER] == COUNT_STRING_DECIDER:

             print("Accepting ", user_count_choice[COUNT_NUMBER_INDEX])

             for rolls in user_roll_values:
                  if rolls == int(user_count_choice.strip().split()[COUNT_NUMBER_INDEX]):

                      if rolls == 1:
                           ones_value += rolls

                      elif rolls == 2:
                           twos_value += rolls

                      elif rolls == 3:
                           threes_value += rolls

                      elif rolls == 4:
                           fours_value += rolls

                      elif rolls == 5:
                           fives_value += rolls

                      elif rolls == 6:
                           sixes_value += rolls

             print("Score card:"
          "\n1's:", ones_value,
          "\n2's:", twos_value,
          "\n3's:", threes_value,
          "\n4's:", fours_value,
          "\n5's:", fives_value,
          "\n6's:", sixes_value,
          "\nThree of a kind:", three_of_kind_value,
          "\nFour of a kind:", four_of_kind_value,
          "\nFull House:",  full_house_value,
          "\nPytzee:", pytzee_value,
          "\nChance:", chance_value,
          "\nSmall straight:", small_straight_value,
          "\nLarge straight:", large_straight_value)

         elif user_count_choice.lower() == THREE_OF_KIND_STRING:

              three_of_kind_counter += 1

              if three_of_kind_value > 1:

                   print("There is already a score in that slot.")
              else:

                   three_of_kind_value = three_of_a_kind(user_roll_values)

                   user_scorecard(0,0,0,0,0,0,three_of_kind_value,0,0,0,0,0,0)
                  elif user_count_choice.lower() == FOUR_OF_KIND_STRING:
              four_of_kind_counter += 1

              if four_of_kind_value > 1:

                   print("There is already a score in that slot.")
              else:
                   four_of_kind_value += four_of_a_kind(user_roll_values)
                   user_scorecard(0,0,0,0,0,0,0,four_of_kind_value,0,0,0,0,0)

         elif user_count_choice.lower() == PYTZEE_STRING:

              pytzee_value += pytzee(user_roll_values)

              user_scorecard(0,0,0,0,0,0,0,0,0,pytzee_value,0,0,0)

              pytzee_counter += 1

              if pytzee_counter > 1:
                   pytzee_value += 100

         elif user_count_choice.lower() == SMALL_STRAIGHT_STRING:

              small_straight_counter += 1

              if small_straight_counter > 1:
                   print("There is already a score in that slot.")

              else:

                   small_straight_value += small_straight(user_roll_values)

                   user_scorecard(0,0,0,0,0,0,0,0,0,0,0,small_straight_value,0)

         elif user_count_choice.lower() == LARGE_STRAIGHT_STRING:
              large_straight_counter += 1

              if large_straight_counter > 1:
                   print("There is already a score in that slot.")
              else:

                   large_straight_value += large_straight(user_roll_values)

                   user_scorecard(0,0,0,0,0,0,0,0,0,0,0,0,large_straight_value)
                
         elif user_count_choice.lower() == FULL_HOUSE_STRING:
              full_house_counter += 1

              if full_house_counter > 1:
                   print("There is already a score in that slot.")
              else:
                   full_house_value += full_house(user_roll_values)

                   user_scorecard(0,0,0,0,0,0,0,0,full_house_value,0,0,0,0)

         elif user_count_choice.lower() == CHANCE_STRING:
              chance_counter += 1

              if chance_counter > 1:
                   print("There is already a score in that slot.")

              else:

                   chance_value += chance(user_roll_values)

                   user_scorecard(0,0,0,0,0,0,0,0,0,0,chance_value,0,0)
    else:

         return 0

    return ones_value + twos_value + threes_value + fours_value + fives_value + sixes_value + three_of_kind_value + four_of_kind_value + pytzee_value + full_house_value + chance_value + large_straight_value +\
 small_straight_value



"""
5) If the user chooses three or four of a kind and there is a three or four of a kind, they are awarded all points for all rolls.
"""
"""
Function to check if roll items contain three of a kind:
:param roll_list: The rolls of the user
:return: The total value of the rolls if there is truly a three of a kind. If not, then return 0.
"""

def three_of_a_kind(roll_list):

     num_one = 0
     num_two = 0
     num_three = 0
     num_four = 0
     num_five = 0
     num_six = 0



     total_value = 0

     #For each loop which updates the number trackers and determines if the roll is truly a three of a kind.
     for roll in roll_list:


        if roll == 1:
            num_one += 1

        elif roll == 2:
            num_two += 1

        elif roll == 3:
            num_three += 1

        elif roll == 4:
            num_four += 1

        elif roll == 5:
            num_five += 1

        elif roll == 6:
            num_six += 1

     if num_one >= 3 or num_two >= 3 or num_three >= 3 or num_four >= 3 or num_five >= 3 or num_six >= 3:
         print("Three of a kind!")

         for roll in roll_list:
             total_value += int(roll)

     else:
         print("This is not a three of a kind!")


     return total_value




"""
Function to check if roll items contain four of a kind:
:param roll_list: The rolls of the user
:return: The total value of the rolls if there is truly a four of a kind. If not, then return 0.
"""

def four_of_a_kind(roll_list):

     num_one = 0
     num_two = 0
     num_three = 0
     num_four = 0
     num_five = 0
     num_six = 0



     total_value = 0

     #Similar to the three of a kind function, but instead of searching if a value appears three times this function determines if a values appears four times.
     for roll in roll_list:


        if roll == 1:
            num_one += 1

        elif roll == 2:
            num_two += 1

        elif roll == 3:
            num_three += 1

        elif roll == 4:
            num_four += 1

        elif roll == 5:
            num_five += 1

        elif roll == 6:
            num_six += 1

     if num_one == 4 or num_two == 4 or num_three == 4 or num_four == 4 or num_five == 4 or num_six == 4:
         print("Four of a kind!")

         for roll in roll_list:
             total_value += int(roll)

     else:
         print("This is not a four of a kind!")

     return total_value

"""
6) Pytzee = All rolls are the same. (1,1,1,1). If the user selects pytzee, they get 50 points; 100 additional point for every pytzee afterward.
"""
"""
Function to check if roll items are a pytzee:
:param roll_list: The rolls of the user
:return: Fifty points are awarded if there is truly a pytzee. If not, then return 0.
"""
def pytzee(roll_list):


    success_counter = 0
    total = 0

    #A pytzee is when all numbers in a roll are the same. If numbers in index positions 1, 2, 3, and 4 are equal to the number in index position 0, then a pytzee is achieved.
    for roll in roll_list:
        if roll == roll_list[0]:

            success_counter += 1



    if success_counter == len(roll_list):

        print("Pytzee!")
        for roll in roll_list:

            total += roll

        total += 50
    else:
        print("This is not a Pytzee!")
        return 0

    print(total)
    return total



"""
Function to check if roll items contain small straight:
7) Small straight = Four-number sequence in a row. (1,2,3,4), (4,5,6,7). If the user has a small straight, then award 30 points.
"""
"""
:param roll_list: The rolls of the user
:return: 30 points are awarded if the rolls truly contain a small straight. If not, then return 0.
"""
def small_straight(roll_list):

    roll_list.sort()



    total_score = 0

    num_one = 0

    num_two = 0

    num_three = 0

    num_four = 0

    num_five = 0

    num_six = 0


    for roll in roll_list:

        if roll == 1:
            num_one += 1

        elif roll == 2:
            num_two += 1

        elif roll == 3:
            num_three += 1

        elif roll == 4:
            num_four += 1

        elif roll == 5:
            num_five += 1

        elif roll == 6:
            num_six += 1

    #The number of times a certain number appears is tracked, and then compared in the following if statement in order to determine a small straight.
    if (num_one >= 1 and num_two >= 1 and num_three >= 1 and num_four >= 1) or (num_two >= 1 and num_three >= 1 and num_four >= 1 and num_five >= 1) or (num_three >= 1 and num_four >= 1 and num_five >= 1 and num_six >= 1):

        print("Small straight!")
        
        total_score += 30

    else:
        print("This is not a small straight!")
        return 0
    return total_score




"""
Function to check if roll items contain large straight:
8) Large straight = five-nunmber sequence in a row. (1,2,3,4,5), (2,3,4,5,6). If the user has a large straight, then award 40 points.
"""
"""
:param roll_list: The rolls of the user
:return: 40 points are awarded if the rolls truly contain a large straight. If not, then return 0.
"""
def large_straight(roll_list):

    roll_list.sort()



    total_score = 0

    #If the roll list is equal to these values, then it is marked as a large straight.
    if roll_list == [1, 2, 3, 4, 5] or roll_list == [2, 3, 4, 5, 6]:
        print("Large straight!")
        total_score += 40

    else:
        print("This is not a large straight!")
        return 0

    return total_score

"""
Function to handle Full House:
9) Full House = Three of a kind and a pair of a different number. (3,3,3,2,2). If the user has a full house, give them 25 points.
"""

"""
:param roll_list: The rolls of the user
:return: 25 points are awarded if the rolls contain a full house. If not, then return 0.
"""
def full_house(roll_list):

    roll_list.sort()

    total_score = 0
    #If the roll list equals these values, then it is marked as a full house.
    if roll_list == [1, 1, 2, 2, 2] or roll_list == [2, 2, 3, 3, 3] or roll_list == [3, 3, 4, 4, 4,] or roll_list == [4, 4, 5, 5, 5] or roll_list == [5, 5, 6, 6, 6]:
         print("Full House!")
         total_score += 25

    else:
        print("This is not a full house!")
        return 0

    return total_score


"""
Function to handle chance:
:param roll_list: The rolls of the user
:return: The total value of the user's rolls.
"""
def chance(roll_list):

    total_score = 0

    print("Chance!")

    #Simply calculates the total value of the user rolls. The end result is returned.
    for roll in roll_list:
        total_score += roll

    return total_score





"""
Function to handle scoring:
:param ones_score: The returned value of the number of 1's counted.
:param twos_score: The returned value of the number of 2's counted.
:param threes_score: The returned value of the number of 3's counted.
:param fours_score: The returned value of the number of 4's counted.
:param fives_score: The returned value of the number of 5's counted.
:param sixes_score: The returned value of the number of 6's counted.
:param three_of_kind_score: The returned value of the three of a kind score.
:param four_of_kind_score: The returned value of the four of a kind score.
:param full_house_score: The returned value of the full house score score.
:param pytzee_score: The returned value of the pytzee score.
:param chance_score: The returned value of the chance score.
:param small_straight_score:The returned value of the small straight score.
:param large_straight_score: The returned value of the large straight score.
:return: A score card with all the total values.
"""
def user_scorecard(ones_score, twos_score, threes_score, fours_score, fives_score, sixes_score, three_of_kind_score, four_of_kind_score, full_house_score, pytzee_score, chance_score, small_straight_score, lar\
ge_straight_score):

     ones_scorecard = 0
     twos_scorecard = 0
     threes_scorecard = 0
     fours_scorecard = 0
     fives_scorecard = 0
     sixes_scorecard = 0
     three_of_kind_scorecard = 0
     four_of_kind_scorecard = 0
     full_house_scorecard = 0
     pytzee_scorecard = 0
     chance_scorecard = 0
     small_straight_scorecard = 0
     large_straight_scorecard = 0

     ones_scorecard += ones_score
     twos_scorecard += twos_score
     threes_scorecard += threes_score
     fours_scorecard += fours_score
     fives_scorecard += fives_score
     sixes_scorecard += sixes_score
     three_of_kind_scorecard += three_of_kind_score
     four_of_kind_scorecard += four_of_kind_score
     full_house_scorecard += full_house_score
     pytzee_scorecard += pytzee_score
     chance_scorecard += chance_score
     small_straight_scorecard += small_straight_score
     large_straight_scorecard += large_straight_score

     #The score card is printed and returned with all values.
     return print("Score card:"
                  "\n1's:", ones_scorecard,
                  "\n2's:", twos_scorecard,
                  "\n3's:", threes_scorecard,
                  "\n4's:", fours_scorecard,
                  "\n5's:", fives_scorecard,
                  "\n6's:", sixes_scorecard,
                  "\nThree of a kind:", three_of_kind_scorecard,
                  "\nFour of a kind:", four_of_kind_scorecard,
                  "\nFull House:",  full_house_scorecard,
                  "\nPytzee:", pytzee_scorecard,
                  "\nChance:", chance_scorecard,
                  "\nSmall straight:", small_straight_scorecard,
                  "\nLarge straight:", large_straight_scorecard)




if __name__ == "__main__":

    user_rounds = input("How many rounds do you want to play? >> ")
    play_game(int(user_rounds))
