"""
Application created by BogdosDev

name:Mathematical Functions
version: 1.0 
"""

import tkinter as tk
from ctypes import windll
from tkinter.messagebox import showinfo

from scripts.widgets import Entry, Label, Button, update_theme
import scripts.horner as horner
from scripts.distinctive import distinctive
from scripts.geometry import Geometry
from scripts.monotony import Monotony

from scripts.colors import Colors, theme
    

WIDTH, HEIGHT = 420, 560
Geo = Geometry(width=WIDTH, height=HEIGHT)

# App structure
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        self.title(" Mathematical Functions")
        x_Left = int((self.winfo_screenwidth() - WIDTH) /2 + WIDTH/2.18)
        y_Top = int((self.winfo_screenheight()/2 - HEIGHT/2))
        self.geometry(f'{str(WIDTH)}x{str(HEIGHT)}+{x_Left}+{y_Top}')
        self.configure(bg=Colors.bg(theme))
        self.resizable(height = False, width = False)
        icon_img = tk.PhotoImage(file=f"assets/function-icon.png")
        self.iconphoto(False, icon_img)
        
        windll.shcore.SetProcessDpiAwareness(1)
        

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Canvas.__init__(self, master, bg=Colors.bg(theme), highlightthickness=0, width=WIDTH ,height=HEIGHT)
        _Label = Label(self)
        _Button = Button(self)
          
        img_title = tk.PhotoImage(file=f"assets/{theme}/title-1.png")
        page_title = _Label.title(img_title)
        page_title.place(x=Geo.center(widget_width=200), y=26, width=200)   
        
        img = tk.PhotoImage(file=f"assets/{theme}/button-1.png")        
        bt = _Button.image_button(image=img, command=lambda:master.switch_frame(PageOne))
        bt.place(x=Geo.center(widget_width=200), y=120, width=200)
        
        img = tk.PhotoImage(file=f"assets/{theme}/button-2.png")        
        bt = _Button.image_button(image=img, command=lambda:master.switch_frame(PageTwo))
        bt.place(x=Geo.center(widget_width=200), y=182, width=200)
        
        img = tk.PhotoImage(file=f"assets/{theme}/button-6.png")        
        bt = _Button.image_button(image=img, command=lambda:master.switch_frame(PageThree)) 
        bt.place(x=Geo.center(widget_width=200), y=244, width=200)
        
        img = tk.PhotoImage(file=f"assets/{theme}/button-7.png")        
        bt = _Button.image_button(image=img, command=lambda:master.switch_frame(MorePage)) 
        bt.place(x=Geo.center(widget_width=200), y=306, width=200)
        
        img = tk.PhotoImage(file=f"assets/{theme}/button-4.png")        
        bt = _Button.image_button(image=img, command=lambda:self.quit())
        bt.place(x=Geo.center(widget_width=100), y=HEIGHT-60, width=100)
        
        # copyright claim
        cpr_img = tk.PhotoImage(file=f"assets/{theme}/copyright_mark.png")
        cpr = tk.Label(self, image=cpr_img, bg=Colors.bg(theme))
        cpr.image = cpr_img
        cpr.place(x=WIDTH - 110, y=HEIGHT - 30)
    
