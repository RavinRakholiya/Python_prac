# # Read text file

# # open function
# # read method
# # seek method
# # tell method
# # readline method
# # readlines method
# # close method

# # path=(r'F:\Courses\python hindi\harshit vashisth\file1.txt')

# f=open('file1.txt')                   # here i have to put txt file's path if .py file and .txt file are not in same folder.
#                                       # f=open('file1.txt','r') ---for read file, f=open('file1.txt','w') ---for write file, f=open('file1.txt')----bydefault is reading mode
# print(f.read())                # f.read() will return me the file data in string form
# f.close()

# # o/p: 
# #      -------------- Important things to remember -----------------
# #      -- never do something to impress someone.
# #      -- never live your life on someone else opinions.
# #      -- Just find whatever you love and then hustle untill you don't need to introduce yourself.




# f1=open('file1.txt')                      # o/p: -------------- Important things to remember -----------------
# print(f1.read())                          #      -- never do something to impress someone.
# print(f1.read())                          #      -- never live your life on someone else opinions.
# f1.close()                                #      -- Just find whatever you love and then hustle untill you don't need to introduce yourself.
# # python will return file data only one time even though we wrote print(f1.read()) two times. 
# # this is happen because python read text file according to cursor, hemce when second time print(f1.read()) executed, our cursor was on last position in file, therefore we got data only one time




# f2=open('file1.txt')                      # o/p: cursor position - 0
# print(f"cursor position - {f2.tell()}")   #      -------------- Important things to remember -----------------
# print(f2.read())                          #      -- never do something to impress someone.
# print(f"cursor position - {f2.tell()}")   #      -- never live your life on someone else opinions.
# print(f2.read())                          #      -- Just find whatever you love and then hustle untill you don't need to introduce yourself.
# f2.close()                                #      cursor position - 250

# # tell() method is used for getting position of cursor






# # seek() method----> it is used for changing the position of cursor
# f3=open('file1.txt') 
# print(f"cursor position - {f3.tell()}")                    
# print(f3.read())   
# print(f"cursor position - {f3.tell()}") 
# print("Before seek method")
# f3.seek(0)     
# print("After seek method")
# print(f"cursor position - {f3.tell()}")    
# print(f3.read())                          
# f3.close()                              

# # o/p: cursor position - 0
# #      -------------- Important things to remember -----------------
# #      -- never do something to impress someone.
# #      -- never live your life on someone else opinions.
# #      -- Just find whatever you love and then hustle untill you don't need to introduce yourself.
# #      cursor position - 248
# #      Before seek method
# #      After seek method
# #      cursor position - 0
# #      -------------- Important things to remember -----------------
# #      -- never do something to impress someone.
# #      -- never live your life on someone else opinions.
# #      -- Just find whatever you love and then hustle untill you don't need to introduce yourself.






# # readline() method  ----> read one line at a time

# f4=open('file1.txt')     
# print(f4.readline())                          
# f4.close()                          # o/p: -------------- Important things to remember -----------------


# f4=open('file1.txt')     
# print(f4.readline())        
# print(f4.readline())                          
# print(f4.readline())                          
# f4.close()

# # o/p: -------------- Important things to remember -----------------

# #      -- never do something to impress someone.

# #      -- never live your life on someone else opinions.


# f4=open('file1.txt')     
# print(f4.readline(),end='')         # to remove space between two line
# print(f4.readline())                          
# print(f4.readline())                          
# f4.close()

# # o/p: -------------- Important things to remember -----------------
# #      -- never do something to impress someone.

# #      -- never live your life on someone else opinions.





# # readlines() method ----> it will make list of lines which are in file
# f4=open('file1.txt')     
# lines=f4.readlines()
# print(lines)                      
# print(len(lines))        # o/p: 4
# f4.close()               # o/p: ['-------------- Important things to remember -----------------\n', '-- never do something to impress someone.\n', '-- never live your life on someone else opinions.\n', "-- Just find whatever you love and then hustle untill you don't need to introduce yourself."]


# f4=open('file1.txt')                 # o/p: -------------- Important things to remember -----------------
# lines=f4.readlines()                 #      -- never do something to impress someone.
# for line in lines:                   #      -- never live your life on someone else opinions.
#     print(line,end='')               #      -- Just find whatever you love and then hustle untill you don't need to introduce yourself.
# f4.close()




# # name, closed  ----> data descripter
# f4=open('file1.txt')     
# print(f4.name)                  # o/p: file1.txt
# print(f4.closed)                # o/p: False
# f4.close()
# print(f4.closed)                # o/p: True





