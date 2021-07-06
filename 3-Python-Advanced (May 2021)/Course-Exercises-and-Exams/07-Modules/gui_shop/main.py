# from authentication import render_main_enter_screen
from gui_shop.authentication import render_main_enter_screen
from gui_shop.canvas import tk

if __name__ == '__main__':
    render_main_enter_screen()
    tk.mainloop() # keeps the window on our screen until we close it. Otherwise it wold disappears.

