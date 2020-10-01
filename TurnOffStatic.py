print("Status: Initializing...\n")
import tkinter as tk
from tkinter import ttk
import pyautogui as pag
from time import perf_counter


class StaticOff(tk.Tk):

	def __init__(self):
		super(StaticOff, self).__init__()
		self.title("Turn Off Static")
		self.minsize(310,90)
		self.create_layout()
		
	def create_layout(self):
		tk.Label(self, text = "Choose an Application:").pack(side = "top")
		apps = ["Chrome", "Microsoft Teams", "VLC media player", "RStudio",
				"Reader DC", "Word", "Tableau",	"Sublime Text"]
		self.combo_box = ttk.Combobox(self, value = apps)
		self.combo_box.current(0)
		self.combo_box.pack(side = "top")
		tk.Button(self, text = "TURN OFF STATIC",
			   command = self.static_off).pack(side = "top")
	
	def static_off(self):
		self.speaker = pag.Point(25, 933-35)
		app = self.combo_box.get()
		self.tab = pag.getWindowsWithTitle(app)
		self.tab[0].maximize()
		print(f"Status: {self.combo_box.get()}")
		self.automate()
		self.destroy()
		while True:
			if int(perf_counter())%22 == 0:
				self.automate()
			

	def automate(self):
		initial = pag.position()
		pag.moveTo(self.speaker, duration = 0.5)
		pag.rightClick(self.speaker)
		pag.write(['s','o'])
		self.tab[0].activate()
		pag.moveTo(initial, duration = 0.5)
	
so = StaticOff()
so.mainloop()
