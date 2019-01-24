####
# Each team's file must define four tokens:
# team_name: a string
# strategy_name: a string
# strategy_description: a string
# move: A function that returns 'c' or 'b'
####

team_name = 'anthony and ui' # Only 10 chars displayed.
strategy_name = 'Collude unless Betrayed'
strategy_description = 'Collude the first couple times unless betrayed. Once betrayed, copy the actions of opponent'

def move(my_history, their_history, my_score, their_score):
    if len(my_history) <= 1:
        return 'c'
    elif len(my_history) == 5:
        return 'b'
        
    elif (their_history[-1]) == 'b':
        return 'b'
    else:
        return 'c'
''' Arguments accepted: my_history, their_history are strings.
my_score, their_score are ints.
Make my move.
Returns 'c' or 'b'.
'''
