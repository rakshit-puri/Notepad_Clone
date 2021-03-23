# This is Notepad Clone by skate1512
# It is not a licensed copy and is for educational purpose only
# Commercial use of this notepad is illegal and I am not responsible for any action taken against the user
# I tried to make this as similar as I could to the original Microsoft Notepad

import datetime
import os
from tkinter.font import families
import tkinter.messagebox as msg
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import re
from urlib.parse import quote

font_tuple = "Arial 14"
font_now = "Arial"
font_style_now = "normal"
font_size_now = 14
goto_open = False


# When X button is pressed
def on_closing():
    result = msg.askyesnocancel("Quit", "Do you want to save this file and exit?")
    if result:
        save_as_file()
        root.destroy()

    elif result is not None:
        root.destroy()


# To delete the recent text and open as a new window
def new_file(event = None):
    global file
    root.title("Untitled - Notepad")
    file = None
    # Delete everything from Line 1 Character 0 till the end
    text_area.delete(1.0, END)


# To open an independent instance of Notepad (another window)
def new_window(event = None):
    os.startfile("notepad.pyw")


# Implementation of font menu
def font_window(event = None):
    def save_config():
        global font_now
        global font_size_now
        global font_style_now

        font_now = font_name.get()
        font_size_now = size.get()
        font_style_now = style.get()
        text_area.config(font = (font_now, font_size_now, font_style_now))

        f.destroy()

    def change_font():
        global font_now
        font_now = font_name.get()

    def change_size():
        global font_size_now
        font_size_now = size.get()

    def change_style():
        global font_style_now
        font_style_now = style.get()

    f = Toplevel()
    f.title("Font")
    f.iconbitmap(default = 'transparent.ico')
    Label(f, text = "Font:").grid(row = 0, column = 0, columnspan = 2, padx = 5, sticky = W)
    font_list = tuple(families())
    font_name = StringVar()
    font_menu = ttk.Combobox(f, width = 20, textvariable = font_name, state = "readonly")
    font_menu['values'] = font_list
    font_menu.current(font_list.index(font_now))
    font_menu.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = W)
    font_menu.bind("<<Combobox>>", change_font)

    Label(f, text = "Font Style:").grid(row = 0, column = 2, padx = 5, sticky = W)
    font_s = tuple(["normal", "bold", "italic"])
    style = StringVar()
    font_style = ttk.Combobox(f, width = 10, textvariable = style, state = "readonly")
    font_style['values'] = font_s
    font_style.current(font_s.index(font_style_now))
    font_style.grid(row = 2, column = 2, columnspan = 1, padx = 5, pady = 5, sticky = W)
    font_style.bind("<<Combobox>>", change_style)

    Label(f, text = "Size:").grid(row = 0, column = 3, padx = 5, sticky = W)
    font_ = tuple(range(8, 74, 2))
    size = IntVar()
    font_size = ttk.Combobox(f, width = 10, textvariable = size, state = "readonly")
    font_size['values'] = font_
    font_size.current(font_.index(font_size_now))
    font_size.grid(row = 2, column = 3, columnspan = 1, padx = 5, pady = 5, sticky = W)
    font_size.bind("<<Combobox>>", change_size)

    Button(f, text = "   OK   ", command = save_config).grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "ew")
    Button(f, text = "Cancel", command = f.destroy).grid(row = 3, column = 3, padx = 5, pady = 5, sticky = "ew")


