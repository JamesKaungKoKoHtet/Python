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
			DataToSaveList.append(x[5:36])
			
		print(" . ")
		
		return DataToSaveList
		
#giving File Path (will do with scanner later)
dic="C:\\Users\\NDMM0051\\Downloads\\pe\\DumbFile.txt"
#declaring variables to get data from methods
dataToCsv=Main.getDumpData(dic)
filenameToCsv=Main.getFolderName(dic)

# print(dataToCsv)
# print("printing dump data")
# print(dataToCsv[0][0:16])
# print(filenameToCsv)
# print(dataToCsv[0][17:32])



while (1):
			path_check=os.path.isdir("C:\\Users\\NDMM0051\\Downloads\\pe\\Testfiles")
			#if folder is not exist create new folder
			if path_check==False:
				os.makedirs('C:\\Users\\NDMM0051\\Downloads\\pe\\Testfiles')
			else:
				break


for x in filenameToCsv:
	print(" ------------------------")
	print("THIS CSV CREATED")
	print(x)
	print(" ------------------------")
		
	with open(("C:\\Users\\NDMM0051\\Downloads\\pe\\Testfiles\\")+x,mode='w',newline='') as csvf:

		csvw = csv.writer(csvf,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		
		writeTempList=[]
		writeTemp=""
		for y in dataToCsv :
			
			if y[0:16] == x[5:21]:
				
				print(".")
			
				print("write temp loop")
				A=y[17:32]
				#  CANNOT CHECK IF A IS IN WRITE TEMP LIST COZ LSIT AND STRING 
				# change writetempList to writeTemp(strings) will work for a paw out data but not from far
				
				if A in writeTempList:
					print(" _________________________________________________")
					print(A)
					print("            . . . . . . . . NOT WRITING DATA  > > > > >  ")
					print("TEMP FILE IS HERE ")
					print(writeTempList)
					print(" _________________________________________________")

				if not A in writeTempList:

					print("write row here ")

					csvw.writerow([y[0:16],y[17:32]])

					print(y[0:16],y[17:32])

					writeTemp=[y[17:32]]

					writeTempList.append(writeTemp)

					print("TEMP FILE IS HERE ")
					print(writeTempList)


		