class PageOne(tk.Frame):  # -Horner Solver
    def __init__(self, master):
        tk.Canvas.__init__(self, master, bg=Colors.bg(theme), highlightthickness=0, width=WIDTH ,height=HEIGHT)
        
        img_title = tk.PhotoImage(file=f"assets/{theme}/title-2.png")
        page_title = Label(self).title(img_title)
        page_title.place(x=Geo.center(widget_width=200),y=26, width=200)   
        
        canvas_entries = tk.Canvas(self, bg=Colors.bg(theme), highlightthickness=0)
        canvas_entries.place(x=Geo.center(widget_width=340), y=106, width=340 ,height=100)
        
        _Label = Label(canvas_entries)
        _Button = Button(canvas_entries)
        _Entry = Entry(canvas_entries)
        
        # START
        
        _Label.prefix("x","4", x=21, y=0)
        _Label.prefix("x","3", x=95, y=0)
        _Label.prefix("x","2", x=163, y=0)
        _Label.prefix("x","1", x=230, y=0)
        _Label.prefix("x","0", x=305, y=0)
            
        var_4x = tk.StringVar()
        var_3x = tk.StringVar()
        var_2x = tk.StringVar()
        var_1x = tk.StringVar()
        var_0x = tk.StringVar()
            
        img_ = tk.PhotoImage(file=f"assets/{theme}/entry-1.png")
        lb_1 = tk.Label(canvas_entries, image=img_, bg=Colors.bg(theme))
        lb_2 = tk.Label(canvas_entries, image=img_, bg=Colors.bg(theme))
        lb_3 = tk.Label(canvas_entries, image=img_, bg=Colors.bg(theme))
        lb_4 = tk.Label(canvas_entries, image=img_, bg=Colors.bg(theme))
        lb_5 = tk.Label(canvas_entries, image=img_, bg=Colors.bg(theme))
        lb_1.image =  lb_2.image = lb_3.image = lb_4.image = lb_5.image = img_
        
        lb_1.place(x=0, y=26, width=55)
        lb_2.place(x=74, y=26, width=55)
        lb_3.place(x=142, y=26, width=55)
        lb_4.place(x=210, y=26, width=55)
        lb_5.place(x=285, y=26, width=55)
        
        _Entry.entry(var_4x).place(x=7, y=33, width=40, height=25)
        _Entry.entry(var_3x).place(x=83, y=33, width=40, height=25)
        _Entry.entry(var_2x).place(x=150, y=33, width=40, height=25)
        _Entry.entry(var_1x).place(x=217, y=33, width=40, height=25)
        _Entry.entry(var_0x).place(x=292, y=33, width=40, height=25)    
            
        # END 
        
        _Label = Label(self)
        _Button = Button(self)
        
        self.solve_var = tk.StringVar()
        self.solve_var.set("None Yet")
        def solve():
            try:
                lst = horner.power_4(var_4x.get(), var_3x.get(), var_2x.get(), var_1x.get(), var_0x.get())
            except:
                print("horner failed")
                lst = "FAILED"
            self.solve_var.set(str(lst))
                
        answr = _Label.subtitle(textvariable=self.solve_var)
        answr.place(x=Geo.center(widget_width=340), y=320,width=340)
        img_answer = tk.PhotoImage(file=f"assets/{theme}/subtitle-1.png")
        _Label.title(img_answer).place(x=Geo.center(widget_width=180),y=290, width=180) 
        
        img = tk.PhotoImage(file=f"assets/{theme}/button-5.png")        
        bt = _Button.image_button(image=img, command=lambda:solve())
        bt.place(x=Geo.center(widget_width=200), y=210, width=200)
        
        img = tk.PhotoImage(file=f"assets/{theme}/button-3.png")        
        bt = _Button.image_button(image=img, command=lambda:master.switch_frame(StartPage))
        _x, _y = Geo.anchor_BL(widget_size=(50,50), difference=(16,10))
        bt.place(x=_x, y=_y, width=50, height=50)

class PageTwo(tk.Frame):  # -Distinctive
    def __init__(self, master):
        tk.Canvas.__init__(self, master, bg=Colors.bg(theme), highlightthickness=0, width=WIDTH ,height=HEIGHT)
        
        img_title = tk.PhotoImage(file=f"assets/{theme}/title-3.png")
        page_title = Label(self).title(img_title)
        page_title.image = img_title
        page_title.place(x=Geo.center(widget_width=200),y=26, width=200)   
        
        canvas_entries = tk.Canvas(self, bg=Colors.bg(theme), highlightthickness=0)
        canvas_entries.place(x=Geo.center(widget_width=340), y=106, width=340 ,height=100)
        
        _Label = Label(canvas_entries)
        _Button = Button(canvas_entries)
        _Entry = Entry(canvas_entries)
                
        # START
        
        _Label.prefix("a","", x=70, y=0, width=35, show=False)
        _Label.prefix("b","", x=159, y=0, width=35, show=False)
        _Label.prefix("c","", x=245, y=0, width=35, show=False)
        
        var_a = tk.StringVar()
        var_b = tk.StringVar()
        var_c = tk.StringVar()
        
        img_ = tk.PhotoImage(file=f"assets/{theme}/entry-1.png")
        lb_1 = tk.Label(canvas_entries, image=img_, bg=Colors.bg(theme))
        lb_2 = tk.Label(canvas_entries, image=img_, bg=Colors.bg(theme))
        lb_3 = tk.Label(canvas_entries, image=img_, bg=Colors.bg(theme))
        lb_1.image =  lb_2.image = lb_3.image = img_
        
        lb_1.place(x=60, y=26, width=55)
        lb_2.place(x=148, y=26, width=55)
        lb_3.place(x=235, y=26, width=55)
        
        _Entry.entry(var_a).place(x=67, y=33, width=40, height=25)
        _Entry.entry(var_b).place(x=156 , y=33, width=40, height=25)
        _Entry.entry(var_c).place(x=242, y=33, width=40, height=25) 
        
        # END
        
        _Label = Label(self)
        _Button = Button(self)
        
        self.solve_var = tk.StringVar()
        self.solve_var.set("None Yet")
        def solve():
            try:
                result = distinctive(var_a.get(), var_b.get(), var_c.get())
            except:
                print("distinctive failed")
                result = "FAILED"
            self.solve_var.set(str(result))
                
        answr = _Label.subtitle(textvariable=self.solve_var)
        answr.place(x=Geo.center(widget_width=340), y=320,width=340)
        img_answer = tk.PhotoImage(file=f"assets/{theme}/subtitle-1.png")
        _Label.title(img_answer).place(x=Geo.center(widget_width=180),y=290, width=180) 
        
        img = tk.PhotoImage(file=f"assets/{theme}/button-5.png")        
        bt = _Button.image_button(image=img, command=lambda:solve())
        bt.place(x=Geo.center(widget_width=200), y=210, width=200)
        
        img = tk.PhotoImage(file=f"assets/{theme}/button-3.png")        
        bt = _Button.image_button(image=img, command=lambda:master.switch_frame(StartPage))
        _x, _y = Geo.anchor_BL(widget_size=(50,50), difference=(16,10))
        bt.place(x=_x, y=_y, width=50, height=50)
        
