import os, random, re
from random import randint

def test_set():
    #choose random txtfile
    rand_file=random.choice(os.listdir("test/"))
    while (rand_file == "scraper.py") :#can't choose scraper.py
        rand_file=random.choice(os.listdir("test/"))

    print("rand_file: " + rand_file)

    #choose random game (by choosing a random line)
    rand_line = random.choice(open("test/"+rand_file).readlines())
    while (    not ( ('+' in rand_line) or ( ('-' in rand_line) and (re.match(rand_line, "(\w+)-(\w)" )) and (re.match(rand_line, "(\W+)-(\W)" )) ))   ):
    	#use regrex
    	#eliminate: RED        HUANG HaiLin ; CM  ; China-Guangdong
    	#eliminate: DATE       2014-09-22
    	rand_line = random.choice(open("test/"+rand_file).readlines())

    print("rand_line: " + rand_line)

    rand_line_len = len(rand_line)-1

    print(rand_line_len)
    
    rand_index = randint(0,rand_line_len)

    print(rand_index)

    while (    not( rand_line[rand_index].isalpha() )    ):
    	rand_index = randint(0,rand_line_len)

    print(rand_line[rand_index])
    get_rand_move= rand_line[rand_index] + rand_line[rand_index+1] + rand_line[rand_index+2] + rand_line[rand_index+3]

    print("get_rand_move: " + get_rand_move)


    line_num = 0

    f = open("test/" + rand_file)

    for line in f:
    	if line == rand_line:
    		print("check if line == randline: " + line)
    		print("check if line == randline: " + rand_line)
    		break;
    	else:
        	line_num = line_num +1
    print("line_num: "+ str(line_num))

   

    print("-----------List of moves before the random move-------------")
    # Open and read file into buffer
    f2 = open("test/" + rand_file,"r")
    lines2 = f2.readlines()

    # If we need to read line 33, and assign it to some variable
    x2 = lines2[line_num]
    print(x2)

    moves_before_randMove_string=""
    previous_line = 0


    while not ("START" in moves_before_randMove_string):
    	previous_line = previous_line +1
    	moves_before_randMove_string= "".join((lines2[line_num-previous_line], moves_before_randMove_string))
    print(moves_before_randMove_string)

test_set();










