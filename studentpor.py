from tkinter import *
import os

root60 = Tk()
root60.geometry('200x100')
root60.title('sucess')
root60.withdraw()

root62 = Tk()
root62.geometry('200x100')
root62.title('sucess')
root62.withdraw()

root61 = Tk()
root61.geometry('200x100')
root61.title('Failed')
root61.withdraw()

root = Tk()
root.geometry('600x700')
root.title('Student Portal')
root.configure(bg = 'purple')
root.withdraw()

root2 = Tk()
root2.geometry('300x300')
root2.title('Inputs')
root2.configure(bg = 'green')

root2.withdraw()

root3 = Tk()
root3.geometry('600x600')
root3.title('welcome page')
root3.configure(bg = 'yellow')

root4 = Tk()
root4.geometry('250x250')
root4.title('Log in')
root4.configure(bg = 'blue')
root4.withdraw()

def signup():
    root.deiconify()
    root3.withdraw()

sucess = Label(root60, text = 'Sucessfully signed in',font ='calibri 15 bold')
sucess.grid( row = 0, column = 0, columnspan = 2)

sucess2 = Label(root62, text = 'Sucessfully logged in',font ='calibri 15 bold')
sucess2.grid( row = 0, column = 0, columnspan = 2)

failed = Label(root61, text = 'Incorrect password',font ='calibri 15 bold')
failed.grid()

label1 = Label(root3, text =' welcome to school',font = 'times 35 bold')
label1.place(relx = 0.5, rely = 0.5, anchor = CENTER)

button1 = Button(root3, text = 'sign up',font ='calibri 15 bold', command = signup)
button1.place(relx = 0.4, rely = 0.6, anchor = CENTER)

def logg():
    root4.deiconify()
    root3.withdraw()

button2 = Button(root3, text = 'login in',font ='calibri 15 bold', command = logg)
button2.place(relx = 0.6, rely = 0.6, anchor = CENTER)



heading = Label(root, text = 'Student portal',font = 'times 35 bold', fg = 'purple', bg = 'white',padx =10)
heading.place(relx = 0.5, rely = 0.06, anchor = CENTER)

frame = Frame(root,padx = 100, bg = 'white')
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)



title = Label(frame , text = 'Portal Registration',font='calibri 20 bold', fg = 'purple',bg = 'white')
title.grid(row = 0, column = 1, sticky = 'w', ipadx = 10, padx = 10)


matric_no = Label(frame, text = 'Matric number*', fg ='purple',bg = 'white',font ='calibri 10 bold')
matric_no.grid(row = 11, column = 1,pady = 10)
matric_v = StringVar()
matric_en = Entry( frame, textvariable = matric_v)
matric_en.grid(row = 11, column = 2,pady = 10)

surname_no = Label(frame, text = 'Surname*', fg ='purple',bg = 'white',font ='calibri 10 bold')
surname_no.grid(row = 12, column = 1,pady = 10)
surname_v = StringVar()
surname_en = Entry( frame, textvariable = surname_v)
surname_en.grid(row = 12, column = 2,pady = 10)


other_no = Label(frame, text = 'Other names*', fg ='purple',bg = 'white',font ='calibri 10 bold')
other_no.grid(row = 13, column = 1,pady = 10)
other_v = StringVar()
other_en = Entry( frame, textvariable = other_v)
other_en.grid(row = 13, column = 2,pady = 10)

email_no = Label(frame, text = 'Email*', fg ='purple',bg = 'white',font ='calibri 10 bold')
email_no.grid(row = 14, column = 1,pady = 10)
email_v = StringVar()
email_en = Entry( frame, textvariable = email_v)
email_en.grid(row = 14, column = 2,pady = 10)


mobile_no = Label(frame, text = 'Mobile number*', fg ='purple',bg = 'white',font ='calibri 10 bold')
mobile_no.grid(row = 15, column = 1,pady = 10)
mobile_v = StringVar()
mobile_en = Entry( frame, textvariable = mobile_v)
mobile_en.grid(row = 15, column = 2,pady = 10)


state_no = Label(frame, text = 'State of origin*', fg ='purple',bg = 'white',font ='calibri 10 bold')
state_no.grid(row = 16, column = 1,pady = 10)
state_v = StringVar()
state_en = Entry( frame, textvariable = state_v)
state_en.grid(row = 16, column = 2,pady = 10)


password_no = Label(frame, text = 'Password*', fg ='purple',bg = 'white',font ='calibri 10 bold')
password_no.grid(row = 18, column = 1, pady = 10)
password_v = StringVar()
password_en = Entry( frame, textvariable = password_v,show = '*')
password_en.grid(row = 18, column = 2, pady = 10)


pass2_no = Label(frame, text = 'Confirm password*', fg ='purple',bg = 'white',font ='calibri 10 bold')
pass2_no.grid(row = 19, column = 1, pady = 10)
pass2_v = StringVar()
pass2_en = Entry( frame, textvariable = pass2_v,show = '*')
pass2_en.grid(row = 19, column = 2, pady = 10)

