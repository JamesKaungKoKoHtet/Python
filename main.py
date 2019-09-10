import csv
import os
class Main:
	

	def getFolderName(self,Input_Path):

		dumpFile=open(Input_Path,"r")
		dumpData= dumpFile.read()
		dumpDataList=dumpData.split("\n")
		
		#SUCCESSFULLY GOT DUMP DATA INTO LIST 
		NameDumpDataList=[]
		print("FolderNameCalled")
		#getting Name for fileName from dump data
		for x in dumpDataList:
			NameDumpDataList.append(x[0:21]+"-list.csv")
		print(" . ")
	
		# test check if values in NameDumpDataList is legit
		# for x in NameDumpDataList:
		# 	print(x)
		return NameDumpDataList
		
	def getDumpData(self,Input_Path):

		dumpFile=open(Input_Path,"r")
		dumpData= dumpFile.read()
		dumpDataList=dumpData.split("\n")
		
		#SUCCESSFULLY GOT DUMP DATA INTO LIST 
		DataToSaveList=[]
		print("DumpDataCalled")
		#getting Data form dump data
		for x in dumpDataList:
			DataToSaveList.append(x[5:36])
			
		print(" . ")
		# test check if values in DataToSaveList is legit
		# for x in DataToSaveList:
		# 	print(x)
		return DataToSaveList
	
#giving File Path (will do with scanner later)
	
	def readCSV(self,dic):
		with open(dic) as csv_file:
			csvr = csv.reader(csv_file, delimiter=',')
			readCsvData=[]
			for row in csvr:
				readCsvData.append(row)
		return readCsvData

	def writeData(self,dic,data):
		with open(dic,mode='a',newline='') as csvfile:
			writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			writer.writerow([data[0:16],data[16:30]])
			print([data[0:16],data[16:30]])

	#function for write CSV file
	def writeCSV(self):
		# readFile()
		filenameToCsv=[]
		filenameToCsv=self.getFolderName("C:\\Users\\NDMM0051\\Downloads\\pe\\DumbFile.txt")
		DumpData=[]
		DumpData=self.getDumpData("C:\\Users\\NDMM0051\\Downloads\\pe\\DumbFile.txt")

		loop_control=0;
		data_control=False

		while (1):
			path_check=os.path.isdir("C:\\Users\\NDMM0051\\Downloads\\pe\\testFile")
			#if folder is not exist create new folder
			if path_check==False:
				os.makedirs("C:\\Users\\NDMM0051\\Downloads\\pe\\testFile")
			else:
				print("break from file check/create")
				break

		index = 0

		for x in filenameToCsv:
			data_control=False
			#check file if it exist
			existence=os.path.isfile('.\\testfiles\\'+x)

			if existence == True:
				readData=self.readCSV('.\\testfile\\'+x)
				print("Line 64.....", readData)
				#check data is du
				for row in readData:
					#check list is not empty
					print("Line 71.....", a , "..... ",DumpData[index])
					if len(row)!=0:
						#check two Strings are equal
						rowFromCSV=row[0]+row[1]
						
						if DumpData[index] == rowFromCSV:
							data_control=True
							break
						else:

							prin("else here")

				#write data
				if data_control==False:
					print("carry")
					self.writeData('.\\testfiles\\'+x,DumpData[index])


			#write new data in new file
			else:
				self.writeData('.\\testfile\\'+x,DumpData[index])
			print(index)
			index=index+1
			print()
		print("Writing complete")



#main method
if __name__ == '__main__':
	class_obj = Main()
	
	class_obj.writeCSV()
	