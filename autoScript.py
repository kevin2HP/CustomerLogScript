
#########################
# 8/18/2020 KEVIN PENZA #
#########################
# Python 3.8.2 #     
################

########################################################################                 ########################################################################
# This code takes User input, specifically the first and last name and #                 #This script was made with the idea of automating a customer log book###
# saves it to a list This script also asigns a id to the Users input  #                 #Instead of manually saving customer Data this script will not only#####
########################################################################                 #save the save the data but also create a folder for each customer######
import os                                                                                #and give each customer their own unique Id making indexing much easier#
#allows us to use ooperating systems functionality through python                        ########################################################################
import random
allNames =[]
iD=0
#infinite while loop
while True:
   #recieve a name  
  fName = input('Enter First Name: ')
  lName  =  input('Enter Last Name: ')
  if fName == '' or lName =='' :              #If the user enters nothing for one of these inputs  I made sure to restart the loop to ensure both values are entered
        print('Enter a name')
        continue
  iD =fName[0]+lName[0]+str(random.randint(1,9000))
  customerName = str(iD) + ' - ' + fName + '-' + lName  #This is the customer id and name
  allNames.append(customerName) #saving customer detail to list
  try: # everything in this block of code will be run 
    os.makedirs('C:\\Administration\\New_Customers\\' + customerName) #Create a file with the customers name
  
  except (FileExistsError):  #if a file already exist this error will return 
    print('File Exists! enter new value')             #CONTINUE the loop will run again
    continue
  print(allNames)