# # without using read function, f4 is iterable
# f4=open('file1.txt')                 # o/p: -------------- Important things to remember -----------------
# for line in f4:                      #      -- never do something to impress someone.
#     print(line,end='')               #      -- never live your life on someone else opinions.
# f4.close()                           #      -- Just find whatever you love and then hustle untill you don't need to introduce yourself.



# # i can make slicing with the help of readlines() method
# f4=open('file1.txt')                 # o/p: -------------- Important things to remember -----------------
# for line in f4.readlines()[:2]:      #      -- never do something to impress someone.
#     print(line,end='')               
# f4.close()














# # With block  ----> it is used for reading and writing file and many other purposes also
# # it is context manager
# # in this, we don't need to use close() method to close our file and in add to it, context manager will handle our file in case of damage file

# with open("file1.txt") as f5:
#     data=f5.read()
#     print(data)

# print(f5.closed)              # o/p: True

# # o/p: 
# #      -------------- Important things to remember -----------------
# #      -- never do something to impress someone.
# #      -- never live your life on someone else opinions.
# #      -- Just find whatever you love and then hustle untill you don't need to introduce yourself.







# # -------------- Important things to remember -----------------
# # -- never do something to impress someone.
# # -- never live your life on someone else opinions.
# # -- Just find whatever you love and then hustle untill you don't need to introduce yourself.




# # 'r' mode ---> used to read file. it is bydefault mode
# # 'a' mode ---> append mode, not delet file data, in fact append new data and old data
# # 'w' mode ---> override the data(delete the old data and write new data), use when file is empty or we want to delete file data
# # 'r+' mode---> we can read and write using this mode, it will not create file, it will start override from starting of the old data but not delete all old data, so we should use seek to set cursor position

# # Write to file


# # with open("file1.txt",'w') as f6:              # w,a mode also create the file if file is not at location
# #     data=f6.write("amckmdla")                        # for a mode--->it will write 1 instead of data in file 




# # with open("file1.txt",'r+') as f6:
# #     f6.seek(len(f6.read()))
# #     f6.write("yash \n ")



















# # Read and Write ---> read one file and write those data in another file
# # here file1.txt have some data and file2.txt is empty
# with open("file1.txt","r") as rf:
#     with open("file2.txt","w") as wf:
#         wf.write(rf.read())

# # when i executed code, file2.txt get data of file1.txt

















# # Excercise 1
# with open("file1.txt","r") as rf:
#     with open("file2.txt","w") as wf:
#         for i in rf:
#             wf.write(f"{(i).split(',')[0]}\'s salary is {(i).split(',')[1]}")


# # OR
# with open("file1.txt","r") as rf:
#     with open("file2.txt","w") as wf:
#         for line in rf.readlines():
#             name, salary=line.split(',')
#             wf.write(f'{name}\'s salary is {salary}')












# # Excercise 2
# with open("index.html","r") as rf:
#     with open("link.txt","w") as wf:
#         for line in rf.readlines():
#             if "<a href=" in line:
#                 pos=line.find("<a href=")
#                 first_quot=line.find("\"",pos)
#                 second_quot=line.find("\"",first_quot+1)
#                 website=line[first_quot+1:second_quot]
#                 wf.write(website+"\n")





# # Better way
# with open("index.html","r") as rf:
#     with open("link.txt","w") as wf:
#         page=rf.read()
#         # link_exist=True
#         while True:
#             pos=page.find("<a href=")
#             if pos== -1:
#                 break
#                 # link_exist=False
#             else:
#                 first_quot=page.find("\"",pos)
#                 second_quot=page.find("\"",first_quot+1)
#                 web=page[first_quot+1:second_quot]
#                 wf.write(web+"\n")
#                 page=page[second_quot:]

















# # Read Love Story
# with open('file1.txt','r') as rf:
#     print(rf.encoding)
#     data=rf.read()
#     print(data)

# # # file1.txt
# # Love Story
# # chat start
# # 😘😗😇💓😗
# # chat end
# # Note - Real friends don't need to send this emojis !
# # One more Note - after your family, dogs love human being most but they can't send you emojis !
# # Second last note - if someone sends you thse emojis just say :) and don't get over exited !
# # Fissl Note - I love you, subscribe to this channel now ! 

# # o/p: cp1252
# #      Love Story
# #      chat start
# #      ðŸ˜˜ðŸ˜—ðŸ˜‡ðŸ’“ðŸ˜—
# #      chat end
# #      Note - Real friends don't need to send this emojis !
# #      One more Note - after your family, dogs love human being most but they can't send you emojis !
# #      Second last note - if someone sends you thse emojis just say :) and don't get over exited !
# #      Fissl Note - I love you, subscribe to this channel now !



# # to read emojis we should use encoding
# with open('file1.txt','r',encoding='utf-8') as rf:
#     print(rf.encoding)
#     data=rf.read()
#     print(data)

