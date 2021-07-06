from tkinter import Tk


def create_app():
    tk = Tk() # create window
    tk.geometry("700x500+0+0") # define size of
    tk.title("GUI Product shop")
    return tk


tk = create_app() # create tk object_dict
