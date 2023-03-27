import tkinter as tk
import tkinter.font as font
import sys
import os
import exHanoi

moves = []
status = "auto"
pause = False
delay = 2000


class ExHanoi(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Extended Hanoi")
        self.x1 = {"A": 260, "B": 790, "C": 1320}
        self.tower1_disks = []
        self.tower2_disks = []
        self.tower3_disks = []
        self.disks_in_tower = {"A": self.tower1_disks, "B": self.tower2_disks, "C": self.tower3_disks}
        self.disks_coords = []

        disk_size_t1 = {'x1': 10, 'y1': 700, 'x2': 530, 'y2': 720}
        disk_size_t2 = {'x1': 545, 'y1': 700, 'x2': 1055, 'y2': 720}
        disk_size_t3 = {'x1': 1080, 'y1': 700, 'x2': 1580, 'y2': 720}

        my_font = font.Font(family='Helvetica', size=10, weight="bold")

        # Canvas
        self.canvas = tk.Canvas(self, width=1600, height=900, bg="#B8E8FC")
        self.canvas.grid(row=1, column=0, padx=5, pady=5)
        # Towers
        self.canvas.create_rectangle(260, 150, 280, 720, fill="#B1AFFF", tags="Tower 1")
        self.canvas.create_rectangle(790, 150, 810, 720, fill="#B1AFFF", tags="Tower 2")
        self.canvas.create_rectangle(1320, 150, 1340, 720, fill="#B1AFFF", tags="Tower 3")

        self.canvas.create_rectangle(0, 720, 1600, 800, fill="#C8FFD4")
        frame = tk.Frame(master=self)
        frame.grid(row=0, column=0, padx=10, pady=10)
        # delay entry
        self.delay_entry = tk.Entry(frame, width=20, font=my_font)
        self.delay_entry.grid(row=0, column=1, padx=10)
        self.delay_entry.insert(0, 'delay')
        self.delay_entry.bind("<FocusIn>", lambda args: self.delay_entry.delete('0', 'end'))
        # disk entry
        self.disk_entry = tk.Entry(frame, width=20, font=my_font)
        self.disk_entry.grid(row=0, column=2, padx=10)
        self.disk_entry.insert(0, 'No of disks')
        self.disk_entry.bind("<FocusIn>", lambda args: self.disk_entry.delete('0', 'end'))

        def auto():
            global moves, pause, status, delay
            disks = int(self.disk_entry.get())
            show_disks(disks)
            if self.delay_entry.get() != "delay":
                print(self.delay_entry.get() + "000")
                delay = int(self.delay_entry.get() + "000")
            self.auto["state"] = "disabled"
            self.manual["state"] = "disabled"
            self.reset["state"] = "normal"
            self.final["state"] = "normal"
            self.pause["state"] = "normal"
            self.resume["state"] = "normal"
            moves = exHanoi.extended_hanoi("A", "B", "C", disks)
            status = "auto"
            self.after(delay, self.movement)

        def manual():
            global moves, status
            self.next["state"] = "normal"
            self.auto["state"] = "disabled"
            self.manual["state"] = "disabled"
            self.reset["state"] = "normal"
            self.final["state"] = "normal"
            disks = int(self.disk_entry.get())
            show_disks(disks)
            status = "manual"
            moves = exHanoi.extended_hanoi("A", "B", "C", disks)

        def reset():
            python = sys.executable
            os.execl(python, python, *sys.argv)

        def next_step():
            self.movement()

        def final():
            global status
            status = "final"
            for disk in self.tower1_disks:
                self.canvas.delete(disk)
            for disk in self.tower2_disks:
                self.canvas.delete(disk)
            for disk in self.tower3_disks:
                self.canvas.delete(disk)
            self.tower3_disks = []
            self.tower2_disks = []
            self.tower1_disks = []
            for disk_coords in self.disks_coords:
                n = self.x1["C"] - (disk_coords[2] - disk_coords[0] - 20) / 2
                m = self.x1["C"] + 20 + (disk_coords[2] - disk_coords[0] - 20) / 2
                bottom = 720 - ((len(self.tower3_disks) + 1) * 20)
                disk_coords[0] = n
                disk_coords[1] = bottom
                disk_coords[2] = m
                disk_coords[3] = bottom + 20
                self.tower3_disks.append(
                    self.canvas.create_rectangle(disk_coords[0], disk_coords[1], disk_coords[2], disk_coords[3],
                                                 fill="#F55353"))

        def pause():
            global pause
            pause = True
            self.pause["state"] = "disable"
            self.resume["state"] = "normal"

        def resume():
            global pause, moves, delay
            pause = False
            self.resume["state"] = "disable"
            self.pause["state"] = "normal"
            self.after(delay, self.movement)

        # Buttons

        # auto button
        self.auto = tk.Button(frame, text="Auto", command=auto, bg="#277BC0", fg="#FFFFFF", activebackground='#1E5DC0',
                              activeforeground="#FFFFFF", disabledforeground="#FFFFFF", width=6, font=my_font)
        self.auto.grid(row=0, column=3, padx=15)

        # manual button
        self.manual = tk.Button(frame, text="Manual", command=manual, bg="#379237", fg="#FFFFFF",
                                activebackground='#186B1E', activeforeground="#FFFFFF", disabledforeground="#FFFFFF",
                                width=6, font=my_font)
        self.manual.grid(row=0, column=4)

        # next button
        self.next = tk.Button(frame, text="Next Step", command=next_step, bg="#FECD70", fg="#FFFFFF",
                              activebackground='#F0B475', activeforeground="#FFFFFF", disabledforeground="#FFFFFF",
                              width=8, font=my_font)
        self.next.grid(row=0, column=5, padx=15)
        self.next["state"] = "disabled"

        # pause button
        self.pause = tk.Button(frame, text="Pause", command=pause, bg="#393E46", fg="#FFFFFF",
                               activebackground='#1F2226', activeforeground="#FFFFFF", disabledforeground="#FFFFFF",
                               width=6, font=my_font)
        self.pause.grid(row=0, column=6)
        self.pause["state"] = "disabled"

        # resume button
        self.resume = tk.Button(frame, text="Resume", command=resume, bg="#FD841F", fg="#FFFFFF",
                                activebackground='#CF6C19', activeforeground="#FFFFFF", disabledforeground="#FFFFFF",
                                width=6, font=my_font)
        self.resume.grid(row=0, column=7, padx=15)
        self.resume["state"] = "disabled"

        # final button
        self.final = tk.Button(frame, text="Final", command=final, bg="#7743DB", fg="#FFFFFF",
                               activebackground='#432C7A', activeforeground="#FFFFFF", disabledforeground="#FFFFFF",
                               width=6, font=my_font)
        self.final.grid(row=0, column=8)
        self.final["state"] = "disabled"

        # reset button
        self.reset = tk.Button(frame, text="Reset", command=reset, bg="#DC3535", fg="#FFFFFF",
                               activebackground='#B20600', activeforeground="#FFFFFF", disabledforeground="#FFFFFF",
                               width=6, font=my_font)
        self.reset.grid(row=0, column=9, padx=15)
        self.reset["state"] = "disabled"

        def show_disks(disks):
            # first tower
            for _ in range(disks):
                d1 = self.canvas.create_rectangle(disk_size_t1["x1"], disk_size_t1["y1"], disk_size_t1["x2"],
                                                  disk_size_t1["y2"], fill="#F55353")
                self.tower1_disks.append(d1)
                self.disks_coords.append(self.canvas.coords(d1))
                d2 = self.canvas.create_rectangle(disk_size_t2["x1"], disk_size_t2["y1"], disk_size_t2["x2"],
                                                  disk_size_t2["y2"], fill="#F55353")
                self.tower2_disks.append(d2)
                self.disks_coords.append(self.canvas.coords(d2))
                d3 = self.canvas.create_rectangle(disk_size_t3["x1"], disk_size_t3["y1"], disk_size_t3["x2"],
                                                  disk_size_t3["y2"], fill="#F55353")
                self.tower3_disks.append(d3)
                self.disks_coords.append(self.canvas.coords(d3))
                # change tower1 size
                disk_size_t1["x1"] += 15
                disk_size_t1["y1"] -= 20
                disk_size_t1["x2"] -= 15
                disk_size_t1["y2"] -= 20
                # change tower2 size
                disk_size_t2["x1"] += 15
                disk_size_t2["y1"] -= 20
                disk_size_t2["x2"] -= 15
                disk_size_t2["y2"] -= 20
                # change tower3 size
                disk_size_t3["x1"] += 15
                disk_size_t3["y1"] -= 20
                disk_size_t3["x2"] -= 15
                disk_size_t3["y2"] -= 20

    def movement(self):
        global moves, delay, status
        if not pause and len(moves) != 0:
            move = moves.pop(0)
            source, destination = move
            rect_coords = self.canvas.coords(self.disks_in_tower[source][-1])
            n = self.x1[destination] - (rect_coords[2] - rect_coords[0] - 20) / 2
            m = self.x1[destination] + 20 + (rect_coords[2] - rect_coords[0] - 20) / 2
            bottom = 720 - ((len(self.disks_in_tower[destination]) + 1) * 20)
            self.canvas.delete(self.disks_in_tower[source][-1])
            self.disks_in_tower[source].remove(self.disks_in_tower[source][-1])
            rect_coords[0] = n
            rect_coords[1] = bottom
            rect_coords[2] = m
            rect_coords[3] = bottom + 20
            self.disks_in_tower[destination].append(
                self.canvas.create_rectangle(rect_coords[0], rect_coords[1], rect_coords[2], rect_coords[3],
                                             fill="#F55353"))
            if status != "manual" and status != "final":
                self.after(delay, self.movement)


if __name__ == "__main__":
    ex_hanoi = ExHanoi()
    ex_hanoi.mainloop()