# To open text based files in Notepad Clone
def open_file(event = None):
    global file
    file = askopenfilename(defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Document", "*.txt"),
                                                                   ("Python Script", "*.py")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        text_area.delete(1.0, END)
        f = open(file, "r")
        text_area.insert(1.0, f.read())


# To save the current file
def save_file(event = None):
    global file
    if file is None:
        file = asksaveasfilename(initialfile = "Untitled.txt", defaultextension = ".txt",
                                 filetypes = [("All Files", "*.*"), ("Text Document", "*.txt"),
                                              ("Python Script", "*.py")])
        if file != "":
            f = open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")

        else:
            file = None

    else:
        f = open(file, "w")
        f.write(text_area.get(1.0, END))
        f.close()
        root.title(os.path.basename(file) + " - Notepad")


# To save the current file as .txt file or any other text based file(example: .py)
def save_as_file(event = None):
    global file
    if file is None:
        file = asksaveasfilename(initialfile = "Untitled.txt", defaultextension = ".txt",
                                 filetypes = [("All Files", "*.*"), ("Text Document", "*.txt"),
                                              ("Python Script", "*.py")])

        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")

    else:
        file = asksaveasfilename(initialfile = "Untitled.txt", defaultextension = ".txt",
                                 filetypes = [("All Files", "*.*"), ("Text Document", "*.txt"),
                                              ("Python Script", "*.py")])
        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(text_area.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")


# Implementation of cut command
def cut():
    text_area.event_generate("<<Cut>>")


# Implementation of copy command
def copy():
    text_area.event_generate("<<Copy>>")


# Implementation of paste command
def paste():
    text_area.event_generate("<<Paste>>")


# Implementation of undo command
def undo():
    text_area.event_generate("<<Undo>>")


# Implementation of delete command
def delete(event = None):
    text_area.delete(INSERT, INSERT + "+1c")


# To get the index for find/replace functions
def get_index(index):
    return tuple(map(int, str.split(index, ".")))


# Implementation of Find command
def find(event = None):
    def find_text():
        search_string = e.get()

        if no_case_match.get():
            match_case = False
        else:
            match_case = True

        if direction.get():
            row, col = get_index(text_area.index(INSERT))
            beg_col = str(col - len(search_string))
            beg_location = str(str(row) + '.' + beg_col)
            location = text_area.search(search_string, text_area.index(beg_location), backwards = True, nocase = match_case)
        else:
            location = text_area.search(search_string, text_area.index(INSERT), nocase = match_case)

        if location != '':
            prior_search = search_string

            row, col = get_index(location)
            end_col = str(col + len(search_string))
            end_location = str(str(row) + '.' + end_col)

            text_area.mark_set("insert", end_location)
            text_area.see("insert")
            text_area.tag_remove('sel', "1.0", END)
            text_area.tag_raise("sel")
            text_area.tag_add('sel', location, end_location)
            text_area.focus()
        else:
            print("Not found")

    #  Interface of Find
    top = Toplevel()
    top.title("Find")
    top.iconbitmap(default = 'transparent.ico')
    Label(top, text = "Find what:").grid(row = 0, column = 0, padx = 5, sticky = W)
    e = Entry(top, width = 28)
    e.bind("<Return>", find_text)
    e.grid(row = 0, column = 1, columnspan = 2, padx = 5, pady = 5)

    find_button = Button(top, text = "  Find Next  ", command = find_text).grid(row = 0, column = 4, padx = 10,
                                                                                pady = 2, sticky = "ew")
    cancel_button = Button(top, text = "  Cancel  ", command = top.destroy).grid(row = 1, column = 4, padx = 10,
                                                                                 pady = 2, sticky = "ew")
    no_case_match = BooleanVar()
    no_case_match.set(False)
    match_case = Checkbutton(top, text = 'Match case', variable = no_case_match)
    match_case.grid(row = 1, column = 0, sticky = "sw", padx = 5, pady = 10, columnspan = 2)

    direction = BooleanVar()
    direction.set(False)
    direction_box = LabelFrame(top, text = 'Direction')
    direction_box.grid(row = 2, column = 2, sticky = 'ne', pady = (0, 10))

    up_button = Radiobutton(direction_box, text = 'Up', variable = direction, value = True)
    up_button.grid(row = 1, column = 0, padx = 5)

    down_button = Radiobutton(direction_box, text = 'Down', variable = direction, value = False)
    down_button.grid(row = 1, column = 1, padx = (0, 5))


# Implementation of Replace command
def replace(event = None):
    direction = BooleanVar()
    direction.set(False)
    no_case_match = BooleanVar()
    no_case_match.set(False)
    prior_search = ""

    # Implementation of Find Next button
    def find_next():
        nonlocal prior_search
        search_string = e.get()

        if no_case_match.get():
            match_case = False
        else:
            match_case = True

        if direction.get():
            row, col = get_index(text_area.index(INSERT))
            beg_col = str(col - len(search_string))
            beg_location = str(str(row) + '.' + beg_col)
            location = text_area.search(search_string, text_area.index(beg_location), backwards=True, nocase=match_case)

        else:
            location = text_area.search(search_string, text_area.index(INSERT), nocase=match_case)

        if location != '':
            prior_search = search_string
            row, col = get_index(location)
            end_col = str(col + len(search_string))
            end_location = str(str(row) + '.' + end_col)

            text_area.mark_set("insert", end_location)
            text_area.see("insert")
            text_area.tag_remove('sel', "1.0", END)
            text_area.tag_raise("sel")
            text_area.tag_add('sel', location, end_location)
            text_area.focus()
        else:
            pass

    # Implementation of Replace All button
    def replace_all():
        new = re.sub(e.get(), rep.get(), text_area.get(1.0, END))
        text_area.delete(1.0, END)
        text_area.insert(1.0, new)

    # Implementation of Replace Next button
    def replace_next():
        def f():
            search_string = e.get()
            if no_case_match.get():
                match_case = False
            else:
                match_case = True

            if direction.get():
                row, col = get_index(text_area.index(INSERT))
                beg_col = str(col - len(search_string))
                beg_location = str(str(row) + '.' + beg_col)
                location = text_area.search(search_string, text_area.index(beg_location), backwards = True,
                                            nocase = match_case)
            else:
                location = text_area.search(search_string, text_area.index(INSERT), nocase = match_case)

            if location != '':
                prior_search = search_string

                row, col = get_index(location)
                end_col = str(col + len(search_string))
                end_location = str(str(row) + '.' + end_col)

                text_area.mark_set("insert", end_location)
                text_area.see("insert")
                text_area.tag_remove('sel', "1.0", END)
                text_area.tag_raise("sel")
                text_area.tag_add('sel', location, end_location)
                text_area.focus()
            else:
                pass

        f()
        nonlocal prior_search
        replace_string = rep.get()

        if prior_search != replace_string:
            prior_search = e.get()

        search_string = prior_search

        try:
            if text_area.selection_get() == search_string:
                text_area.delete(SEL_FIRST, SEL_LAST)

                row, col = get_index(text_area.index(INSERT))
                text_area.insert(INSERT, replace_string)
                end_location = str(str(row) + '.' + str(col))

                text_area.tag_add('sel', end_location, INSERT)
                text_area.focus()

        except TclError:
            pass
        f()

    #  Interface of Replace
    top = Toplevel()
    top.title("Replace")
    top.iconbitmap(default = 'transparent.ico')
    Label(top, text = "Find what:").grid(row = 0, column = 0, padx = 5, sticky = W)
    e = Entry(top, width = 28)
    e.bind("<Return>", replace_all)
    e.grid(row = 0, column = 1, columnspan = 2, padx = 5, pady = 5)
    Label(top, text = "Replace with:").grid(row = 1, column = 0, padx = 5, sticky = W)
    rep = Entry(top, width = 28)
    rep.bind("<Return>", replace_all)
    rep.grid(row = 1, column = 1, columnspan = 2, padx = 5, pady = 5)

    find_next = Button(top, text = "  Find Next ", command = find_next).grid(row = 0, column = 4, padx = 10, pady = 5,
                                                                             sticky = "ew")
    replace_next = Button(top, text = "  Replace Next  ", command = replace_next).grid(row = 1, column = 4, padx = 10,
                                                                                       pady = 5, sticky = "ew")
    replace_all = Button(top, text = "  Replace All  ", command = replace_all).grid(row = 2, column = 4, padx = 10,
                                                                                    pady = 5, sticky = "ew")
    cancel_button = Button(top, text = "  Cancel  ", command = top.destroy).grid(row = 3, column = 4, padx = 10,
                                                                                 pady = 5, sticky = "ew")
    no_case_match = BooleanVar()
    no_case_match.set(False)
    match_case = Checkbutton(top, text = 'Match case', variable = no_case_match)
    match_case.grid(row = 3, column = 0, sticky = "sw", padx = 5, pady = 10, columnspan = 2)


# Interface of the Go To... Command
def show_goto(event=None):
    global goto_open
    if not goto_open:
        goto_open = True

    # Implementation of Go To Button
    def goto():
        line = e.get()
        try:
            line = int(line)
            text_area.mark_set("insert", "%d.0" % line)
            text_area.see("insert")

        except ValueError:
            pass

    # Implementation of Cancel Button
    def quit_goto():
        goto_open = False
        top.destroy()

    top = Toplevel()
    top.title('Go To Line')
    top.resizable(False, False)

    # search string box
    find_label = Label(top, text = 'Line Number:')
    find_label.grid(row = 0, column = 0, sticky = 'nw', pady = (10, 0), padx = 5)
    e = Entry(top, width = 35)
    e.grid(row = 1, column = 0, columnspan = 2, sticky = 'new', padx = 5, pady = (0, 10))
    e.focus()
    button_box = Frame(top)
    Button(button_box, text = "Go To",
           command = goto).grid(row = '0', column = 0, padx = 0, pady = (0, 5), sticky = 'e')
    Button(button_box, text = "Cancel",
           command = quit_goto).grid(row = '0', column = 1, padx = (5, 10), pady = (0, 5), sticky = 'e')
    button_box.grid(column = 1, row = 2)


# Implementation of Search Command
def search(event = None):
    txt = quote(text_area.get(1.0, END))
    url = "https://www.google.com.tr/search?q={}" + txt
    webbrowser.open_new_tab(url)


# Implementation of Select All
def select_all():
    text_area.tag_add("sel", 1.0, END)


# Implementation of Word Wrap option
# This shows or hides the horizontal scrollbar
def word_wrap():
    if not word_wrap1.get():
        scroll.pack(side = BOTTOM, fill = X)
        text_area.configure(wrap = NONE, xscrollcommand = scroll.set, yscrollcommand = Scroll.set, undo = True)
    else:
        scroll.pack_forget()
        text_area.configure(wrap = WORD, yscrollcommand = Scroll.set, undo = True)
    text_area.pack(fill = BOTH, expand = True)


# Implementation of Time/Date Command
# It appends the current time and date in the text_area
# The format is HH:MM DD:MM:YYYY as per the default system in India
def time_date(event = None):
    x = datetime.date.today()
    year = str(x.year)
    month = str(x.month)
    if int(month) < 10:
        month = "0" + month
    day = str(x.day)
    y = datetime.datetime.now()
    t = y.strftime("%H:%M")
    text_area.insert(END, t + " " + day + "-" + month + "-" + year)


def get_help():
    msg.showinfo("Notepad", "This is a Notepad clone by skate1512")


# This is to show/hide the statusbar
def status():
    if not show_status.get():
        statusbar.pack_forget()
    else:
        statusbar.pack(fill = X, expand = 0)


# This is to open a menu when mouse is right-clicked
def show_context_menu(event=None):
    try:
        context_menu.tk_popup(event.x_root, event.y_root)
    finally:
        context_menu.grab_release()


# Root Window initialisation
root = Tk()
root.title('Untitled - Notepad')
root.iconbitmap('Notepad.ico')
root.geometry("743x659")
text_area = Text(root, font = font_tuple, undo = True)
text_area.focus_set()


# Scrollbar
Scroll = Scrollbar(text_area)
Scroll.pack(side = RIGHT, fill = Y)
Scroll.configure(command = text_area.yview)
text_area.configure(wrap = WORD, yscrollcommand = Scroll.set, undo = True)
text_area.bind("<<Button-3>>", show_context_menu)
text_area.pack(fill = BOTH, expand = True)

scroll = Scrollbar(text_area, orient = HORIZONTAL)
scroll.configure(command = text_area.xview)

file = None

menu_bar = Menu(root)
# File menu
file_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", accelerator = "Ctrl+N", command = new_file)
root.bind("<Control - N>", new_file)
root.bind("<Control - n>", new_file)
file_menu.add_command(label = "New Window", accelerator = "Ctrl+Shift+N", command = new_window)
root.bind("<Control - Shift - N>", new_file)
root.bind("<Control - Shift - n>", new_file)
file_menu.add_command(label = "Open", accelerator = "Ctrl+O", command = open_file)
root.bind("<Control - O>", open_file)
root.bind("<Control - o>", open_file)
file_menu.add_command(label = "Save", accelerator = "Ctrl+S", command = save_file)
root.bind("<Control - S>", save_file)
root.bind("<Control - s>", save_file)
file_menu.add_command(label = "Save As...", accelerator = "Ctrl+Shift+S", command = save_as_file)
root.bind("<Control - Shift - S>", save_as_file)
root.bind("<Control - Shift - s>", save_as_file)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = on_closing)

# Edit Menu
edit_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Undo", accelerator = "Ctrl+Z", command = undo)
edit_menu.add_separator()
edit_menu.add_command(label = "Cut", accelerator = "Ctrl+X", command = cut)
edit_menu.add_command(label = "Copy", accelerator = "Ctrl+C", command = copy)
edit_menu.add_command(label = "Paste ", accelerator = "Ctrl+V", command = paste)
edit_menu.add_command(label = "Delete", accelerator = "Delete", command = delete)

edit_menu.add_separator()

edit_menu.add_command(label = "Search with Google...", accelerator = "Ctrl+E", command = search)
root.bind("<Control - E>", search)
root.bind("<Control - e>", search)
edit_menu.add_command(label = "Find", accelerator = "Ctrl+F", command = find)
root.bind("<Control - f>", find)
root.bind("<Control - F>", find)
edit_menu.add_command(label = "Replace", accelerator = "Ctrl+H", command = replace)
root.bind("<Control - H>", replace)
root.bind("<Control - h>", replace)
edit_menu.add_command(label = "Go to...", accelerator = "Ctrl+H", command = show_goto)
root.bind("<Control - g>", show_goto)
root.bind("<Control - G>", show_goto)
edit_menu.add_separator()

edit_menu.add_command(label = "Select All", accelerator = "Ctrl+A", command = select_all)
edit_menu.add_command(label = "Time/Date", accelerator = "Ctrl+T", command = time_date)
root.bind("<Control - t>", time_date)
root.bind("<Control - T>", time_date)

# Format Menu
format_menu = Menu(menu_bar, tearoff = 0)
word_wrap1 = BooleanVar()
word_wrap1.set(True)
menu_bar.add_cascade(label = "Format", menu = format_menu)
format_menu.add_checkbutton(label = "Word Wrap", onvalue = 1, offvalue = 0, variable = word_wrap1, command = word_wrap)
format_menu.add_command(label = "Font...", command = font_window)

# View menu
view_menu = Menu(menu_bar, tearoff = 0)
show_status = BooleanVar()
show_status.set(True)
menu_bar.add_cascade(label = "View", menu = view_menu)

view_menu.add_checkbutton(label = "Status Bar", onvalue = 1, offvalue = 0, variable = show_status, command = status)

# Help Menu
help_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "Help", menu = help_menu)
help_menu.add_command(label = "View Help", command = get_help)

