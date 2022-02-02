import tkinter as tk
from scripts.colors import Colors, theme

def update_theme(_theme):
    global theme
    theme = _theme

class Label():
    def __init__(self, root) -> None:
        self.root = root
        
        
    def title(self, image):
        lb = tk.Label(self.root, image=image, bg=Colors.bg(theme), fg= Colors.fg(theme), font=('Dosis SemiBold', 22))
        lb.image = image
        return lb
    
    def subtitle(self, text="", textvariable="", fontsize=20):
        lb = tk.Label(self.root, text=text ,textvariable=textvariable ,bg=Colors.bg(theme), fg= Colors.fg(theme), font=('Dosis Medium', fontsize))
        return lb
    
    def prefix(self, text_1, text_2, x, y, width=15, show=True):
        lb_1 = tk.Label(self.root, text=text_1, bg=Colors.bg(theme), fg=Colors.fg(theme), font=('Dosis Medium', 14))
        lb_2 = tk.Label(self.root, text=text_2, bg=Colors.bg(theme), fg=Colors.fg(theme), font=('Dosis Medium', 10))
        lb_1.place(x=x, y=y, width=width, height=30)
        if show:
            lb_2.place(x=x+11, y=y+4, width=width-8, height=15)

class Button():
    def __init__(self, root) -> None:
        self.root = root

        
    def image_button(self, image, command):
        btn = tk.Button(self.root, image=image, command=command, bg=Colors.bg(theme), activebackground=Colors.bg(theme), bd=0, highlightthickness=0,)
        btn.image = image
        return btn
    
class Entry():
    def __init__(self, root) -> None:
        self.root = root

    
    def entry(self, var, justify='center'):
        entry = tk.Entry(self.root, textvariable=var, justify=justify, bg=Colors.bg_entry(theme), fg=Colors.fg_entry(theme), highlightthickness=0, bd=0, font=('Dosis Medium', 18))
        return entry