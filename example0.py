####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'TOP_BANGAHS'
strategy_name = 'Sneaky Cooperator'
strategy_description = 'Betray once in a while in order to get a better payout, when the opponent has not betrayed in the last ten turns and only colluded during last 3 turns.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
    # This player always colludes.
    if 'b' not in opponent.history[-10:] and opponent.history[-3:] == ['C']*3:
        return 'b'
    return 'c'
    