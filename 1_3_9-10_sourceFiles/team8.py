####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Rock and Leah' # Only 10 chars displayed.
strategy_name = 'Loyal Betray, Betray, Collude'
strategy_description = 'If the opponent copies the strategy, program colludes, otherwise it betrays'
    
def move(my_history, their_history, my_score, their_score):
  #play b,b,c and if opponent copies collude, and betray otherwise
   if len(my_history) <=2:
       return 'b'
   if len(my_history) ==3:
       return 'c' 
   if (their_score) ==-750 and (their_history) ==3:
       return 'c'
   else:
       return 'b'
   # For rounds onwards betray if severly punished and if not, collude
       recent_round_them = their_history[-1]
       recent_round_me = my_history[-1]
                  
       # Look at rounds before that one
       for round in range(len(my_history)-1):
           prior_round_them = their_history[round]
           prior_round_me = my_history[round]
           # If one matches
           if (prior_round_me == recent_round_me) and \
                   (prior_round_them == recent_round_them):
               return their_history[round]
       # No match found
       if my_history[-1]=='c' and their_history[-1]=='b':
           return 'b' # Betray if they were severely punished last time
       else:
           return 'c' # Otherwise collude.

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             