root.configure(menu = menu_bar)

# Context Menu - Right Mouse Button
context_menu = Menu(root, tearoff = 0)
context_menu.add_command(label = 'Undo', underline = 2, accelerator = 'Ctrl+Z', command = undo)
context_menu.add_separator()
context_menu.add_command(label = 'Cut', underline = 2, accelerator = 'Ctrl+X', command = cut)
context_menu.add_command(label = 'Copy', underline = 0, accelerator = 'Ctrl+C', command = copy)
context_menu.add_command(label = 'Paste', underline = 0, accelerator = 'Ctrl+V', command = paste)
context_menu.add_command(label = 'Delete', underline = 2, accelerator = 'Del', command = delete)
context_menu.add_separator()
context_menu.add_command(label = 'Select All', underline = 2, accelerator = 'Ctrl+A', command = select_all)
context_menu.add_separator()
context_menu.add_command(label = 'Search with Google... ', underline = 0, accelerator = 'Ctrl+E', command = search)
# Binding Right Mouse Button to the context_menu
root.bind("<Button-3>", show_context_menu)

global statusbar
statusbar = Label(root, text = " Ln 1, Col 1")
statusbar.pack(fill = X, expand = 0)

cursor_move = False


# This is to update the Statusbar when cursor is moved
def cursor_change(event = None):
    global cursor_move
    if text_area.edit_modified():
        cursor_move = True
        line = int(text_area.index('end-1c').split('.')[0])
        character = len(text_area.get(1.0, 'end-1c')) + 1
        statusbar.config(text = " Ln " + str(line) + ", Col " + str(character).format(line, character))
    text_area.edit_modified(False)


text_area.bind("<<Modified>>", cursor_change)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
