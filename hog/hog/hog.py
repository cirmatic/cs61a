"""The Game of Hog."""

from dice import six_sided, make_test_dice
from ucb import main, trace, interact

GOAL = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome. Defaults to the six sided dice.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1

    time=0
    sow_sad=0
    sum=0
    temp=0
    while time<num_rolls :
          temp=dice()
          sum+=temp
          time+=1    
          if temp==1 :
             sow_sad=1
    if sow_sad==1 :
       return 1
    else :
       return sum
    # END PROBLEM 1


def boar_brawl(player_score, opponent_score):
    """Return the points scored by rolling 0 dice according to Boar Brawl.

    player_score:     The total score of the current player.
    opponent_score:   The total score of the other player.

    """
    # BEGIN PROBLEM 2
    from operator import abs

    ones=player_score%10
    tens=0
    if opponent_score<=9 and opponent_score>=0 :
       tens=0
    else :
       tens=opponent_score//10%10
    
    if abs(tens-ones)==0 :
       return 1
    else :
       return abs(tens-ones)*3

    # END PROBLEM 2


def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    # BEGIN PROBLEM 3

    if num_rolls==0 :
       score=boar_brawl(player_score,opponent_score)
    else :
       score=roll_dice(num_rolls,dice)
    return score

    # END PROBLEM 3


def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Sus Fuss.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return score

def is_prime(n):
    """Return whether N is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return 0
        k += 1
    return 1

def num_factors(n):
    """Return the number of factors of N, including 1 and N itself."""
    # BEGIN PROBLEM 4

    k = 2
    num = 0
    while k <n :
     if n%k ==0 :
      num+=1
     k+=1
    return num+2

    # END PROBLEM 4

def sus_points(score):
    """Return the new score of a player taking into account the Sus Fuss rule."""
    # BEGIN PROBLEM 4
    
    if num_factors==3 or num_factors==4 :
     while not is_prime(score) :
      score+=1
     return score    
    else :
     return score
    # END PROBLEM 4

def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.
    """
    # BEGIN PROBLEM 4

    assert type(num_rolls) == int, 'num_rolls must be an integer.'

    score = simple_update(num_rolls,player_score,opponent_score,dice)
   
    score = sus_points(score)

    return score

    # END PROBLEM 4


def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the opponent's score.
    """
    return 5


def play(strategy0, strategy1, update,
         score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5, sus_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Sus
    Fuss rule is in effect.

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.

    An update function, such as sus_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)

    # BEGIN PROBLEM 5

    while score0<goal and score1<goal :
     if who==0 :
      num_rolls=strategy0(score0,score1)
      score0 = update(num_rolls,score0,score1,dice)
      who = 1-who
     elif who==1 :
      num_rolls=strategy1(score1,score0)
      score1 = update(num_rolls,score1,score0,dice)
      who = 1- who 
    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    if n==0 :
     def always_roll_0(player_score,opponent_score):
      return 0
     return always_roll_0
    elif n==1 :
     def always_roll_1(player_score,opponent_score):
      return 1
     return always_roll_1
    elif n==2 :
     def always_roll_2(player_score,opponent_score):
      return 2
     return always_roll_2
    elif n==3 :
     def always_roll_3(player_score,opponent_score):
      return 3
     return always_roll_3
    elif n==4 :
     def always_roll_4(player_score,opponent_score):
      return 4
     return always_rol_4
    elif n==5 :
     def always_roll_5(player_score,opponent_score):
      return 5
     return always_roll_5
    elif n==6 :
     def always_roll_6(player_score,opponent_score):
      return 6
     return always_roll_6 
    elif n==7 :
     def always_roll_7(player_score,opponent_score):
      return 7 
     return always_roll_7 
    elif n==8 :
     def always_roll_8(player_score,opponent_score):
      return 8
     return always_roll_8 
    elif n==9 :
     def always_roll_9(player_score,opponent_score):
      return 9
     return always_roll_9 
    elif n==10 :
     def always_roll_10(player_score,opponent_score):
      return 10
     return always_roll_10
    # END PROBLEM 6


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> catch_up(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL):
    """Return whether STRATEGY always chooses the same number of dice to roll
    given a game that goes to GOAL points.

    >>> is_always_roll(always_roll_5)
    1
    >>> is_always_roll(always_roll(3))
    1
    >>> is_always_roll(catch_up)
    0
    """
    # BEGIN PROBLEM 7
    strategy_now=strategy
    tem=strategy_now(0,0)

    i=0
    j=1
    while i<goal :
     while j<goal :
      if tem!=strategy_now(i,j) :
       return 0
      j+=1
     i+=1
     j=0
    return 1
      
    # END PROBLEM 7


def make_averaged(original_function, samples_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called SAMPLES_COUNT times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3
    """
    # BEGIN PROBLEM 8

    def result_function(*args) :
        function = original_function
        count = samples_count
        result = 0
        
        i=1
        while i<=count :
              result+=function(*args)
              i+=1
        return result//count                
    return result_function

    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, samples_count=1000):
    """Return the number of dice (1 to 10) that gives the maximum average score for a turn.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """

    # BEGIN PROBLEM 9

    max_score=0
    roll=1
    tem=0
    max_roll=0
    function=make_averaged(roll_dice,samples_count)

    while roll<=10 :
          tem=function(roll,dice)
          if max_score<tem :
             max_score=tem
             max_roll=roll

          roll+=1
    return max_roll

    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1, sus_update)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print('Max scoring num rolls for six-sided dice:', six_sided_max)

    print('always_roll(6) win rate:', average_win_rate(always_roll(6))) # near 0.5
    print('catch_up win rate:', average_win_rate(catch_up))
    print('always_roll(3) win rate:', average_win_rate(always_roll(3)))
    print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    print('boar_strategy win rate:', average_win_rate(boar_strategy))
    print('sus_strategy win rate:', average_win_rate(sus_strategy))
    print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"



def boar_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore score and Sus Fuss.
    """
    # BEGIN PROBLEM 10

    score=boar_brawl(score,opponent_score)
    if score >= threshold :
       num_rolls = 0
    return num_rolls  # Remove this line once implemented.
    # END PROBLEM 10


def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice when your score would increase by at least threshold."""
    new_score=sus_update(num_rolls,score,opponent_score)
    deta = new_score - score
    if deta>=threshold :
       num_rolls=0
    return num_rolls  # Remove this line once implemented.

    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    return 6  # Remove this line once implemented.
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
