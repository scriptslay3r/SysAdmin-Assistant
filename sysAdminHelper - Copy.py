import tkinter as tk
import os


""" This is something I am testing to get input from pages. (such as the IP address of a machine or name of user that needs password reset)"""


def switch_frame(self, frame_class):
    """Destroys current frame and replaces it with a new one."""
    new_frame = frame_class(self)
    if self._frame is not None:
        self._frame.destroy()
    self._frame = new_frame
    self._frame.pack()




if __name__ == "__main__":
    class SysAdminHelper(tk.Tk):
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)
            self.title("Making Workflow Easier :)")
            self.geometry("800x480")
            self._frame = None
            self.switch_frame(StartPage)

class StartPage(tk.Frame):
    """ This is my Home page, I am creating all the navigation buttons that will take you to the corresponding page"""
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
        """this is where I put the buttons in order"""

        passwordBtn.pack()
        systemInfoBtn.pack()
        nmapBtn.pack()

"""My Nmap Page"""
class NmapPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        tk.Label(self, text="Alright, let's start searching the network!").pack()
        tk.Button(self, text="Search")
        tk.Button(self, text="Go Home",
                    command=lambda: master.switch_frame(StartPage)).pack()

"""Password Reset Page"""
class PasswordPage(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        tk.Label(self, text="Uh oh.. someone forgot their password! \n That's Alright. I can fix that XD").pack()


"""System Info Page"""
class systemInfoPage(tk.Frame):


    def __init__(self,master):
        tk.Frame.__init__(self,master)
        tk.Label(self, text="What is the IP Address or Hostname of the machine you'd like a report on?").pack()
        e1 = tk.Entry(self).pack()
        ##results = tk.Entry(self).get()
        ##print(e1)
        #e2 = tk.Entry(self).pack()
        tk.Button(self, text="test Entry",
                    command= tk.Entry(self).get()).pack()