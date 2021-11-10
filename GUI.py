from tkinter import *
import tkinter as tk
from tkinter.font import BOLD, ITALIC
from tkinter.ttk import *



class Fixture:
    def __init__(self, master=None):
        self.master = master
        # Creating a canvas
        self.canvas = Canvas(self.master)
        

        # xxxxxxxxxxxxxxxxxxxxx ROW 1 xxxxxxxxxxxxxxxxxxxxx

        # ------------ ROUND 1 Fixtures ------------
        Team_one= tk.Label(master,text="Round One",width=10,height=2,fg="Black",font=("Arial",15,BOLD))
        Team_one.place(x=120,y=40)
        self.createFixtures(50, 100, 200, 100, "SRH", "CSK")  # 1 vs 2
        self.createFixtures(50, 170, 200, 170, "DC", "RCB")  # 3 vs 4
        self.createFixtures(50, 240, 200, 240, "PBKS", "MI")  # 5 vs 6
        self.createFixtures(50, 310, 200, 310, "RR", "KKR")  # 7 vs 8

        # ------------ ROUND 2 Fixtures ------------
        Team_two= tk.Label(master,text="Round Two",width=10,height=2,fg="Black",font=("Arial",15,BOLD))
        Team_two.place(x=520,y=40)
        self.createFixtures(460, 100, 610, 100, 'RCB', 'CSK')  # 1 vs 2
        self.createFixtures(460, 170, 610, 170, 'SRH', 'MI')  # 3 vs 4
        self.createFixtures(460, 240, 610, 240, 'RCB', 'CSK')  # 5 vs 6
        self.createFixtures(460, 310, 610, 310, 'RCB', 'CSK')  # 7 vs 8

        # ------------ ROUND 3 Fixtures ------------
        Team_three= tk.Label(master,text="Round Three",width=10,height=2,fg="Black",font=("Arial",15,BOLD))
        Team_three.place(x=960,y=40)
        self.createFixtures(890, 100, 1040, 100, 'MI', 'CSK')  # 1 VS 2
        self.createFixtures(890, 170, 1040, 170, 'MI', 'CSK')  # 3 VS 4
        self.createFixtures(890, 240, 1040, 240, 'MI', 'CSK')  # 5 VS 6
        self.createFixtures(890, 310, 1040, 310, 'MI', 'CSK')  # 7 VS 8

        
        # ------------ ROUND 4 Fixtures ------------
        Team_four= tk.Label(master,text="Round Four",width=10,height=2,fg="Black",font=("Arial",15,BOLD))
        Team_four.place(x=1320,y=40)
        self.createFixtures(1250, 100, 1400, 100, 'MI', 'CSK')  # 1 VS 2
        self.createFixtures(1250, 170, 1400, 170, 'MI', 'CSK')  # 3 VS 4
        self.createFixtures(1250, 240, 1400, 240, 'MI', 'CSK')  # 5 VS 6
        self.createFixtures(1250, 310, 1400, 310, 'MI', 'CSK')  # 7 VS 8

        # xxxxxxxxxxxxxxxxxxxxx ROW 2 xxxxxxxxxxxxxxxxxxxxx



        # ------------ ROUND 5 Fixtures ------------s
        Team_five= tk.Label(master,text="Round Five",width=10,height=2,fg="Black",font=("Arial",15,BOLD))
        Team_five.place(x=280,y=440)
        self.createFixtures(200, 500, 350, 500, 'MI', 'CSK')  # 1 VS 2
        self.createFixtures(200, 570, 350, 570, 'MI', 'CSK')  # 3 VS 4
        self.createFixtures(200, 640, 350, 640, 'MI', 'CSK')  # 5 VS 6
        self.createFixtures(200, 710, 350, 710, 'MI', 'CSK')  # 7 VS 8

        # ------------ ROUND 6 Fixtures ------------s
        Team_six= tk.Label(master,text="Round Six",width=10,height=2,fg="Black",font=("Arial",15,BOLD))
        Team_six.place(x=670,y=440)
        self.createFixtures(600, 500, 750, 500, 'MI', 'CSK')  # 1 VS 2
        self.createFixtures(600, 570, 750, 570, 'MI', 'CSK')  # 3 VS 4
        self.createFixtures(600, 640, 750, 640, 'MI', 'CSK')  # 5 VS 6
        self.createFixtures(600, 710, 750, 710, 'MI', 'CSK')  # 7 VS 8

        # ------------ ROUND 7 Fixtures ------------

        Team_seven= tk.Label(master,text="Round Seven",width=10,height=2,fg="Black",font=("Arial",15,BOLD))
        Team_seven.place(x=1060,y=440)
        self.createFixtures(1000, 500, 1150, 500, 'MI', 'CSK')  # 1 VS 2
        self.createFixtures(1000, 570, 1150, 570, 'MI', 'CSK')  # 3 VS 4
        self.createFixtures(1000, 640, 1150, 640, 'MI', 'CSK')  # 5 VS 6
        self.createFixtures(1000, 710, 1150, 710, 'MI', 'CSK')  # 7 VS 8
        self.canvas.pack(fill=BOTH, expand=True)

    def createFixtures(self, startX1, startY1, startX2, startY2, team1, team2):

        # First team text and background
        self.canvas.create_rectangle(
            startX1, startY1, startX1 + 100, startY1 + 50, outline="black", width=2, fill="white")
        self.canvas.create_text(
            startX1 + 50, startY1 + 25, fill="black", text=team1, font=("Poppins", 20))
        

        # VS text
        self.canvas.create_text(
            startX1 + 125, startY1 + 25, fill="red", text="vs", font=("Poppins", 20))

        # Second team text and background
        self.canvas.create_rectangle(
            startX2, startY2, startX2 + 100, startY2 + 50, outline="black", width=2, fill="white")
        self.canvas.create_text(
            startX2 + 50, startY2 + 25, fill="black", text=team2, font=("Poppins", 20))


if __name__ == "__main__":
    master = Tk()
    scrollbar = Scrollbar(master)
    scrollbar.pack(side=RIGHT, fill=Y)
    fixture = Fixture(master)

    master.title('Tournament Fixtures')
    master.geometry("1920x1080")


    mainloop()
