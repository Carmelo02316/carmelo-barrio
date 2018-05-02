user_ball_size = int(input("what size is the ball? "))
ball_color = input("what color is the ball? ") 
ball_sponsor = input("what is the ball's sponsor? ")
user_knuckleball = input("True or False: was it a knuckleball? ")
tivela = input("True or False, was it a trivela? ")
rabona = input("True or False, was it a rabona? ")

def ball_size():
    print(user_ball_size)
    if user_ball_size == 5:
        print " the ball is regulation size"
    else:
        print "the ball is not regulation size"
        
ball_size()
        