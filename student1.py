from tkinter import *
from tkinter import messagebox
import os
import re
import ast
import mysql.connector

myconn = mysql.connector.connect(
    host="localhost", 
    user = "root",
    passwd = "",
    port="3306", 
    database = "userdetails"
    )

control = myconn.cursor()

# new_dir = 'C:\\Users\\HP\\Desktop\\studentdetails'
# os.chdir(new_dir)


def result2():
    root2.withdraw()
    
    matric2 = matric_en2.get()
    password2 = password_en2.get()

    # f =  open('C:\\Users\\HP\\Desktop\\studentdetails\\details.txt','r')
    # content = f.readlines()
    
    selectQry = ''' SELECT * FROM info
                    WHERE password = '{0}' and email='{1}'
                '''.format(password,email)
    control.execute(selectQry)
    output=control.fetchall()
    if output:
        for feilds in output:
            print('welcome dear',feilds[0])
    else:
        print('No match found') 
    status = False
    
    # for i in content:
    #     b = ast.literal_eval(i)
    #     der = b.values()
    #     if b.get('matric') == matric2 and b.get('password') == password2:
            status = True
            
    if status:
        messagebox.showinfo('sucessful','Log in successful')

        root4 = Toplevel(root)
        root4.title('Details')
        root4.geometry('600x300')
        label1 = Label(root4, text = 'your details are:')
        label1.pack()
        img = PhotoImage(file ='C:\\Users\\HP\\Pictures\\CASEtools.PNG' )
        imglbl = Label(root4,image = img, width = 10, height = 10)
        imglbl.pack()
        label1 = Label(root4, text = der)
        label1.pack()
        
    elif b.get('matric') != matric2:
        messagebox.showerror('error','Wrong matric number')
    elif b.get('password') != password2:
        messagebox.showerror('error','Wrong password')


    f.close()



def log1():
    global root2
    
    root2 = Toplevel(root)
    root2.title('Sign up')
    root2.geometry('300x200')
    root2.configure(bg = 'black')

    global matric_en2
    global password_en2

    matric_no2 = Label(root2, text = ' Enter your matric number:', fg ='brown',bg = 'black',font ='calibri 12 bold')
    matric_no2.place(x = 55, y = 10)
    matric_v = StringVar()
    matric_en2 = Entry(root2, textvariable = matric_v, width = 45)
    matric_en2.place(x = 10, y = 40)

    password_no2 = Label(root2, text = 'Password:', fg ='brown',bg = 'black',font ='calibri 12 bold')
    password_no2.place(x = 90, y = 70)
    password_v = StringVar()
    password_en2 = Entry( root2, textvariable = password_v,show = '*', width = 45)
    password_en2.place(x = 10, y = 100)

    submit = Button(root2, text = 'Submit', command = result2, fg ='brown',bg = 'black',font ='calibri 11 bold')
    submit.place(x = 80, y = 130)

    close = Button(root2, text = 'close', command = root.quit, fg ='brown',bg = 'black',font ='calibri 11 bold')
    close.place(x = 150, y = 130)


   


def result():
    global matric
    global password
    global sname
    global other
    global email
    global mobile
    global state
    global pass2
    global gender
    global count
    global namelist
    global dic
     

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

    if gender == 1:
        gender = "Male"
    elif gender == 2:
        gender = "Female"


    if password == pass2:
        # dic = {'matric': matric, 'surname': sname, 'other name': other,'email': email,'mobile number': mobile,'state': state,'password': password,'confirm password': pass2,'Gender': gender,'Country': count}
        # namelist = open('details.txt','a')
        # namelist.write(str(dic) + '\n')
        # namelist.close()
        
        
        result = '''
                        INSERT INTO acad(matricnumber,firstname,surnamename,othername,mobilenumber,state,country,email,gender,password,confirmpassword)
                        VALUES
                        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                 '''
        values = (matric,sname,other,email,mobile,state,password,pass2,gender,count)
        messagebox.showinfo('Sign up sucessful','Sign up completed,Log in')
        login2 = Button(frame, text = 'Login',command = lambda:[log1(),root1.withdraw()] , fg ='purple',bg = 'white',font ='calibri 11 bold')
        login2.place(x = 80, y = 510)

        matric_en.delete(0,END)
        surname_en.delete(0,END)
        other_en.delete(0,END)
        email_en.delete(0,END)
        mobile_en.delete(0,END)
        state_en.delete(0,END)
        password_en.delete(0,END)
        pass2_en.delete(0,END)
    
    else:
        messagebox.showerror('error','Has to be the same password')

        





