txtfile='finished-games/5-ram-cup-xiangqi-championship-2.txt'

#Remove comments from txt files
import re #regrex

def removeComments(string):
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurance streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
    string = re.sub(re.compile("DIAG{.*?}",re.DOTALL ) ,"" ,string)
    return string


with open(txtfile, 'r') as myfile:
    data_lines=myfile.read()

myfile.close()

data_lines=removeComments(data_lines)

with open(txtfile, "w") as text_file:
	text_file.write(data_lines)
text_file.close





#from FitnessFunction import *

from Xiangqi import *

f = open(txtfile)
line = f.readline() #Read the first line 
move=''
while line:
	if 'START' in line:

		line = f.readline()
		print(line)

		for i in range(0,len(line)):
			char = line[i]
			if (char=='p' or char=='r' or char=='h' or char=='e' or char=='a' or char=='k' or char=='c' or char=='s' or char=='P' or char=='R' or char=='H' or char=='E' or char=='A' or char=='K' or char=='C' or char=='S'):
				if char=="p":
					move=move+"s"
				elif char=="P":
					move=move+"S"
				else:
					move = move+ char
				move = move+ line[i+1]
				if line[i+2]==".":
					move=move+"="
				else:
					move = move+ line[i+2]
				move = move+ line[i+3]

			print(move)
			if len(move)==4:
				if move[1].isdigit():
					x.Input(move[0],int(move[1]),move[2],int(move[3]))
					x.Display()
					"""
					piece_fit = PieceFitness(x.board)
					print(piece_fit)
					attack_fit = AttackingFitness(x.board)
					print(attack_fit)
					"""
					move=""
				elif 'END' in move:
					move=""
					x = None
					x = Engine()
					#pass
					#exit()
				else:
					x.Input(move[0].strip(),move[1].strip(),move[2].strip(),int(move[3].strip()))
					x.Display()
					#piece_fit = PieceFitness(x.board)
					#print(piece_fit)
					#attack_fit = AttackingFitness(x.board)
					#print(attack_fit)
					move=""


		while not('END' in line):
			line = f.readline()
			print(line)


			for i in range(0,len(line)):
				char = line[i]
				if (char=='p' or char=='r' or char=='h' or char=='e' or char=='a' or char=='k' or char=='c' or char=='s' or char=='P' or  char=='R' or char=='H' or char=='E' or char=='A' or char=='K' or char=='C' or char=='S'):
					if char=="p":
						move=move+"s"
					elif char=="P":
						move=move+"S"
					else:
						move = move+ char
					move = move+ line[i+1]
					if line[i+2]==".":
						move=move+"="
					else:
						move = move+ line[i+2]
					move = move+ line[i+3]
				print(move)
				if len(move)==4:
					if move[1].isdigit():
						try:
							x.Input(move[0],int(move[1]),move[2],int(move[3]))
							x.Display()
							"""
							piece_fit = PieceFitness(x.board)
							print(piece_fit)
							attack_fit = AttackingFitness(x.board)
							print(attack_fit)"""
						except:
							pass
						move=""
						
					elif 'END' in move:
						move=""
						x = None
						x = Engine()
						#pass
						#exit()
					else:
						try:
							x.Input(move[0].strip(),move[1].strip(),move[2].strip(),int(move[3].strip()))
							x.Display()
							#piece_fit = PieceFitness(x.board)
							#print(piece_fit)
							#attack_fit = AttackingFitness(x.board)
							#print(attack_fit)
						except:
							pass
						move=""
					



		line = f.readline()
		print(line)
		for i in range(0,len(line)):
			char = line[i]
			if (char=='p' or char=='r' or char=='h' or char=='e' or char=='a' or char=='k' or char=='c' or char=='s' or char=='P' or char=='R' or char=='H' or char=='E' or char=='A' or char=='K' or char=='C' or char=='S'):
				if char=="p":
					move=move+"s"
				elif char=="P":
					move=move+"S"
				else:
					move = move+ char
				move = move+ line[i+1]
				if line[i+2]==".":
					move=move+"="
				else:
					move = move+ line[i+2]
				move = move+ line[i+3]

			print(move)
			if len(move)==4:
				if move[1].isdigit():
						x.Input(move[0],int(move[1]),move[2],int(move[3]))
						x.Display()
						#piece_fit = PieceFitness(x.board)
						#print(piece_fit)
						#attack_fit = AttackingFitness(x.board)
						#print(attack_fit)
						move=""
				elif 'END' in move:
					move=""
					x = None
					x = Engine()
					#exit()
					#pass
					break
				else:
					x.Input(move[0].strip(),move[1].strip(),move[2].strip(),int(move[3].strip()))
					x.Display()
					#piece_fit = PieceFitness(x.board)
					#print(piece_fit)
					#attack_fit = AttackingFitness(x.board)
					#print(attack_fit)
					move=""

	line = f.readline()