class PageThree(tk.Frame):  # -Monotony
    def __init__(self, master):
        tk.Canvas.__init__(self, master, bg=Colors.bg(theme), highlightthickness=0, width=WIDTH ,height=HEIGHT)
        
        _Label = Label(self)
        _Button = Button(self)
        _Entry = Entry(self)
        
        img_title = tk.PhotoImage(file=f"assets/{theme}/title-4.png")
        page_title = _Label.title(img_title)
        page_title.image = img_title
        page_title.place(x=Geo.center(widget_width=200),y=26, width=200)   
        
        # START
        
        entry_var = tk.StringVar()
        
        img_ = tk.PhotoImage(file=f"assets/{theme}/entry-2.png")
        lb_1 = tk.Label(self, image=img_, bg=Colors.bg(theme))
        lb_1.image = img_
        
        lb_1.place(x=Geo.center(widget_width=300), y=132, width=300)
        
        _Entry.entry(entry_var, justify='left').place(x=Geo.center(widget_width=210), y=134, width=240, height=35)
        
        
        def solve():
            mon = Monotony()
            mon.set_function(func=entry_var.get())
            results = f"f'(x) = 0:  {mon.solve()}\n\nf'(x) < 0:  {mon.get_smaller()}\n\nf'(x) > 0:  {mon.get_greater()}"
            showinfo(title="Monotony Results", message=results)
            
        
        img = tk.PhotoImage(file=f"assets/{theme}/button-5.png")        
        bt = _Button.image_button(image=img, command=lambda:solve())
        bt.place(x=Geo.center(widget_width=200), y=210, width=200)
        
        #END
        
        img_dictionary = tk.PhotoImage(file=f"assets/{theme}/subtitle-3.png")
        _Label.title(img_dictionary).place(x=Geo.center(widget_width=310),y=290, width=310)
        
        img = tk.PhotoImage(file=f"assets/{theme}/button-3.png")        
        bt = _Button.image_button(image=img, command=lambda:master.switch_frame(StartPage))
        _x, _y = Geo.anchor_BL(widget_size=(50,50), difference=(16,10))
        bt.place(x=_x, y=_y, width=50, height=50)
        
class MorePage(tk.Frame):
    def __init__(self, master):
        tk.Canvas.__init__(self, master, bg=Colors.bg(theme), highlightthickness=0, width=WIDTH ,height=HEIGHT)
        _Label = Label(self)
        _Button = Button(self)
          
        img_title = tk.PhotoImage(file=f"assets/{theme}/title-5.png")
        page_title = _Label.title(img_title)
        page_title.place(x=Geo.center(widget_width=200), y=26, width=200)   
        
        img_sub = tk.PhotoImage(file=f"assets/{theme}/subtitle-2.png")
        _Label.title(img_sub).place(x=Geometry(width=WIDTH/2, height=HEIGHT).center(widget_width=166)/2 + 20,y=160, width=166,  height=50) 
        
        def save():
            global theme
            Colors.change_theme()
            theme = Colors.get_theme()
            update_theme(theme)
            master.switch_frame(MorePage)
                   
        img = tk.PhotoImage(file=f"assets/{theme}/button-8.png")        
        bt = _Button.image_button(image=img, command=lambda:save())
        bt.place(x=Geometry(width=WIDTH/2, height=HEIGHT).center(widget_width=200)/2 + WIDTH/2 - 20, y=160, width=200, height=50)
        
        img = tk.PhotoImage(file=f"assets/{theme}/button-3.png")        
        bt = _Button.image_button(image=img, command=lambda:master.switch_frame(StartPage))
        _x, _y = Geo.anchor_BL(widget_size=(50,50), difference=(16,10))
        bt.place(x=_x, y=_y, width=50, height=50)
        
        # copyright claim
        cpr_img = tk.PhotoImage(file=f"assets/{theme}/copyright_mark.png")
        cpr = tk.Label(self, image=cpr_img, bg=Colors.bg(theme))
        cpr.image = cpr_img
        cpr.place(x=WIDTH - 110, y=HEIGHT - 30)

# Initialization
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()