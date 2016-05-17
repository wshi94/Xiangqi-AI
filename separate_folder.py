import random
import shutil, glob

#files that don't work:10, 72, 127, 338, 371, 444

rand_test= random.sample(range(1,662), 332) # 66+66+200 = 332 random files
#made into one list for files for val set and test set because we cant have duplicate numbers

while ( 10 in rand_test or 72 in rand_test or 127 in rand_test or 338 in rand_test or 371 in rand_test or 444 in rand_test):
	rand_test= random.sample(range(1,662), 332)
print(rand_test)
print("len: "+ str(len(rand_test)))



#test Set
test_list=[]
for i in range(0, 66):
	test_list.append(rand_test[i])
print("len")

list_allFiles = glob.glob("test/*.txt")
for l in list_allFiles:
	for n in test_list:
		if "tournament-"+str(n)+".txt" in l :
			print(l)
			src = "test/" + "tournament-"+str(n)+".txt"
			dst = "test_testSet/"+ "tournament-"+str(n)+".txt"
			shutil.move(src, dst)

#val Set
val_list=[]
for i in range(66, 132):
	val_list.append(rand_test[i])
print("len")
print(len(val_list))

list_allFiles = glob.glob("test/*.txt")

for l in list_allFiles:
	for n in val_list:
		if "tournament-"+str(n)+".txt" in l :
			print(l)
			src = "test/" + "tournament-"+str(n)+".txt"
			dst = "test_valSet/"+ "tournament-"+str(n)+".txt"
			shutil.move(src, dst)

#train Set
train_list=[]
for i in range(132, 332):
	train_list.append(rand_test[i])
print("len")
print(len(train_list))

list_allFiles = glob.glob("test/*.txt")
for l in list_allFiles:
	for n in train_list:
		if "tournament-"+str(n)+".txt" in l :
			print(l)
			src = "test/" + "tournament-"+str(n)+".txt"
			dst = "test_trainSet/"+ "tournament-"+str(n)+".txt"
			shutil.move(src, dst)


