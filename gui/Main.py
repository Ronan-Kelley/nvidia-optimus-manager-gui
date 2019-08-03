#!/usr/bin/python3
from tkinter import Tk, Button, Label, Message, N, W, E, S
import subprocess

class OptimusGui():
    def __init__(self, master):
        self.master = master
        master.title("Optimus Manager Gui")

        self.warning_label = Label(master, text="changing graphics configuration requires this to be run as root!")
        self.warning_label.grid(row=2, column=1, columnspan=3)

        self.status_output = Message(master, text="getting status...")
        self.status_output.grid(columnspan=2, row=1, column=1)

        self.intel_button = Button(master, text="use intel graphics", command=lambda: self.swapGraphics("intel"))
        self.intel_button.grid(row=3, column=1)

        self.hybrid_button = Button(master, text="use hybrid graphics", command=lambda: self.swapGraphics("hybrid"))
        self.hybrid_button.grid(row=3, column=2)

        self.nvidia_button = Button(master, text="use nvidia graphics", command=lambda: self.swapGraphics("nvidia"))
        self.nvidia_button.grid(row=3, column=3)

        self.quit_button = Button(master, text="quit", command=master.quit)
        self.quit_button.grid(row=4,column=3)

        self.updateStatus()

    def swapGraphics(self, swap_val):
        if swap_val == "intel":
            # print("swapping to intel!")
            subprocess.run(["nvidia-optimus-manager", "configure", "intel"])
        elif swap_val == "hybrid":
            # print("swapping to hybrid!")
            subprocess.run(["nvidia-optimus-manager", "configure", "hybrid"])
        elif swap_val == "nvidia":
            # print("swapping to nvidia!")
            subprocess.run(["nvidia-optimus-manager", "configure", "nvidia"])
        else:
            print("invalid argument for swapGraphics!")
        
        self.updateStatus()

    def updateStatus(self):
        print("updating status!")
        output = subprocess.check_output(["nvidia-optimus-manager", "status"], encoding="ascii")
        self.status_output.configure(text=output)

root = Tk()
optimus_gui = OptimusGui(root)
root.geometry("430x200")
root.mainloop()

print("running!")