"""
This script saves each topic in a bagfile as a csv.

Accepts a filename as an optional argument. Operates on all bagfiles in current directory if no argument provided

Usage1 (for one bag file):
	python bag2csv.py filename.bag
Usage 2 (for all bag files in current directory):
	python bag2csv.py

Written by Nick Speal in May 2013 at McGill University's Aerospace Mechatronics Laboratory
www.speal.ca
modified by V. Hugel on May 2016 to deal with specific features
"""

"""
for python3
	pip3 install pycryptodomex
	pip3 install gnupg
	pip3 install rospkg
"""

import rosbag, sys, csv
import time
import string
import os #for file management make directory
import shutil #for file management, copy file

#verify correct input arguments: 1 or 2
if (len(sys.argv) > 2):
	print ("invalid number of arguments:   " , str(len(sys.argv)))
	print ("should be 2: 'bag2csv.py' and 'bagName'")
	print ("or just 1  : 'bag2csv.py'")
	sys.exit(1)
elif (len(sys.argv) == 2):
	print ("reading only 1 bagfile: ", sys.argv[1])
	listOfBagFiles = [sys.argv[1]]
	numberOfFiles = str(len(listOfBagFiles))
elif (len(sys.argv) == 1):
	listOfBagFiles = [f for f in os.listdir(".") if f[-4:] == ".bag"]	#get list of only bag files in current dir.
	numberOfFiles = str(len(listOfBagFiles))
	print ("reading all ", numberOfFiles, " bagfiles in current directory: \n")
	for f in listOfBagFiles:
		print(f)
	print ("\n press ctrl+c in the next 10 seconds to cancel \n")
	time.sleep(10)
else:
	print ("bad argument(s): ", str(sys.argv))	#shouldnt really come up
	sys.exit(1)

count = 0
for bagFile in listOfBagFiles:
	count += 1
	print ("reading file " , str(count) , " of  " , numberOfFiles + ": " , bagFile)
	#access bag
	bag = rosbag.Bag(bagFile)
	bagContents = bag.read_messages()
	bagName = bag.filename


	#create a new directory
	#folder = str.rstrip(bagName, ".bag")
	folder = 'data_measurements';
	try:	#else already exists
		os.makedirs(folder)
	except:
		pass
	shutil.copyfile(bagName, folder + '/' + bagName)


	#get list of topics from the bag
	listOfTopics = []
	for topic, msg, t in bagContents:
		if topic not in listOfTopics:
			listOfTopics.append(topic)

	print(listOfTopics)

	for topicName in listOfTopics:
		#Create a new CSV file for each topic
		filename = folder + '/' + str.replace(topicName, '/', '_slash_') + '.csv'
		with open(filename, 'w+') as csvfile:
			filewriter = csv.writer(csvfile, delimiter = ',')
			firstIteration = True	#allows header row
			for subtopic, msg, t in bag.read_messages(topicName):	# for each instant in time that has data for topicName
				#parse data from this instant, which is of the form of multiple lines of "Name: value\n"
				#	- put it in the form of a list of 2-element lists
				msgString = str(msg)
				msgList = str.split(msgString, '\n')
				if topicName == '/mavros/global_position/global':
					#print msgList
					# remove frame_id with local origin
					msgList.remove('  frame_id: local_origin');
					msgList.remove('header: ');
					msgList.remove('  stamp: ');
					msgList.remove('status: ');
				else :
					if topicName == '/consignes':
						# replace False by 0 and True by 1
						if msgList[0]=='besoin_correction: False':
							msgList[0]='besoin_correction: 0'
						else:
							msgList[0]='besoin_correction: 1'
					else :
						if topicName == '/gps_aplati':
							msgList.remove('header: ');
							msgList.remove('  stamp: ');
							msgList.remove("  frame_id: ''")
							msgList.remove('status: ');
						else :
							if topicName == '/mavros/battery':
								msgList.remove('header: ');
								msgList.remove('  stamp: ');
								msgList.remove("  frame_id: ''")
							else :
								if topicName == '/cmd_vel':
									msgList.remove('linear: ');
									msgList.remove('angular: ');			

				instantaneousListOfData = []
				for nameValuePair in msgList:
					splitPair = str.split(nameValuePair, ':')
					for i in range(len(splitPair)):	#should be 0 to 1
						splitPair[i] = str.strip(splitPair[i])
					if topicName == '/mavros/global_position/global' or topicName == '/gps_aplati': 
						if splitPair[0] == 'position_covariance':
							# loop for 1 to 9, contruct 9 new pairs of string.
							splitCovariance = str.split(splitPair[1][1:len(splitPair[1])-1], ',')
							for k in range(len(splitCovariance)):
								splitCovariance[k] = str.strip(splitCovariance[k])
								instantaneousListOfData.append(["PosCov"+str(k+1),splitCovariance[k]])
						else:	
							instantaneousListOfData.append(splitPair)
					else:
						instantaneousListOfData.append(splitPair)
				#write the first row from the first element of each pair
				if firstIteration:	# header
					headers = ["rosbagTimestamp"]	#first column header
					for pair in instantaneousListOfData:
						headers.append(pair[0])
					filewriter.writerow(headers)
					firstIteration = False
				# write the value from each pair to the file
				values = [str(t)]	#first column will have rosbag timestamp
				for pair in instantaneousListOfData:
					values.append(pair[1])
				filewriter.writerow(values)
	bag.close()
print ("Done reading all ", numberOfFiles, " bag files.")
