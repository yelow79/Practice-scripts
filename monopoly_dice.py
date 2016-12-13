#!usr/bin/python3

# monopoly_dice
# writen by yelow79
import random
while True:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = (die1 + die2)
        print ('You Rolled', die1, 'and', die2)
        if die1 == die2:
                print ('Totaling', total)
                print ('You Rolled Doubles')
                print ('Rolling Again!!!')
        else:
                print ('Totaling', total)
                break

        