def registration():
    root.withdraw()
    global root1
    global frame
    global matric_en
    global surname_en
    global other_en
    global email_en
    global mobile_en
    global state_en
    global password_en
    global pass2_en
    global gender_v
    global clicked

    global root1

    root1 = Toplevel(root)
    root1.title('Sign up')
    root1.geometry('600x700')
    root1.configure(bg = 'purple')

    heading = Label(root1, text = 'Student portal',font = 'times 35 bold', fg = 'purple', bg = 'white',padx =10)
    heading.place(x = 140, y = 6)

    frame = Frame(root1,padx = 100, bg = 'white',width = 400, height = 550)
    frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)



    title = Label(frame , text = 'Portal Registration',font='calibri 20 bold', fg = 'purple',bg = 'white')
    title.place(x = 20, y = 20)


    matric_no = Label(frame, text = 'Matric number*', fg ='purple',bg = 'white',font ='calibri 10 bold')
    matric_no.place(x = 0, y = 70)
    matric_v = StringVar()
    matric_en = Entry( frame, textvariable = matric_v )
    matric_en.place(x = 120, y = 70)

    surname_no = Label(frame, text = 'Surname*', fg ='purple',bg = 'white',font ='calibri 10 bold')
    surname_no.place(x = 0, y = 110)
    surname_v = StringVar()
    surname_en = Entry(frame, textvariable = surname_v)
    surname_en.place(x = 120, y = 110)

    other_no = Label(frame, text = 'Other names*', fg ='purple',bg = 'white',font ='calibri 10 bold')
    other_no.place(x = 0, y = 150)
    other_v = StringVar()
    other_en = Entry( frame, textvariable = other_v)
    other_en.place(x = 120, y = 150)

    email_no = Label(frame, text = 'Email*', fg ='purple',bg = 'white',font ='calibri 10 bold')
    email_no.place(x = 0, y = 190)
    email_v = StringVar()
    email_en = Entry( frame, textvariable = email_v)
    email_en.place(x = 120, y = 190)


    mobile_no = Label(frame, text = 'Mobile number*', fg ='purple',bg = 'white',font ='calibri 10 bold')
    mobile_no.place(x = 0, y = 230)
    mobile_v = StringVar()
    mobile_en = Entry( frame, textvariable = mobile_v)
    mobile_en.place(x = 120, y = 230)


    state_no = Label(frame, text = 'State of origin*', fg ='purple',bg = 'white',font ='calibri 10 bold')
    state_no.place(x = 0, y = 270)
    state_v = StringVar()
    state_en = Entry( frame, textvariable = state_v)
    state_en.place(x = 120, y = 270)

    gender_v = IntVar()
    gender_v.set(1)
    gender_name = Label(frame, text = 'Gender*', fg ='purple',bg = 'white',font ='calibri 10 bold')
    gender_name.place(x = 0, y = 310)
    genderLbl1 = Radiobutton(frame, text = 'male', variable = gender_v, value = 1)
    genderLbl1.place(x = 120, y = 310)
    genderLbl2 = Radiobutton(frame, text = 'female', variable = gender_v, value = 2)
    genderLbl2.place(x = 200, y = 310)

    country1 = Label(frame, text = 'Country*', fg ='purple',bg = 'white',font ='calibri 10 bold')
    country1.place(x = 0, y = 350)

    countryOpt = ['Nigeria','Ghana','Algeria','liberia','usa']
    clicked = StringVar()
    clicked.set('Nigeria')
    country = OptionMenu(frame,clicked,*countryOpt)
    country.place(x = 120, y = 350)

    password_no = Label(frame, text = 'Password*', fg ='purple',bg = 'white',font ='calibri 10 bold')
    password_no.place(x = 0, y = 390)
    password_v = StringVar()
    password_en = Entry( frame, textvariable = password_v,show = '*')
    password_en.place(x = 120, y = 390)


    pass2_no = Label(frame, text = 'Confirm password*', fg ='purple',bg = 'white',font ='calibri 10 bold')
    pass2_no.place(x = 0, y = 430)
    pass2_v = StringVar()
    pass2_en = Entry( frame, textvariable = pass2_v,show = '*')
    pass2_en.place(x = 120, y = 430)

    close = Button(frame, text = 'close', command = root.quit, fg ='purple',bg = 'white',font ='calibri 11 bold')
    close.place(x = 140, y = 470)

    submit = Button(frame, text = 'Submit',command = result , fg ='purple',bg = 'white',font ='calibri 11 bold')
    submit.place(x = 20, y = 470)


def main_screen():
    global root
    root = Tk()
    root.geometry('300x200')
    root.title('welcome page')
    root.configure(bg = 'red')
    welcome = Label(root, text = "WELCOME \n Wisdom's Unversity",bg = 'red', width = 300, height = 2,font ='calibri 15 bold' )
    welcome.pack()
    login1 = Button(root, text = 'Login',command = lambda:[log1(),root.withdraw()],bg = 'green', height = 2, width = 30)
    login1.pack(pady = 10) 
    sign_up1 = Button(root, text = 'Sign up', height = 2,bg = 'green', width = 30, command = registration)
    sign_up1.pack( pady = 10) 

    root.mainloop()

main_screen()