# # o/p: utf-8
# #      Love Story
# #      chat start
# #      �����😇💓💓😗😗
# #      chat end
# #      Note - Real friends don't need to send this emojis !
# #      One more Note - after your family, dogs love human being most but they can't send you emojis !
# #      Second last note - if someone sends you thse emojis just say :) and don't get over exited !
# #      Fissl Note - I love you, subscribe to this channel now !









# # if our file has number of char and if we read then it will not memory efficient
# with open('file1.txt','r') as rf:
#     data=rf.read(100)
#     print(data)

# # o/p: it will return only 100 char from file



# # to read whole file
# with open('file1.txt','r') as rf:
#     data=rf.read(10)
#     while(len(data)>0):
#         print(data)
#         data=rf.read(10)










# File3.csv
# name,email,phone_no
# Ravin,ravinrakholiya559@gmail.com,+918732904392
# Rupen,rupenrakholiya559@gmail.com,+917433089863






# # Work with CSV File
# # csv file ---> used for storing data in tabula form



# Read to CSV

# # we can read csv file using reader function or DictReader class from csv module


# # Read csv file using reader
# from csv import reader
# with open('file3.csv','r') as rf:
#     csv_reader=reader(rf)
#     # csv_reader is iterator
#     print(csv_reader)                   # o/p: <_csv.reader object at 0x0125D8E8>
#     print(type(csv_reader))             # o/p: <class '_csv.reader'>
#     for i in csv_reader:                # csv_reader is iterator so we can print it only one time, if we want to use more than one time then we can convert it into list.
#         print(i)

# # o/p: ['name', 'email', 'phone_no']                 # but here column name also printed, we can overcome this problem using next() methos
# #      ['Ravin', 'ravinrakholiya559@gmail.com', '+918732904392']
# #      ['Rupen', 'rupenrakholiya559@gmail.com', '+917433089863']





# # from csv import reader
# # with open(r'file3.csv','r',encoding='utf=8') as rf:
# #     csv_reader=reader(rf)
# #     # csv_reader is iterator
# #     print(csv_reader)                   # o/p: <_csv.reader object at 0x0125D8E8>
# #     print(type(csv_reader))             # o/p: <class '_csv.reader'>
# #     next(csv_reader)
# #     for i in csv_reader:                # o/p: ['Ravin', 'ravinrakholiya559@gmail.com', '+918732904392']
# #         print(i)                        #      ['Rupen', 'rupenrakholiya559@gmail.com', '+917433089863']








# # Read csv file using DictReader
# from csv import DictReader                          # we read csv file as ordered dictionary using DictReader
# with open('file3.csv','r') as rf:
#     csv_reader1=DictReader(rf)
#     print(type(csv_reader1))                         # o/p: <class 'csv.DictReader'>
#     for line in csv_reader1:
#         print(line)

# # o/p: {'name': 'Ravin', 'email': 'ravinrakholiya559@gmail.com', 'phone_no': '+918732904392'}
# #      {'name': 'Rupen', 'email': 'rupenrakholiya559@gmail.com', 'phone_no': '+917433089863'}







# from csv import DictReader                          
# with open('file3.csv','r') as rf:                    # o/p: Ravin
#     csv_reader1=DictReader(rf)                       # o/p: Rupen
#     for line in csv_reader1:
#         print(line['name'])






    

# # File3.csv
# # name|email|phone_no
# # Ravin|ravinrakholiya559@gmail.com|+918732904392
# # Rupen|rupenrakholiya559@gmail.com|+917433089863

# from csv import DictReader                          
# with open('file3.csv','r') as rf:                    # o/p: {'name|email|phone_no': 'Ravin|ravinrakholiya559@gmail.com|+918732904392'}
#     csv_reader1=DictReader(rf)                       #      {'name|email|phone_no': 'Rupen|rupenrakholiya559@gmail.com|+917433089863'}
#     for line in csv_reader1:
#         print(line)



# # sometimes we get error just because of | instead of , so we can address this issue by using delimiter
# from csv import DictReader                          
# with open('file3.csv','r') as rf:                    # o/p: {'name': 'Ravin', 'email': 'ravinrakholiya559@gmail.com', 'phone_no': '+918732904392'}
#     csv_reader1=DictReader(rf,delimiter='|')         #      {'name': 'Rupen', 'email': 'rupenrakholiya559@gmail.com', 'phone_no': '+917433089863'}
#     for line in csv_reader1:
#         print(line)




# DictReader is better than reader





# # Write to CSV
# # writer, DictWriter  -----> for write into csv file


