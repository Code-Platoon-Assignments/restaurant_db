import tkinter as tk
from tkinter import ttk
from pairs.pairs import Pairs

LARGEFONT =("Verdana", 35)
LIST_FONT = ('Arial', 18)
pairs_interface = Pairs()

def listbox_insert_items_from_file(listbox):
        names = pairs_interface.include_list
        for index, line in enumerate(names):
            listbox.insert(index, line.strip())

class TeacherBot(tk.Tk):
	
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self)
		self.title('cp')
		container.pack(side = "top", fill = "both", expand = True)

		# container.grid_rowconfigure(0, weight = 1)
		# container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, Pairs_Page, Students_Page):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame startpage
class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		label = ttk.Label(self, text ="Instructor Bot", font = LARGEFONT)
		
		label.grid(row = 0, column = 0, padx = 10, pady = 10)

		tab_control = ttk.Notebook(self, height=300, width=300)
		tab1 = ttk.Frame(tab_control)
		tab2 = ttk.Frame(tab_control)
		tab_control.add(tab1, text='Tab 1')
		tab_control.add(tab2, text='Tab 2')		

		tab_control.grid(row = 0, column = 0, sticky ="nsew")

		ttk.Label(tab1, text='Welcome to GeeksForGeeks').grid(column=0, row=0, padx=30, pady=30)
		ttk.Label(tab2, text='Lets dive into the world of computers').grid(column=0, row=0, padx=30, pady=30)

		button1 = ttk.Button(self, text ="Page 1",
		command = lambda : controller.show_frame(Students_Page))

		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		button2 = ttk.Button(self, text ="Page 2",
		command = lambda : controller.show_frame(Pairs_Page))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)

		


# second window frame page1
class Students_Page(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Students Page", font = LARGEFONT)
		label.pack() #row = 0, column = 4, padx = 10, pady = 10


		# create left frame list with scroll
		include_list = tk.Listbox(self, selectmode=tk.MULTIPLE, font=LIST_FONT, height=40)
		
		listbox_insert_items_from_file(include_list)
		include_list.pack(side='left', fill=tk.BOTH)

		scrollbar = tk.Scrollbar(self)
		scrollbar.pack(side='right', fill=tk.BOTH)

		include_list.config(yscrollcommand=scrollbar.set)
		
		scrollbar.config(command=include_list.yview)
		
		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
	
		button1.pack()

		button2 = ttk.Button(self, text ="Pairs Page",
							command = lambda : controller.show_frame(Pairs_Page))
		
		button2.pack()




# third window frame page2
class Pairs_Page(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Pairs Page", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="Student page",
							command = lambda : controller.show_frame(Students_Page))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
		button2 = ttk.Button(self, text ="Startpage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)



# Driver Code
app = TeacherBot()
app.mainloop()
