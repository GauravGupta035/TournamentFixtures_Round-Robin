from tkinter import *
from tkinter.ttk import *


class Fixture:
    def __init__(self, master=None):
        self.master = master

        # Hard coded method for generating fixtures
        # self.create()

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

    def createFixtures(self, startX1, startY1, startX2, startY2, team1, team2):
        self.canvas = Canvas(self.master)
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

        self.canvas.pack(fill=BOTH, expand=True)

    # Hard code for generating fixtures
    def create(self):
        self.canvas = Canvas(self.master)

        # ---------------- ROUND 1 Fixtures --------------

        # Team No 1 vs Team No 2
        self.canvas.create_rectangle(
            250, 10, 350, 60, outline="black", width=2, fill="white")
        self.canvas.create_text(300, 35, fill="black",
                                text="SRH", font=("Poppins", 20))

        self.canvas.create_text(375, 35, fill="red",
                                text="vs", font=("Poppins", 15))

        self.canvas.create_rectangle(
            400, 10, 500, 60, outline="black", width=2, fill="white")
        self.canvas.create_text(450, 35, fill="black",
                                text="CSK", font=("Poppins", 20))

        # Team No 3 vs Team No 4
        self.canvas.create_rectangle(
            250, 80, 350, 130, outline="black", width=2, fill="white")
        self.canvas.create_text(300, 105, fill="black",
                                text="DC", font=("Poppins", 20))

        self.canvas.create_text(375, 105, fill="red",
                                text="vs", font=("Poppins", 15))

        self.canvas.create_rectangle(
            400, 80, 500, 130, outline="black", width=2, fill="white")
        self.canvas.create_text(450, 105, fill="black",
                                text="RCB", font=("Poppins", 20))

        # Team No 5 vs Team No 6
        self.canvas.create_rectangle(
            250, 150, 350, 200, outline="black", width=2, fill="white")
        self.canvas.create_text(300, 175, fill="black",
                                text="PBKS", font=("Poppins", 20))

        self.canvas.create_text(375, 175, fill="red",
                                text="vs", font=("Poppins", 15))

        self.canvas.create_rectangle(
            400, 150, 500, 200, outline="black", width=2, fill="white")
        self.canvas.create_text(450, 175, fill="black",
                                text="MI", font=("Poppins", 20))

        # Team No 7 vs Team No 8
        self.canvas.create_rectangle(
            250, 220, 350, 270, outline="black", width=2, fill="white")
        self.canvas.create_text(300, 245, fill="black",
                                text="RR", font=("Poppins", 20))

        self.canvas.create_text(375, 245, fill="red",
                                text="vs", font=("Poppins", 15))

        self.canvas.create_rectangle(
            400, 220, 500, 270, outline="black", width=2, fill="white")
        self.canvas.create_text(450, 245, fill="black",
                                text="KKR", font=("Poppins", 20))

        # ---------------- ROUND 2 Fixtures --------------

        # Team No 1 vs Team No 2
        self.canvas.create_rectangle(
            750, 10, 850, 60, outline="black", width=2, fill="white")
        self.canvas.create_text(800, 35, fill="black",
                                text="RCB", font=("Poppins", 20))

        self.canvas.create_text(875, 35, fill="red",
                                text="vs", font=("Poppins", 15))

        self.canvas.create_rectangle(
            900, 10, 1000, 60, outline="black", width=2, fill="white")
        self.canvas.create_text(950, 35, fill="black",
                                text="CSK", font=("Poppins", 20))

        # Team No 3 vs Team No 4
        self.canvas.create_rectangle(
            750, 80, 850, 130, outline="black", width=2, fill="white")
        self.canvas.create_text(800, 105, fill="black",
                                text="SRH", font=("Poppins", 20))

        self.canvas.create_text(875, 105, fill="red",
                                text="vs", font=("Poppins", 15))

        self.canvas.create_rectangle(
            900, 80, 1000, 130, outline="black", width=2, fill="white")
        self.canvas.create_text(950, 105, fill="black",
                                text="MI", font=("Poppins", 20))

        # Team No 5 vs Team No 6
        self.canvas.create_rectangle(
            750, 150, 850, 200, outline="black", width=2, fill="white")
        self.canvas.create_text(800, 175, fill="black",
                                text="DC", font=("Poppins", 20))

        self.canvas.create_text(870, 175, fill="red",
                                text="vs", font=("Poppins", 15))

        self.canvas.create_rectangle(
            900, 150, 1000, 200, outline="black", width=2, fill="white")
        self.canvas.create_text(950, 175, fill="black",
                                text="KKR", font=("Poppins", 20))

        # Team No 7 vs Team No 8
        self.canvas.create_rectangle(
            750, 220, 850, 270, outline="black", width=2, fill="white")
        self.canvas.create_text(800, 245, fill="black",
                                text="PBKS", font=("Poppins", 20))

        self.canvas.create_text(875, 245, fill="red",
                                text="vs", font=("Poppins", 15))

        self.canvas.create_rectangle(
            900, 220, 1000, 270, outline="black", width=2, fill="white")
        self.canvas.create_text(950, 245, fill="black",
                                text="RR", font=("Poppins", 20))

        # ---------------- ROUND 3 Fixtures --------------

        # Team No 1 vs Team No 2
        self.canvas.create_rectangle(
            250, 410, 350, 460, outline="black", width=2, fill="white")
        self.canvas.create_text(300, 443, fill="black",
                                text="MI", font=("Poppins", 20))

        self.canvas.create_text(375, 435, fill="red",
                                text="vs", font=("Poppins", 15))

        self.canvas.create_rectangle(
            400, 410, 500, 460, outline="black", width=2, fill="white")
        self.canvas.create_text(450, 435, fill="black",
                                text="CSK", font=("Poppins", 20))

        # Team No 3 vs Team No 4
        self.canvas.create_rectangle(
            250, 480, 350, 530, outline="black", width=2, fill="white")
        self.canvas.create_text(300, 505, fill="black",
                                text="RCB", font=("Poppins", 20))

        self.canvas.create_text(375, 505, fill="red",
                                text="vs", font=("Poppins", 15))

        self.canvas.create_rectangle(
            400, 480, 500, 530, outline="black", width=2, fill="white")
        self.canvas.create_text(450, 505, fill="black",
                                text="KKR", font=("Poppins", 20))

        # Team No 5 vs Team No 6
        self.canvas.create_rectangle(
            250, 550, 350, 600, outline="black", width=2, fill="white")
        self.canvas.create_text(300, 575, fill="black",
                                text="SRH", font=("Poppins", 20))

        self.canvas.create_text(375, 575, fill="red",
                                text="vs", font=("Poppins", 15))

        self.canvas.create_rectangle(
            400, 550, 500, 600, outline="black", width=2, fill="white")
        self.canvas.create_text(450, 575, fill="black",
                                text="RR", font=("Poppins", 20))

        # Team No 7 vs Team No 8
        self.canvas.create_rectangle(
            250, 620, 350, 670, outline="black", width=2, fill="white")
        self.canvas.create_text(300, 645, fill="black",
                                text="DC", font=("Poppins", 20))

        self.canvas.create_text(375, 645, fill="red",
                                text="vs", font=("Poppins", 15))

        self.canvas.create_rectangle(
            400, 620, 500, 670, outline="black", width=2, fill="white")
        self.canvas.create_text(450, 645, fill="black",
                                text="PBKS", font=("Poppins", 20))

        # ---------------- ROUND 4 Fixtures --------------

        # Team No 1 vs Team No 2
        self.canvas.create_rectangle(
            750, 410, 850, 460, outline="black", width=2, fill="white")
        self.canvas.create_text(800, 435, fill="black",
                                text="KKR", font=("Poppins", 20))

        self.canvas.create_text(875, 435, fill="red",
                                text="vs", font=("Poppins", 15))

        self.canvas.create_rectangle(
            900, 410, 1000, 460, outline="black", width=2, fill="white")
        self.canvas.create_text(950, 435, fill="black",
                                text="CSK", font=("Poppins", 20))

        # Team No 3 vs Team No 4
        self.canvas.create_rectangle(
            750, 480, 850, 530, outline="black", width=2, fill="white")
        self.canvas.create_text(800, 505, fill="black",
                                text="MI", font=("Poppins", 20))

        self.canvas.create_text(875, 505, fill="red",
                                text="vs", font=("Poppins", 15))

        self.canvas.create_rectangle(
            900, 480, 1000, 530, outline="black", width=2, fill="white")
        self.canvas.create_text(950, 505, fill="black",
                                text="RR", font=("Poppins", 20))

        # Team No 5 vs Team No 6
        self.canvas.create_rectangle(
            750, 550, 850, 600, outline="black", width=2, fill="white")
        self.canvas.create_text(800, 575, fill="black",
                                text="RCB", font=("Poppins", 20))

        self.canvas.create_text(870, 575, fill="red",
                                text="vs", font=("Poppins", 15))

        self.canvas.create_rectangle(
            900, 550, 1000, 600, outline="black", width=2, fill="white")
        self.canvas.create_text(950, 575, fill="black",
                                text="PBKS", font=("Poppins", 20))

        # Team No 7 vs Team No 8
        self.canvas.create_rectangle(
            750, 620, 850, 670, outline="black", width=2, fill="white")
        self.canvas.create_text(800, 645, fill="black",
                                text="SRH", font=("Poppins", 20))

        self.canvas.create_text(875, 645, fill="red",
                                text="vs", font=("Poppins", 15))

        self.canvas.create_rectangle(
            900, 620, 1000, 670, outline="black", width=2, fill="white")
        self.canvas.create_text(950, 645, fill="black",
                                text="DC", font=("Poppins", 20))

        self.canvas.pack(fill=BOTH, expand=True)


if __name__ == "__main__":
    master = Tk()
    fixture = Fixture(master)

    master.title('Tournament Fixtures')
    master.geometry("1920x1080")

    mainloop()
