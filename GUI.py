from tkinter import *
from tkinter.ttk import *


class Fixture:
    def __init__(self, master=None):
        self.master = master
        # Creating a canvas
        self.canvas = Canvas(self.master)

        # xxxxxxxxxxxxxxxxxxxxx ROW 1 xxxxxxxxxxxxxxxxxxxxx

        # ------------ ROUND 1 Fixtures ------------
        self.createFixtures(250, 10, 400, 10, "SRH", "CSK")  # 1 vs 2
        self.createFixtures(250, 80, 400, 80, "DC", "RCB")  # 3 vs 4
        self.createFixtures(250, 150, 400, 150, "PBKS", "MI")  # 5 vs 6
        self.createFixtures(250, 220, 400, 220, "RR", "KKR")  # 7 vs 8

        # ------------ ROUND 2 Fixtures ------------
        self.createFixtures(750, 10, 900, 10, 'RCB', 'CSK')  # 1 vs 2
        self.createFixtures(750, 80, 900, 80, 'SRH', 'MI')  # 3 vs 4
        self.createFixtures(750, 150, 900, 150, 'RCB', 'CSK')  # 5 vs 6
        self.createFixtures(750, 220, 900, 220, 'RCB', 'CSK')  # 7 vs 8

        # ------------ ROUND 3 Fixtures ------------
        self.createFixtures(1250, 10, 1400, 10, 'MI', 'CSK')  # 1 VS 2
        self.createFixtures(1250, 80, 1400, 80, 'MI', 'CSK')  # 3 VS 4
        self.createFixtures(1250, 150, 1400, 150, 'MI', 'CSK')  # 5 VS 6
        self.createFixtures(1250, 220, 1400, 220, 'MI', 'CSK')  # 7 VS 8

        # xxxxxxxxxxxxxxxxxxxxx ROW 2 xxxxxxxxxxxxxxxxxxxxx

        # ------------ ROUND 4 Fixtures ------------
        self.createFixtures(250, 360, 400, 360, 'MI', 'CSK')  # 1 VS 2
        self.createFixtures(250, 430, 400, 430, 'MI', 'CSK')  # 3 VS 4
        self.createFixtures(250, 500, 400, 500, 'MI', 'CSK')  # 5 VS 6
        self.createFixtures(250, 570, 400, 570, 'MI', 'CSK')  # 7 VS 8

        # ------------ ROUND 5 Fixtures ------------s
        self.createFixtures(750, 360, 900, 360, 'MI', 'CSK')  # 1 VS 2
        self.createFixtures(750, 430, 900, 430, 'MI', 'CSK')  # 3 VS 4
        self.createFixtures(750, 500, 900, 500, 'MI', 'CSK')  # 5 VS 6
        self.createFixtures(750, 570, 900, 570, 'MI', 'CSK')  # 7 VS 8

        # ------------ ROUND 6 Fixtures ------------s
        self.createFixtures(1250, 360, 1400, 360, 'MI', 'CSK')  # 1 VS 2
        self.createFixtures(1250, 430, 1400, 430, 'MI', 'CSK')  # 3 VS 4
        self.createFixtures(1250, 500, 1400, 500, 'MI', 'CSK')  # 5 VS 6
        self.createFixtures(1250, 570, 1400, 570, 'MI', 'CSK')  # 7 VS 8

        # xxxxxxxxxxxxxxxxxxxxx ROW 3 xxxxxxxxxxxxxxxxxxxxx

        # ------------ ROUND 7 Fixtures ------------
        self.createFixtures(750, 710, 900, 710, 'MI', 'CSK')  # 1 VS 2
        self.createFixtures(750, 780, 900, 780, 'MI', 'CSK')  # 3 VS 4
        self.createFixtures(750, 850, 900, 850, 'MI', 'CSK')  # 5 VS 6
        self.createFixtures(750, 920, 900, 920, 'MI', 'CSK')  # 7 VS 8

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
