###RANDOM GENERATION OF FACIAL EXPRESSIONS


##REFERENCE EMAIL:
# You can make 6 blocks

# 1. Two blocks where go will be for Happy/ angry but no go for neutral faces.

# 2.  Two blocks where go will be for Neutral/ angry but no go for Happy faces.

# 3.  Two blocks where go will be for Happy/ neutral but no go for angry faces.

# You can present these block in alternating manner. 

# Counterbalancing means that you have make sure that if for participant 1 2 3 block then to participant 2 you should give eg 2 3 1 manner then participant 3 would get 312 etc... So that it can be said that order of the target stimulus was not a factor in the experiement.


def gen():
	import random 
	import os
	import os

	angry_list=list()
	happy_list=list()
	neutral_list=list()
	#rest_list=list()
	path=os.path.abspath(os.getcwd())

	files=os.listdir(path+"/angry")
	for file in files:
		angry_list.append("angry"+file)

	files=os.listdir(path+"/happy")
	for file in files:
		happy_list.append("happy"+file)

	files=os.listdir(path+"/neutral")
	for file in files:
		neutral_list.append("neutral"+file)


	#run 1
	#70 percent angry+happy 30 percent neutral
	#shuffle both the lists
	random.shuffle(angry_list)
	random.shuffle(happy_list)
	Tget=angry_list+happy_list
	random.shuffle(Tget)
	RUN1_list=PrepareRun(Tget,neutral_list,42,18)
	#run 2
	#70 percent angry+neutral 30 percent happy
	random.shuffle(angry_list)
	random.shuffle(neutral_list)
	Tget=angry_list+neutral_list
	random.shuffle(Tget)
	RUN2_list=PrepareRun(Tget,happy_list,42,18)
	#run 3
	#70 percent happy+neutral 30 percent angry
	random.shuffle(happy_list)
	random.shuffle(neutral_list)
	Tget=happy_list+neutral_list
	random.shuffle(Tget)
	RUN3_list=PrepareRun(Tget,angry_list,42,18)

	PrepareXLSX(RUN1_list,1)
	PrepareXLSX(RUN2_list,2)
	PrepareXLSX(RUN3_list,3)
def PrepareXLSX(RUN_LIST,N):
	import xlsxwriter
	import random

	Actual_XLSX=str("Actual")+str(N)+str(".xlsx")
	Trail_XLSX=str("Trial")+str(N)+str(".xlsx")

	workbook=xlsxwriter.Workbook(Actual_XLSX)
	workbook2=xlsxwriter.Workbook(Trail_XLSX)
	worksheet=workbook.add_worksheet()
	worksheet2=workbook2.add_worksheet()

	row=0
	column=0
	trow=0
	tcolumn=0

	worksheet.write(row,column,"Image_Name")
	worksheet.write(row,column+1,"Emotion")
	worksheet.write(row,column+2,"Correct_Answer")

	worksheet2.write(row,column,"Image_Name")
	worksheet2.write(row,column+1,"Emotion")
	worksheet2.write(row,column+2,"Correct_Answer")

	row=1
	trow=1

	print(RUN_LIST)
	random.shuffle(RUN_LIST)
	counter=0

	for i in RUN_LIST:
		print(i)
		if(i[0]=="a"):
			#angry
			worksheet.write(row,column,i[5:])
			worksheet.write(row,column+1,"angry")
			worksheet.write(row,column+2,"angry")
			if(counter%4==0 and trow<9):
				worksheet2.write(trow,tcolumn,i[5:])
				worksheet2.write(trow,tcolumn+1,"angry")
				worksheet2.write(trow,tcolumn+2,"angry")
				trow=trow+1
			
		elif(i[0]=="h"):
			#happy 
			worksheet.write(row,column,i[5:])
			worksheet.write(row,column+1,"happy")
			worksheet.write(row,column+2,"happy")
			if(counter%4==0 and trow<9):
				worksheet2.write(trow,tcolumn,i[5:])
				worksheet2.write(trow,tcolumn+1,"happy")
				worksheet2.write(trow,tcolumn+2,"happy")
				trow=trow+1
			
		elif(i[0]=="n"):
			#neutral
			worksheet.write(row,column,i[7:])
			worksheet.write(row,column+1,"neutral")
			worksheet.write(row,column+2,"neutral")
			if(counter%4==0 and trow<9):
				worksheet2.write(trow,tcolumn,i[7:])
				worksheet2.write(trow,tcolumn+1,"neutral")
				worksheet2.write(trow,tcolumn+2,"neutral")
				trow=trow+1
			
		else:
			worksheet.write(row,column,i)
			worksheet.write(row,column+1,"rest")
			worksheet.write(row,column+2,"rest")
		row=row+1

	workbook.close()
	workbook2.close()

	print("DONE!")
def PrepareRun(list1,list2,n1,n2):
	rv=list()

	i=0
	j=0
	while(j<n1):
		if(i==len(list1)):
			i=0
		rv.append(list1[i])
		i=i+1
		j=j+1
	i=0
	j=0
	while(j<n2):
		#print(i)
		if(i==len(list2)):
			i=0
		rv.append(list2[i])
		i=i+1
		j=j+1
	return rv

if __name__=="__main__":
	gen()