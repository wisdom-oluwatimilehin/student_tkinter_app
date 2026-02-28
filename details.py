import os
ask = int(input("how many inputs will you like to put in: "))
o = 1
new_dir = 'C:\\Users\\HP\\Desktop\\detailsdir'
os.chdir(new_dir)
detailslist = open('details.csv','w')


while ask > 0:
    print("Enter", o)
    matric_no = input("Enter your matric"" number: ")
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    email = input("Enter your email: ")
    phone_no = input("Enter your phone number: ")


    
    detailslist = open('details.csv','a')

    detailslist.write( matric_no + ',' )



    detailslist = open('details.csv','a')

    detailslist.write( fname + ' ,'  )


    detailslist = open('details.csv','a')

    detailslist.write( lname + ',' )



    detailslist = open('details.csv','a')

    detailslist.write(email + ',' )



    detailslist = open('details.csv','a')

    detailslist.write(phone_no + ',' +'\n' )

    detailslist.close()
    ask -= 1
    o += 1


f =  open('details.csv','r')
content = f.read()
print("Your details are....")
print(content)