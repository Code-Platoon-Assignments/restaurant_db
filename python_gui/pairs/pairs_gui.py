import tkinter as tk
from tkinter import ttk
from pairs import Pairs
import random

LIST_FONT = ('Arial', 18)
pairs_interface = Pairs()

def listbox_insert_items_from_file(listbox):
        names = pairs_interface.include_list
        for index, line in enumerate(names):
            listbox.insert(index, line.strip())


def sort_list(listbox1):
    """
    function to sort listbox items case insensitive
    """
    temp_list = list(listbox1.get(0, tk.END))
    temp_list.sort(key=str.lower)

    listbox1.delete(0, tk.END)
    for item in temp_list:
        listbox1.insert(tk.END, item)


def move_item_to_include_list(evt):
    global include_list

    list = evt.widget
    for item in list.curselection():
        index = item
        value = evt.widget.get(index)

        include_list.insert(index, value)
        sort_list(include_list)
        list.delete(index)


def move_item_to_dnt_include_list(evt):
    global dnt_include_list

    list = evt.widget
    for item in list.curselection():
        index = item
        value = evt.widget.get(index)
        print(index)

        dnt_include_list.insert(tk.END, value)
        sort_list(dnt_include_list)
        list.delete(index)
# -------------------------------------------------------- #



# create a root window (top level element)
root = tk.Tk()
root.title('CP')
root.geometry('1300x1200')

# print(window.configure().keys())
label = ttk.Label(root, text="Generate pairs", font=('Arial', 20))
label.pack()

# create a frame (container)
body = ttk.Frame(root)
body.pack(fill='both')  # place the frame onto the window

left_frame = ttk.Frame(body)
left_frame.grid(row='0', column='0', padx=40, pady=10)

right_frame = ttk.Frame(body)
right_frame.grid(row='0', column='1', padx=40, pady=10 )

results_frame = ttk.Frame(body)
results_frame.grid(row='0', column='2', padx=40, pady=10)


# create left frame list with scroll
include_list = tk.Listbox(
    left_frame, selectmode=tk.MULTIPLE, font=LIST_FONT, height=40)
listbox_insert_items_from_file(include_list)
include_list.pack(side='left', fill=tk.BOTH)

scrollbar = tk.Scrollbar(left_frame)
scrollbar.pack(side='right', fill=tk.BOTH)

include_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=include_list.yview)



# create right frame list with scroll
dnt_include_list = tk.Listbox(
    right_frame, selectmode=tk.MULTIPLE,  font=LIST_FONT, height=40)
dnt_include_list.pack()

scrollbar = tk.Scrollbar(right_frame)
scrollbar.pack(side='right', fill=tk.BOTH)

dnt_include_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=dnt_include_list.yview)

include_list.bind('<<ListboxSelect>>', move_item_to_dnt_include_list)
dnt_include_list.bind('<<ListboxSelect>>', move_item_to_include_list)


# create results pane
text_area = tk.Text(results_frame, wrap = tk.WORD, width = 40,height = 40, font = ("Times New Roman", 15))
text_area.pack()


def generate_pairs():

    list_to_include = list(include_list.get(0, tk.END))
    random.shuffle(list_to_include)
    text = pairs_interface.generate_pairs(list_to_include)
    text_area.delete(1.0, tk.END)
    text_area.insert(1.0, text)

button = ttk.Button(results_frame, text='generate pairs', command=generate_pairs)
button.pack()

def send_to_slack():
    generate_pairs()
    pairs_interface.send_pairs_to_slack()

button = ttk.Button(results_frame, text='send pairs to slack', command=send_to_slack)
button.pack()

# create bottom footer
bottom_frame = ttk.Frame(root)
bottom_frame.pack()

quit_button = ttk.Button(bottom_frame, text="Quit", command=root.destroy)
quit_button.pack()


# a = tk.Label(frame, text="hello there").pack()


root.mainloop()
