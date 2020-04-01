import tkinter as tk
import os
import subprocess, sys
import ctypes, sys
import shlex
import tkinter.scrolledtext
import re
from tkinter import Tk
from tkinter import messagebox  
from tkinter import *
import ToDo
""""
########################################################################
TEST TEST TEST 
########################################################################
"""




""""
########################################################################
#TEST TEST TEST 
########################################################################
"""

class IORedirector(object):
    '''A general class for redirecting I/O to this Text widget.'''
    def __init__(self,text_area):
        self.text_area = text_area

class StdoutRedirector(IORedirector):
    '''A class for redirecting stdout to this Text widget.'''
    def write(self,str):
        self.text_area.write(str,False)

########################################################################
#TEST TEST TEST
########################################################################
"""

class RedirectText(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, text_ctrl):
        
        self.output = text_ctrl
        
    #----------------------------------------------------------------------
    def write(self, string):
        """"""
        self.output.insert(tkinter.END, string)
    



"""
"""This Asks for Admin Rights, Which will be needed to run some of the commands"""

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    print("we are admin")
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

"""Setting up the directory paths to use later on"""

parentDirectory = "C:\\Users\\Public\\"
directory = "ScriptsForPython"
    
fullDirectory = parentDirectory + directory
searchPath = fullDirectory + "\\SearchForUsers.ps1"
passwordResetPath = fullDirectory + "\\PasswordReset.ps1"

""" If path does not exist, then create it """

if not os.path.exists(fullDirectory):
    os.mkdir(fullDirectory)
else:
    print("The Directory Already Exists, WELCOME BACK :)")

#####################################################################################################

"""This is where I start building the forms"""