# # write into csv using writer
# from csv import writer
# with open('file3.csv','w') as wf:                    # now file3.csv is empty
#     csv_write=writer(wf)                  # there are two methods in writer for writing 1)writerow, 2)writerows
#     csv_write.writerow(['name','country'])
#     csv_write.writerow(['Rupen','Germany'])
#     csv_write.writerow(['Ravin','India'])
#     csv_write.writerow(['Yash','Austrelia'])

# # o/p: name,country
#                                             # here we are getting line spce between two row data
# #      Rupen,Germany

# #      Ravin,India

# #      Yash,Austrelia






# from csv import writer
# with open('file3.csv','w',newline='') as wf:                    # now file3.csv is empty
#     csv_write=writer(wf)                  # there are two methods in writer for writing 1)writerow, 2)writerows

#     # # 1)writerow   ----> inside list
#     # csv_write.writerow(['name','country'])                                             # o/p: name,country
#     # csv_write.writerow(['Rupen','Germany'])                                            #      Rupen,Germany
#     # csv_write.writerow(['Ravin','India'])                                              #      Ravin,India
#     # csv_write.writerow(['Yash','Austrelia'])                                           #      Yash,Austrelia


#     # 2)writerows    ----> inside list inside list
#     csv_write.writerows([['name','country'],['Rupen','Germany'],['Ravin','India'],['Yash','Austrelia']])



# # here we are using from csv import dict....., we can do this by using only import csv, but we don't import csv because if we import csv then python searching for dict... and it may take more time





# # write into csv using DictWriter
# from csv import DictWriter                            # when we use dictwrite we have to show header(colum_name) in code
# with open("file3.csv",'w') as wf:                     # file3.csv is empty
#     csv_write=DictWriter(wf,fieldnames=['first_name','last_name','age'])
#     csv_write.writeheader()                                # this method will write header in csv file
#                  # here, also two methos for writing in csv 1) writerow    2) wrterows
#     csv_write.writerow({
#         'first_name':'Ravin',
#         'last_name':'Rakholiya',
#         'age':22
#     })                                                      # o/p: first_name,last_name,age
#     csv_write.writerow({                                    #
#         'first_name':'Rupen',                               #      Ravin,Rakholiya,22
#         'last_name':'Rakholiya1',                           #
#         'age':19                                            #      Rupen,Rakholiya1,19
#     })





# # we are getting space between two line in output, and we can address this issue using newline=''

# from csv import DictWriter                            # when we use dictwrite we have to show header(colum_name) in code
# with open("file3.csv",'w',newline='') as wf:                     # file3.csv is empty
#     csv_write=DictWriter(wf,fieldnames=['first_name','last_name','age'])
#     csv_write.writeheader()                                # this method will write header in csv file
#                  # here, also two methos for writing in csv 1) writerow    2) wrterows


#     # #  1) writerow ----> inside dict
#     # csv_write.writerow({
#     #     'first_name':'Ravin',
#     #     'last_name':'Rakholiya',
#     #     'age':22
#     # })                                                      # o/p: first_name,last_name,age
#     # csv_write.writerow({                                    #      Ravin,Rakholiya,22
#     #     'first_name':'Rupen',                               #      Rupen,Rakholiya1,19
#     #     'last_name':'Rakholiya1',                           
#     #     'age':19                                            
#     # })


    
#     # 2) writerows -----> inside list inside dict
#     csv_write.writerows([{'first_name':'Ravin', 'last_name':'Rakholiya','age':22},
#                         {'first_name':'Rupen', 'last_name':'Rakholiya1','age':19}])



# # DictWriter is betterthan Writer





# # read csv  ---> reader, DictReader
# # write csv ---> writer, DictWriter











# Read and Write CSV file simulteneously   -----> read data from one csv and write that data into another csv file

from csv import DictReader,DictWriter
with open('file3.csv','r') as rf:
    with open('file4.csv','w',newline='') as wf:                       # here file3.csv has data and file4.csv was empty
        csv_read=DictReader(rf)
        csv_write=DictWriter(wf,fieldnames=['first_name','last_name','age'])
        csv_write.writeheader()
        for line in csv_read:                                           # o/p: first_name,last_name,age              (in file4.csv for csv.writerow(line))
            # csv_write.writerow(line)                                  #      Ravin,Rakholiya,22
            # ----OR-----                                               #      Rupen,Rakholiya1,19
            fname,lname,age=line['first_name'],line['last_name'],line['age']
            csv_write.writerow({
                'first_name':fname.upper(),                    # o/p: in file4.csv
                'last_name':lname.upper(),                     #      first_name,last_name,age
                'age':age                                      #      RAVIN,RAKHOLIYA,22
            })                                                 #      RUPEN,RAKHOLIYA1,19
