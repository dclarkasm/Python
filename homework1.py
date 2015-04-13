print("let's play a game!\nGuess a number between 0 and 100.\n")

inp = 0
ub = 100
lb = 0
div = lb+(ub-lb)//2
ans = False
nc=0

while(ans!=True):
    while(inp!='y' and inp!='n'):
        inp = input("Is your number between " + str(lb) + " and " + str(div) + "? (y/n): ")
    if(ub-lb)>2:
        if inp=='y':
            ub=div
            div=lb+((ub-lb)//2)
            nc=0
        elif inp=='n':
            lb=div
            div=ub
            nc=nc+1
            if inp=='n' and nc>=2:
                print("Impossible! Lets try this again...\nGuess a number between 0 and 100.\n")
                lb=0
                ub=100
                div = lb+(ub-lb)//2
                nc=0
        inp=0
    else:
        inp=0
        while(inp!='y' and inp!='n'):
            inp = input("is your number " + str(lb+1) + "? (y/n): ")
        if inp=='y':
            print("Yay I win!")
            ans=True
        else:
            print("Impossible! Lets try this again...")
            lb=0
            ub=100
            div = lb+(ub-lb)//2
            nc=0
            imp=0