class SysAdminHelper(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        ##self = Tk()
        ##self.wm_iconbitmap(False, '/Resources/hrc.png')
        ##self.iconphoto(False, tk.PhotoImage(file='hrc.png'))
        ##self.iconbitmap('/hrc.ico')
        ##self.tk.call('wm', 'iconphoto', self._w, tk.PhotoImage(file='/Resources/hrc.png'))
        ##self.iconphoto(False, 'hrc.ico')
        ##self.iconbitmap("hrc.ico")
        self.iconbitmap(r'C:\PythonResources\hrc.ico')
        ##img = self.PhotoImage(file='hrc.ico')
        ##self.tk.call('wm', 'iconphoto', self._w, img)

       



        self.title("Making Workflow Easier :)")
        self.geometry("800x480")
        self._frame = None
        self.switch_frame(StartPage)
       
    
    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

  #####################################################################################################
    
""" This is my Home page, I am creating all the navigation buttons that will take you to the corresponding page"""
class StartPage(tk.Frame):
   
    def __init__(self,master):
        """   this is the "main frame from tkinter """
        tk.Frame.__init__(self,master)
        """this is the label on the front page"""
        tk.Label(self, text="What Can I Do For You?").pack(side="top", fill="x", pady=10)
        """Where I start defining my buttons"""
        nmapBtn = tk.Button(self, text="Search with Nmap",
                    command=lambda: master.switch_frame(NmapPage))
        passwordBtn = tk.Button(self, text="Reset User's Password",
                    command=lambda: master.switch_frame(PasswordPage))
        systemInfoBtn = tk.Button(self, text = "Run sysinfo on a machine",
                    command=lambda: master.switch_frame(systemInfoPage))
        toDoBtn = tk.Button(self, text = "To Do List",
                    command=lambda: master.switch_frame(ToDoPage))
        
        """running a command to get public IP address, and assigning it a variable"""

        publicIP = subprocess.check_output('curl \"http://myexternalip.com/raw\"')
        privateIP = subprocess.check_output('ipconfig | findstr /i \"ipv4\" ', shell=True)
        length = len(privateIP)
        numericPrivateIP = " ".join(re.split("[^0-9. ]*", str(privateIP)))
        shorterIP = numericPrivateIP[length -14 :]
        shortestIP = shorterIP[14:]


        ipLbl = tk.Label(self, text="This is your public IP Address").pack()
        tk.Label(self, text=publicIP).pack()
        tk.Label(self, text="This is your private IP Address").pack()
        tk.Label(self, text=shortestIP.replace(" ", "")).pack()

        """this is where I put the buttons in order"""
        passwordBtn.pack()
        systemInfoBtn.pack()
        nmapBtn.pack()
        toDoBtn.pack()
#####################################################################################################

"""My Nmap Page"""
class NmapPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        headerLbl = tk.Label(self, text="Alright, let's start searching the network!")
        searchBtn = tk.Button(self, text="Search")
        tk.Button(self, text="Go Home",
                    command=lambda: master.switch_frame(StartPage)).pack()

        headerLbl.pack(pady='5')
        searchBtn.pack(pady='5')

        myIp = subprocess.check_output('ipconfig | findstr /i \"ipv4\" ', shell=True)
        ipOutput = tk.Text(self)
        ipLabel = tk.Label(self, text="This is your current private IP Address")
        ipLabel.pack(pady='10')
        ipOutput.pack()
        ipOutput.insert(tk.END, myIp)

#####################################################################################################

"""Password Reset Page"""
class PasswordPage(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        mainText = "Password Reset Page"
        font = "Helvetica 20 bold"
        mainLbl = tk.Label(self,
                            text = mainText,
                            bg = "blue",
                            font = font).pack()
        headerLbl = tk.Label(self, text="Uh oh.. someone forgot their password! \n That's Alright. I can fix that XD")
        instructionsLbl = tk.Label(self, text= "Click the \"Lookup\" button after entering the name of the person you are working with",  pady="50")
        lookupBtn = tk.Button(self, text = "Lookup", 
                                command=lambda: master.switch_frame(LookupPage))
        homeBtn = tk.Button(self, text = "Go Home",
                                command=lambda: master.switch_frame(StartPage))

        """Arranging my buttons"""

        headerLbl.pack(pady='5')
        instructionsLbl.pack(pady='5')
        lookupBtn.pack(pady='5')
        homeBtn.pack(pady='5')

"""Inside Password Page, moving to the look up function"""
#####################################################################################################
class LookupPage(tk.Frame):
    def __init__(self, master):
       
        
        tk.Frame.__init__(self,master)
        mainText = "User Lookup"
        font= "Helvetica 20 bold"
        mainLbl = tk.Label(self,
                            text = mainText,
                            bg = "blue",
                            font = font).pack()
        headerLbl = tk.Label(self, text = "Type the name as close as you can \n If you aren't sure how to spell it just type the first few characters")
        self.lookupName = tk.Entry(self)
        homeBtn = tk.Button(self, text= "Go Home",
                            command=lambda: master.switch_frame(StartPage))
        submitBtn = tk.Button(self, text= "Submit",
                                command=self.on_button)
        ##scrollbar = tk.Scrollbar(self).pack(side="right", fill="y")

        
        


      

        headerLbl.pack(pady='5')
        self.lookupName.pack(pady='5')
        submitBtn.pack(pady='5')
        homeBtn.pack(pady='5')
 
        

    """assigning a variable for the inputted data"""
##---------------------------------------------------------------
    def on_button(self):
        userName = self.lookupName.get()
        print (userName)
        
        """using that variable (userName) to inject into PowerShell Command"""
##---------------------------------------------------------------
        with open(searchPath, "w") as file:
            file.write("$Name ='" + userName + "*'" + "\nGet-ADuser -Filter {name -like $Name} -Properties * | Select-Object name, samaccountname, emailaddress | Sort-Object samaccountname")

        """Calling PowerShell to open with the file that was just created"""
##---------------------------------------------------------------
        p1 = subprocess.check_output(['powershell.exe ', searchPath])
        ##stdout = p1.communicate()
        ##sys.stdout = StdoutRedirector(self)
        #write(stdout)
        self.text_box = tk.Text(self)
        self.text_box.pack()
        self.text_box.insert(tk.END, p1)
        #out_label = tk.Label("test").pack()




"""System Info Page"""
#####################################################################################################

class systemInfoPage(tk.Frame):


    def __init__(self,master):
        tk.Frame.__init__(self,master)
        mainText = "Run Systeminfo command on remote computer"
        font= "Helvetica 20 bold"
        mainLbl = tk.Label(self,
                            text = mainText,
                            bg = "blue",
                            font = font).pack(pady='5')
        
        tk.Label(self, text="What is the IP Address or Hostname of the machine you'd like a report on?").pack()

        """Creating a text input box to accept input from user and use later on"""
        ##---------------------------------------------------------------
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="test Entry",
                    command=self.on_button)
        homeBtn = tk.Button(self, text="Go Home",
                            command=lambda: master.switch_frame(StartPage))
        
        self.entry.pack(pady='5')
        self.button.pack(pady='5')
        homeBtn.pack(pady='5')

    def on_button(self):
        sysInfoMachine = self.entry.get()
        print(sysInfoMachine)
        """i = 0
        while i < 1:
            sysinfoCmd = os.system('cmd /k "systeminfo"')
            i + 1
            break
"""
        ##### systeminfo /s computername for remote computer
        cmd = subprocess.check_output('systeminfo')
        self.output = tk.Text(self)
        self.output.pack()
        self.output.insert(tk.END, cmd)
        print(cmd)




"""To Do Page"""
###################################################################################################

class ToDoPage(tk.Frame):
            
       
        tasks_list = [] 
  
        # global variable is declare for couting the task 
        counter = 1
            
        def inputError() : 
        
        # check for enter task field is empty or not 
            if enterTaskField.get() == "" : 
            
                # show the error message 
                messagebox.showerror("Input Error") 
            
                return 0
        
            return 1
        
        # Function for clearing the contents 
        # of task number text field 
        def clear_taskNumberField() : 
            
            # clear the content of task number text field 
            taskNumberField.delete(0.0, END) 
        
        # Function for clearing the contents 
        # of task entry field    
        def clear_taskField() : 
        
            # clear the content of task field entry box 
            enterTaskField.delete(0, END) 
            
        # Function for inserting the contents 
        # from the task entry field to the text area  
        def insertTask(): 
        
            global counter 
            
            # check for error 
            value = inputError() 
        
            # if error occur then return 
            if value == 0 : 
                return
        
            # get the task string concatenating 
            # with new line character 
            content = enterTaskField.get() + "\n"
        
            # store task in the list 
            tasks_list.append(content) 
        
            # insert content of task entry field to the text area 
            # add task one by one in below one by one 
            TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content) 
        
            # incremented 
            counter += 1
        
            # function calling for deleting the content of task field 
            clear_taskField() 
        
        # function for deleting the specified task 
        def delete() : 
            
            global counter 
            
            # handling the empty task error 
            if len(tasks_list) == 0 : 
                messagebox.showerror("No task") 
                return
        
            # get the task number, which is required to delete 
            number = taskNumberField.get(1.0, END) 
        
            # checking for input error when 
            # empty input in task number field 
            if number == "\n" : 
                messagebox.showerror("input error") 
                return
            
            else : 
                task_no = int(number) 
        
            # function calling for deleting the 
            # content of task number field 
            clear_taskNumberField() 
            
            # deleted specified task from the list 
            tasks_list.pop(task_no - 1) 
        
            # decremented  
            counter -= 1
            
            # whole content of text area widget is deleted 
            TextArea.delete(1.0, END) 
        
            # rewriting the task after deleting one task at a time 
            for i in range(len(tasks_list)) : 
                TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i]) 


             # create a GUI window 
        gui = Tk() 
    
        # set the background colour of GUI window  
        gui.configure(background = "light green") 
    
        # set the title of GUI window 
        gui.title("ToDo App") 
    
        # set the configuration of GUI window  
        gui.geometry("250x300") 
    
        # create a label : Enter Your Task 
        enterTask = tk.Label(gui, text = "Enter Your Task", bg = "light green") 
    
        # create a text entry box  
        # for typing the task 
        enterTaskField = tk.Entry(gui) 
    
        # create a Submit Button and place into the root window 
        # when user press the button, the command or  
        # function affiliated to that button is executed  
        Submit = tk.Button(gui, text = "Submit", fg = "Black", bg = "Red", command = insertTask) 
    
        # create a text area for the root 
        # with lunida 13 font 
        # text area is for writing the content 
        TextArea = tk.Text(gui, height = 5, width = 25, font = "lucida 13") 
    
        # create a label : Delete Task Number 
        taskNumber = tk.Label(gui, text = "Delete Task Number", bg = "blue") 
                            
        taskNumberField = tk.Text(gui, height = 1, width = 2, font = "lucida 13") 
    
        # create a Delete Button and place into the root window 
        # when user press the button, the command or  
        # function affiliated to that button is executed . 
        delete = tk.Button(gui, text = "Delete", fg = "Black", bg = "Red", command = delete) 
    
        # create a Exit Button and place into the root window 
        # when user press the button, the command or  
        # function affiliated to that button is executed . 
        Exit = tk.Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit) 
    
        # grid method is used for placing  
        # the widgets at respective positions  
        # in table like structure. 
        enterTask.grid(row = 0, column = 2) 
    
        # ipadx attributed set the entry box horizontal size                
        enterTaskField.grid(row = 1, column = 2, ipadx = 50) 
                            
        Submit.grid(row = 2, column = 2) 
            
        # padx attributed provide x-axis margin  
        # from the root window to the widget. 
        TextArea.grid(row = 3, column = 2, padx = 10, sticky = W) 
                            
        taskNumber.grid(row = 4, column = 2, pady = 5) 
                            
        taskNumberField.grid(row = 5, column = 2) 
    
        # pady attributed provide y-axis 
        # margin from the widget.                   
        delete.grid(row = 6, column = 2, pady = 5) 
                            
        Exit.grid(row = 7, column = 2) 
        gui.mainloop()


if __name__ == "__main__":

  
     

    app = SysAdminHelper()
    app.mainloop()