gender_v = IntVar()
gender_v.set(1)

genderLbl1 = Radiobutton(frame, text = 'male', variable = gender_v, value = 1)
genderLbl1.grid(row = 17, column = 1, pady = 10)
genderLbl2 = Radiobutton(frame, text = 'female', variable = gender_v, value = 2)
genderLbl2.grid(row = 17, column = 2, pady = 10)

country1 = Label(frame, text = 'Country*', fg ='purple',bg = 'white',font ='calibri 10 bold')
country1.grid(row = 20, column = 1, pady = 10)

countryOpt = ['Nigeria','Ghana','Algeria','liberia','usa']
clicked = StringVar()
clicked.set('Nigeria')
country = OptionMenu(frame,clicked,*countryOpt)
country.grid(row = 20, column = 2, pady = 10)

def result():
    matric = matric_en.get()
    sname = surname_en.get()
    other = other_en.get()
    email = email_en.get()
    mobile = mobile_en.get()
    state = state_en.get()
    password = password_en.get()
    pass2 = pass2_en.get()
    gender = gender_v.get()
    count = clicked.get()
    
    new_dir = 'C:\\Users\\HP\\Desktop\\studentdetails'
    os.chdir(new_dir)

    if password == pass2:
        # display1 = Label(frame, text = 'log in successful',fg ='yellow',bg = 'white',font ='calibri 15 bold')
        # display1.grid(row = 22 , column = 1, rowspan = 2)
        root60.deiconify()
        
        namelist = open('names.txt','a')
        namelist.write(matric + ',' + sname + ',' + other + ',' + email + ',' + mobile + ',' + state + ',' + password + ',' + pass2 )
        namelist.close()

        namelist = open('names.txt','a')
        namelist.write( "," + str(gender)+ ',' + count)
        namelist.close()
        # root2.deiconify()
        # mac = Label(root2, text = matric)
        # mac.grid(row = 0, column = 0)

        # su = Label(root2, text = sname)
        # su.grid(row = 0, column = 1)

        # oth = Label(root2, text = other)
        # oth.grid(row = 1, column = 0)

        # ema = Label(root2, text = email)
        # ema.grid(row = 1, column = 1)

        # mob = Label(root2, text = mobile)
        # mob.grid(row = 2, column = 0)

        # sta = Label(root2, text = state)
        # sta.grid(row = 2, column = 1)

        # pas1 = Label(root2, text = password)
        # pas1.grid(row = 3, column = 0)

        # pas2 = Label(root2, text = pass2)
        # pas2.grid(row = 3, column = 1)

        # gen = Label(root2, text = gender)
        # gen.grid(row = 4, column = 0)

    else:
        root61.deiconify()
        # display = Label(frame, text = 'Passwords are not the same',fg ='red',bg = 'white',font ='calibri 15 bold')
        # display.grid(row = 22 , column = 1, rowspan = 2)


def login():
    root.withdraw()
    root4.deiconify()
    root60.withdraw()


close = Button(frame,+
 text = 'close', command = root.quit, fg ='purple',bg = 'white',font ='calibri 10 bold')
close.grid(row = 21, column = 2 ,pady = 20)

close = Button(root2, text = 'close', command = root.quit, fg ='purple',bg = 'white',font ='calibri 10 bold')
close.grid(row = 5, column = 2 ,pady = 20)

submit = Button(frame, text = 'Submit', command = result, fg ='purple',bg = 'white',font ='calibri 10 bold')
submit.grid(row = 21, column = 1 ,pady = 20)

login = Button(root60, text = 'login', command = login , fg ='black',bg = 'white',font ='calibri 15 bold')
login.grid(row = 1, column = 0 ,pady = 20)

user_no = Label(root4, text = 'Matric number*', fg ='black',font ='calibri 15 bold')
user_no.grid(row = 0, column = 0,pady = 10)
user_v = StringVar()
user_en = Entry( root4, textvariable = user_v, width = 40)
user_en.grid(row = 1, column = 0,pady = 10)

pass3_no = Label(root4, text = 'Password*', fg ='black',font ='calibri 15 bold')
pass3_no.grid(row = 2, column = 0, pady = 10)
pass3_v = StringVar()
pass3_en = Entry( root4, textvariable = pass3_v, show = '*', width = 40)
pass3_en.grid(row = 3, column = 0, pady = 10)


def sub():
    root4.withdraw()
    root62.deiconify()

submit2 = Button(root4, text = 'Submit', command = sub, fg ='black',font ='calibri 15 bold')
submit2.grid(row = 4, column = 0 ,pady = 20)

close1 = Button(root62, text = 'close', command = root.quit, fg ='black',font ='calibri 10 bold')
close1.grid(row = 1, column = 0 ,pady = 20)


root.mainloop()
root2.mainloop()
root3.mainloop()
root4.mainloop()
root60.mainloop()
root61.mainloop()
root62.mainloop() 