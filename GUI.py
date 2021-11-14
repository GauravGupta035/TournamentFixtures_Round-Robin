from tkinter import *
import tkinter as tk
from tkinter.font import BOLD, ITALIC
from tkinter.ttk import *

from backend import sendData, schedule
l = sendData()
# print(l)


class Fixture:
    def __init__(self, master=None):
        self.master = master
        # Creating a canvas
        self.canvas = Canvas(self.master)

        # xxxxxxxxxxxxxxxxxxxxx ROW 1 xxxxxxxxxxxxxxxxxxxxx

        # ------------ ROUND 1 Fixtures ------------
        Team_one = tk.Label(master, text="Round One", width=10,
                            height=2, fg="Black", font=("Arial", 15, BOLD))
        Team_one.place(x=220, y=40)
        self.createFixtures(150, 100, 300, 100, l[0][0], l[0][1])  # 1 vs 2
        self.createFixtures(150, 170, 300, 170, l[1][0], l[1][1])  # 3 vs 4
        self.createFixtures(150, 240, 300, 240, l[2][0], l[2][1])  # 5 vs 6
        self.createFixtures(150, 310, 300, 310, l[3][0], l[3][1])  # 7 vs 8

        # ------------ ROUND 2 Fixtures ------------
        Team_two = tk.Label(master, text="Round Two", width=10,
                            height=2, fg="Black", font=("Arial", 15, BOLD))
        Team_two.place(x=620, y=40)
        self.createFixtures(560, 170, 710, 170, l[5][0], l[5][1])  # 3 vs 4
        self.createFixtures(560, 240, 710, 240, l[6][0], l[6][1])  # 5 vs 6
        self.createFixtures(560, 100, 710, 100, l[4][0], l[4][1])  # 1 vs 2
        self.createFixtures(560, 310, 710, 310, l[7][0], l[7][1])  # 7 vs 8

        # ------------ ROUND 3 Fixtures ------------
        Team_three = tk.Label(master, text="Round Three", width=10,
                              height=2, fg="Black", font=("Arial", 15, BOLD))
        Team_three.place(x=1060, y=40)
        self.createFixtures(990, 100, 1140, 100, l[8][0], l[8][1])  # 1 VS 2
        self.createFixtures(990, 170, 1140, 170, l[9][0], l[9][1])  # 3 VS 4
        self.createFixtures(990, 240, 1140, 240, l[10][0], l[10][1])  # 5 VS 6
        self.createFixtures(990, 310, 1140, 310, l[11][0], l[11][1])  # 7 VS 8

        # ------------ ROUND 4 Fixtures ------------
        Team_four = tk.Label(master, text="Round Four", width=10,
                             height=2, fg="Black", font=("Arial", 15, BOLD))
        Team_four.place(x=1420, y=40)
        self.createFixtures(1350, 100, 1500, 100, l[12][0], l[12][1])  # 1 VS 2
        self.createFixtures(1350, 170, 1500, 170, l[13][0], l[13][1])  # 3 VS 4
        self.createFixtures(1350, 240, 1500, 240, l[14][0], l[14][1])  # 5 VS 6
        self.createFixtures(1350, 310, 1500, 310, l[15][0], l[15][1])  # 7 VS 8

        # xxxxxxxxxxxxxxxxxxxxx ROW 2 xxxxxxxxxxxxxxxxxxxxx

        # ------------ ROUND 5 Fixtures ------------s
        Team_five = tk.Label(master, text="Round Five", width=10,
                             height=2, fg="Black", font=("Arial", 15, BOLD))
        Team_five.place(x=380, y=440)
        self.createFixtures(300, 500, 450, 500, l[16][0], l[16][1])  # 1 VS 2
        self.createFixtures(300, 570, 450, 570, l[17][0], l[17][1])  # 3 VS 4
        self.createFixtures(300, 640, 450, 640, l[18][0], l[18][1])  # 5 VS 6
        self.createFixtures(300, 710, 450, 710, l[19][0], l[19][1])  # 7 VS 8

        # ------------ ROUND 6 Fixtures ------------s
        Team_six = tk.Label(master, text="Round Six", width=10,
                            height=2, fg="Black", font=("Arial", 15, BOLD))
        Team_six.place(x=770, y=440)
        self.createFixtures(700, 500, 850, 500, l[20][0], l[20][1])  # 1 VS 2
        self.createFixtures(700, 570, 850, 570, l[21][0], l[21][1])  # 3 VS 4
        self.createFixtures(700, 640, 850, 640, l[22][0], l[22][1])  # 5 VS 6
        self.createFixtures(700, 710, 850, 710, l[23][0], l[23][1])  # 7 VS 8

        # ------------ ROUND 7 Fixtures ------------

        Team_seven = tk.Label(master, text="Round Seven", width=10,
                              height=2, fg="Black", font=("Arial", 15, BOLD))
        Team_seven.place(x=1160, y=440)
        self.createFixtures(1100, 500, 1250, 500, l[24][0], l[24][1])  # 1 VS 2
        self.createFixtures(1100, 570, 1250, 570, l[25][0], l[25][1])  # 3 VS 4
        self.createFixtures(1100, 640, 1250, 640, l[26][0], l[26][1])  # 5 VS 6
        self.createFixtures(1100, 710, 1250, 710, l[27][0], l[27][1])  # 7 VS 8
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
