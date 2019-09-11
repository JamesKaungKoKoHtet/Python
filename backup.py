import csv
import os
class Main:

	def setPath(input):
		return input

	def getFolderName(path):

		dumpFile=open(path,"r")
		dumpData= dumpFile.read()
		dumpDataList=dumpData.split("\n")
		
		
		NameDumpDataList=[]
		print("FolderNameCalled")
		#getting Name for fileName from dump data
		for x in dumpDataList:
			NameDumpDataList.append(x[0:21]+"-list.csv")
		print(" . ")

		return NameDumpDataList
		
	def getDumpData(path):

		dumpFile=open(path,"r")
		dumpData= dumpFile.read()
		dumpDataList=dumpData.split("\n")
		
		
		DataToSaveList=[]
		print("DumpDataCalled")
		#getting Data form dump data
		for x in dumpDataList:
			DataToSaveList.append(x[5:35])
			
		print(" . ")
		
		return DataToSaveList
	
	
#giving File Path (will do with scanner later)
dic=Main.setPath("C:\\Users\\NDMM0051\\Downloads\\pe\\DumbFile.txt")
#declaring variables to get data from methods
dataToCsv=Main.getDumpData(dic)
filenameToCsv=Main.getFolderName(dic)

print(Main.getDumpData(dic))
print(Main.getFolderName(dic))

while (1):
			path_check=os.path.isdir("C:\\Users\\NDMM0051\\Downloads\\pe\\Testfiles")
			#if folder is not exist create new folder
			if path_check==False:
				os.makedirs('C:\\Users\\NDMM0051\\Downloads\\pe\\Testfiles')
			else:
				break

for x in range(len(filenameToCsv)):
	# the head filenameToCsv[x][5:21]
	
	with open(("C:\\Users\\NDMM0051\\Downloads\\pe\\Testfiles\\")+filenameToCsv[x],mode='w',newline='') as csvf:

		csvw = csv.writer(csvf,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		
		for y in dataToCsv :
			if y[0:16] == filenameToCsv[x][5:21]:
				print(".")
				csvw.writerow([y[0:16],y[18:30]])
for x in range(len(filenameToCsv)):


	with open(("C:\\Users\\NDMM0051\\Downloads\\pe\\Testfiles\\")+filenameToCsv[x]) as csvf:
		csvr = csv.reader(csvf, delimiter=',')
		dataFromCSVfile=[]
		for row in csvr:
			dataFromCSVfile.append(row)
	print(dataFromCSVfile)
	print("data from csv file  C A L L E D ")
	
	

	temp=[]	
	for xx in range(len(dataFromCSVfile)):

		

		if dataFromCSVfile[xx] not in temp:
			with open(("C:\\Users\\NDMM0051\\Downloads\\pe\\Testfiles\\")+filenameToCsv[x],mode='w',newline='') as csvf:
				csvww = csv.writer(csvf,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
				print("CSV FILE WRITING ")
				print(dataFromCSVfile[xx])
				csvww.writerow(dataFromCSVfile[xx])
				temp.append(dataFromCSVfile[xx])
				print(" . . t")
				print(temp)
				print(" . . t")
	



				 