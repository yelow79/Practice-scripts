# wg_dice
# writen by yelow79
import random
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = (die1 + die2)
print (total)
if die1 == die2:
	print ('doubles')
if total > 9:
	print ('nice roll')
if total < 5:
	print ('Unlucky!')
