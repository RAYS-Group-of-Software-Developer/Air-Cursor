import tkinter as tk
from typing import Optional, Tuple, Union
import customtkinter as ctk
import ttkbootstrap as ttkbs
from PIL import Image, ImageTk
import os
from ctypes import windll
from random import randint,choice
import emoji

#  global variables


class Splash_Frame(ctk.CTkFrame):
    def __init__(
        self,
        master: any,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        gif_path: str = None,  # path to gif
        **kwargs,
    ):
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            background_corner_colors,
            overwrite_preferred_drawing_method,
            gif_path,
            **kwargs,
        )


class Titlebar(ctk.CTkFrame):
    def __init__(
        self,
        master: any,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        App_title: str = "Air Cursor",  # title of app
        # iconPath: str = None,  # path to icon
        titleBarColor: str = "black",  # color of titlebar
        # jsutify: str = None,  # left, center, right
        style: str = None,  # style of titlebar -> "mac", "windows"
        resizeable: bool = True,  # resizeable window
        **kwargs,
    ):
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            background_corner_colors,
            overwrite_preferred_drawing_method,
            **kwargs,
        )

        self.parent = master
        print("self.parent" + str(self.parent))

        # layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.resizeable = resizeable
        transparent_color = self._apply_appearance_mode(["#f2f2f2", "#000001"])
        self.titlebar_color = titleBarColor

        # titlebar
        self.App_title = App_title
        self.title_label = ctk.CTkLabel(
            self,
            width=10,
            # image=self.icon,
            compound="left",
            text=f"  {self.App_title}",
            anchor="n",
            font=("Segoe UI", 20, "bold"),
        )
        self.title_label.grid(row=0, sticky="we", padx=(30, 0), pady=7)

        self.title_label.bind("<ButtonPress-1>", self.parent.oldxyset)
        self.title_label._label.bind("<ButtonPress-1>", self.parent.oldxyset)
        self.title_label.bind("<B1-Motion>", self.parent.move_window)
        self.title_label._label.bind("<B1-Motion>", self.parent.move_window)
        self.title_label.bind(
            "<Double-1>", lambda event: self.parent.max_window())

        if self.resizeable == True:
            self.parent.bind("<Motion>", self.parent.change_cursor)
            self.parent.bind("<B1-Motion>", self.parent.resize)
            max_button_color = "yellow"
            hover_color = "#ffda71"
        else:
            max_button_color = "grey60"
            hover_color = "grey60"

        # titlebar buttons -> close, minimize, maximize
        if style == "mac":
            self.button_close = ctk.CTkButton(
                self,
                corner_radius=10,
                width=10,
                height=10,
                text="",
                hover_color="dark red",
                fg_color="red",
                command=lambda: self.parent.destroy(),
            )
            self.button_close.grid(
                row=0, column=2, sticky="ne", padx=(0, 15), pady=10)
            self.button_close.configure(cursor="arrow")

            self.button_max = ctk.CTkButton(
                self,
                corner_radius=10,
                width=10,
                height=10,
                text="",
                hover_color=hover_color,
                fg_color=max_button_color,
                command=lambda: print("maximize"),
            )
            self.button_max.grid(
                row=0, column=1, sticky="ne", padx=10, pady=10)
            self.button_max.configure(cursor="arrow")

            self.button_min = ctk.CTkButton(
                self,
                corner_radius=10,
                width=10,
                height=10,
                text="",
                hover_color="light green",
                fg_color="green",
                command=lambda: print("minimize"),
            )
            self.button_min.grid(row=0, column=0, sticky="ne", pady=10)
            self.button_min.configure(cursor="arrow")
        else:
            self.button_close = ctk.CTkButton(
                self,
                corner_radius=10,
                width=40,
                height=30,
                text="✕",
                hover_color="#c42b1c",
                fg_color="transparent",
                text_color=["black", "white"],
                background_corner_colors=(None, transparent_color, None, None),
                command=self.parent.close_window,
            )
            self.button_close.grid(
                row=0, column=2, sticky="ne", padx=0, pady=0)
            self.button_close.configure(cursor="arrow")
            self.button_close.bind(
                "<Enter>", lambda e: self.change_bg(transparent_color, 1), add="+"
            )
            self.button_close.bind(
                "<Leave>", lambda e: self.change_bg(transparent_color, 0), add="+"
            )

            self.button_max = ctk.CTkButton(
                self,
                corner_radius=0,
                width=40,
                height=30,
                text="□",
                text_color=["black", "white"],
                hover_color="#2d2d2d",
                fg_color="transparent",
                command=self.parent.max_window,
            )
            self.button_max.grid(row=0, column=1, sticky="ne", padx=0, pady=0)
            self.button_max.configure(cursor="arrow")

            self.button_min = ctk.CTkButton(
                self,
                corner_radius=0,
                width=40,
                height=30,
                text="—",
                text_color=["black", "white"],
                hover_color="#2d2d2d",
                fg_color="transparent",
                command=self.parent.min_window,
            )
            self.button_min.grid(row=0, column=0, sticky="ne", pady=0)
            self.button_min.configure(cursor="arrow")

    ################# functions #################
    def change_bg(self, transparent_color, hover):
        if hover:
            self.button_close.configure(
                background_corner_colors=(
                    "#c42b1c",
                    transparent_color,
                    "#c42b1c",
                    "#c42b1c",
                ),
                fg_color="#c42b1c",
            )
        else:
            self.button_close.configure(
                background_corner_colors=(
                    self.titlebar_color,
                    transparent_color,
                    self.titlebar_color,
                    self.titlebar_color,
                ),
                fg_color=self.titlebar_color,
            )


class Base(ctk.CTkFrame):
    def __init__(
        self,
        master: any,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        **kwargs,
    ):
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            background_corner_colors,
            overwrite_preferred_drawing_method,
            **kwargs,
        )

        # layout
        # self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        # self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        
        self.dark_background_image = ctk.CTkImage(Image.open("C:\\Users\\user\\OneDrive - iitr.ac.in\\##Projects\\Air-Cursor\\GUI\\assets\\Backgrounds\\Dark_Theme\\Dark_sky.jpg").resize((int(self.winfo_width()), int(self.winfo_height()))))
        self.light_background_image = ctk.CTkImage(Image.open("C:\\Users\\user\\OneDrive - iitr.ac.in\\##Projects\\Air-Cursor\\GUI\\assets\\Backgrounds\\Light_Theme\\Light_sky.jpg").resize((int(self.winfo_width()), int(self.winfo_height()))))
        self.background_image_label = ctk.CTkLabel(self, image=self.dark_background_image, corner_radius=10)
        # self.background_image_label.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")
        # self.background_image_label.pack(expand=True, fill="both")
        

        self.Configure_widget = self.create_configure_widget()
        self.Help_widget = self.create_help_widget()
        self.About_us_widget = self.create_About_us_widget()
        self.Lauch_widget = self.create_launch_widget()
        self.Tips_widget = self.create_tips_widget()

        self.Configure_widget.place(x=1,rely=0.01,relwidth=0.25,relheight=0.39, anchor="nw")
        self.Help_widget.place(x=1,rely=0.44,relwidth=0.25,relheight=0.38, anchor="nw")
        self.About_us_widget.place(x=1,rely=0.86,relwidth=0.25,relheight=0.13304, anchor="nw")
        
        self.Lauch_widget.place(relx=0.28,rely=0.01,relwidth=0.72,relheight=0.39, anchor="nw")
        self.Tips_widget.place(relx=0.28,rely=0.44,relwidth=0.73,relheight=0.55, anchor="nw")
        
        # set background image
        # self.dark_background_image = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\OneDrive - iitr.ac.in\\##Projects\\Air-Cursor\\GUI\\assets\\Backgrounds\\Dark_Theme\\Dark_sky.jpg").resize(500,500))
        # self.light_background_image = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\OneDrive - iitr.ac.in\\##Projects\\Air-Cursor\\GUI\\assets\\Backgrounds\\Light_Theme\\Light_sky.jpg").resize((int(self.winfo_width()), int(self.winfo_height()))))
        # self.background_image = self.dark_background_image
        # self.background_image_label = ctk.CTkLabel(self, image=self.background_image, corner_radius=10)
        
        
        # Create widgets

    def create_configure_widget(self):
        configure_widget = ctk.CTkFrame(
            self, 
            bg_color="transparent", 
            # fg_color="", 
            corner_radius=10
        )
        
        # a label and a button
        label = ctk.CTkLabel(configure_widget, text="Stable and Reliable\nExperience", font=("Segoe UI", 20, "bold"), corner_radius=10)
        label.place(relx=0.5, rely= 0.33, relwidth=0.95,relheight=0.5 , anchor="center")
        button = ctk.CTkButton(configure_widget, text="Configure", font=("Segoe UI", 20, "bold"), corner_radius=50, fg_color="#000001", command= self.configure_button_click)
        button.place(relx=0.5, rely=0.8, relwidth=0.8, relheight=0.33, anchor="center")
        return configure_widget

        # self.configure_widget.grid_columnconfigure(0, weight=1)
        # self.configure_widget.grid_rowconfigure((0,1,2), weight=1)

    def create_help_widget(self):
        help_widget = ctk.CTkFrame(
            self, 
            bg_color="transparent", 
            # fg_color="", 
            corner_radius=10
        )
        
        # a label and a button
        label = ctk.CTkLabel(help_widget, text="Support and Query", font=("Segoe UI", 20, "bold"), corner_radius=10)
        label.place(relx=0.5, rely= 0.33, relwidth=0.95,relheight=0.66 , anchor="center")
        button = ctk.CTkButton(help_widget, text="Help", font=("Segoe UI", 20, "bold"), corner_radius=50, fg_color="#000001", command= self.help_button_click)
        button.place(relx=0.5, rely=0.8, relwidth=0.8, relheight=0.33, anchor="center")
        return help_widget

    def create_About_us_widget(self):
        About_us_widget = ctk.CTkFrame(
            self, 
            bg_color="#000001", 
            fg_color="#000001",
            # fg_color="", 
            corner_radius=10
        )
        # only a button
        ctk.CTkButton(About_us_widget, text="About us", font=("Segoe UI", 20, "bold"), corner_radius=10, fg_color="#000001", border_color="white", border_width=1, command=self.about_us_button_click).pack(expand=True, fill="both")
        return About_us_widget

    def create_launch_widget(self):
        Lauch_widget = ctk.CTkFrame(
            self, 
            bg_color="transparent", 
            # fg_color="red", 
            corner_radius=10
        )
        
        label_frame = ctk.CTkFrame(Lauch_widget, bg_color="transparent", fg_color="transparent", corner_radius=10)
        button_frame = ctk.CTkFrame(Lauch_widget, bg_color="transparent", fg_color="transparent", corner_radius=10)
        
        """
            Label Frame takes 2/3 of the height
            Button Frame takes 1/3 of the height
        """
        label_frame.place(relx=0.5, rely= 0.34, relwidth=0.95,relheight=0.66 , anchor="center")
        button_frame.place(relx=0.5, rely=0.81, relwidth=0.95, relheight=0.31, anchor="center")
        
        catchphrases = ("Move it like you own it", "You have magic hands.\nTry moving them", "Magic in the air")
        
        
            
        
        # label frame contains a cachphrase about the app -> "Move it like you own it"
        catchphrase_label = ctk.CTkLabel(label_frame, text="Move it like you own it", font=("Segoe UI", 50, "bold", "italic"), corner_radius=10)
        catchphrase_label.pack(side="left")
        
        def update_catcphrase():
            while True:
                new_catchphrase = choice(catchphrases)
                if new_catchphrase != catchphrase_label.cget("text"):
                    break
            catchphrase_label.configure(text=new_catchphrase)
            self.after(3000, update_catcphrase)
        
        update_catcphrase()
        
        # button frame contains two buttons
        launch_button = ctk.CTkButton(button_frame, text="Launch", font=("Segoe UI", 20, "bold"), corner_radius=10, fg_color="#000001", border_color="white", border_width=1, command=self.launch_button_click)
        stop_button = ctk.CTkButton(button_frame, text="Stop", font=("Segoe UI", 20, "bold"), corner_radius=10, fg_color="#000001", border_color="white", border_width=1, command=self.stop_button_click)
        
        launch_button.place(relx=0.45, rely=0.1, relwidth=0.25, relheight=0.89, anchor="nw")
        stop_button.place(relx=0.75, rely=0.1, relwidth=0.25, relheight=0.89, anchor="nw")
        

        return Lauch_widget

    def create_tips_widget(self):
        Tips_widget = ctk.CTkFrame(
            self, 
            bg_color="transparent", 
            fg_color="transparent", 
            corner_radius=10
        )
        tips = ("You need tips! Noob 😁", "Do something you lazy 🤨", "CG kitna hai tera? 🤭", "Chinta mat kar,\nbandi nahi milegi 😁")
        """
            Layout: <button> <tips_content> <button>
            the left button is for previous tip and the right button is for next tip
        """
        # what is the default frame color in dark mode in customtkinter?
        
        
        left_button = ctk.CTkButton(Tips_widget, text="<", font=("Segoe UI", 20, "bold"), corner_radius=20, fg_color="#2b2b2b", hover_color="#000001", command= lambda : previous_tip())
        right_button = ctk.CTkButton(Tips_widget, text=">", font=("Segoe UI", 20, "bold"), corner_radius=20, fg_color="#2b2b2b", hover_color="#000001", command= lambda: next_tip())
        # left_button.place(relx=0.01, rely=0.01, relwidth=0.1, relheight=0.98, anchor="nw")
        # right_button.place(relx=0.89, rely=0.01, relwidth=0.1, relheight=0.98, anchor="nw")
        left_button.place(relx=0, rely=0.0, relwidth=0.1, relheight=1, anchor="nw")
        right_button.place(relx=0.885, rely=0.0, relwidth=0.1, relheight=1, anchor="nw")
        
        tip = tips[0]
        tips_content = ctk.CTkFrame(Tips_widget, bg_color="transparent", fg_color="transparent", corner_radius=10)
        tips_content.place(relx=0.12, rely=0.01, relwidth=0.76, relheight=0.97, anchor="nw")
        tip_label = ctk.CTkLabel(tips_content, text=tip, font=("Segoe UI", 30, "bold"), corner_radius=10, text_color="gold")
        tip_label.pack(expand=True, fill="both")
        
        def previous_tip():
            # change the tip
            while True:
                tip = choice(tips)
                if tip != tip_label.cget("text"):
                    break
            tip_label.configure(text=tip)
        
        def next_tip():
            while True:
                tip = choice(tips)
                if tip != tip_label.cget("text"):
                    break
            tip_label.configure(text=tip)
        
        return Tips_widget
    
    # button click functions
    def configure_button_click(self):
        # self.Configure_widget.destroy()
        # self.Configure_widget = self.create_configure_widget()
        # self.Configure_widget.place(x=1,rely=0.01,relwidth=0.25,relheight=0.39, anchor="nw")
        pass
    
    def help_button_click(self):
        # self.Help_widget.destroy()
        # self.Help_widget = self.create_help_widget()
        # self.Help_widget.place(x=1,rely=0.44,relwidth=0.25,relheight=0.38, anchor="nw")
        pass
    
    def about_us_button_click(self):
        # self.About_us_widget.destroy()
        # self.About_us_widget = self.create_About_us_widget()
        # self.About_us_widget.place(x=1,rely=0.86,relwidth=0.25,relheight=0.13304, anchor="nw")
        pass
    
    def launch_button_click(self):
        pass
    
    def stop_button_click(self):
        pass
    

class MainWindow(ctk.CTk):
    def __init__(
        self,
        fg_color: str | Tuple[str, str] | None = None,
        iconPath: str = None,  # path to icon
        resizeable: bool = True,  # resizeable window
        **kwargs,
    ):
        super().__init__(fg_color, **kwargs)

        # window settings
        width = 950
        height = int(width * 9 / 16)
        self.geometry(f"{width}x{height}")
        self.title("Air Cursor")
        # self.overrideredirect(True)
        self.resizable(resizeable, resizeable)

        self.x = self.winfo_x()
        self.y = self.winfo_y()
        self.fullscreen = False
        self.GWL_EXSTYLE = -20
        self.WS_EX_APPWINDOW = 0x00040000
        self.WS_EX_TOOLWINDOW = 0x00000080
        self.minmize = False

        transparent_color = self._apply_appearance_mode(["white", "#000000"])
        # layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)  # 0 is titlebar, 1 is base
        self.grid_rowconfigure(1, weight=1)

        self.config(background=transparent_color)
        # self.attributes(
        #     "-transparentcolor", transparent_color
        # )  # transparent_color will be the transparent color

        # titlebar

        # self.titlebar = Titlebar(
        #     self,

        #     height=title_height,
        #     bg_color=("white", "black"),
        #     fg_color=("white", "black"),
        #     App_title="Air Cursor",
        #     border_width=0,
        #     corner_radius=10,
        #     background_corner_colors=(transparent_color, transparent_color, None, None),
        # )
        # self.titlebar.grid(row=0, sticky="nwe")
        
        
        # set background image
        
        
        

        # base frame
        self.app = Base(
            self,
            bg_color=("white", "#000000"),
            fg_color=("white", "#000000"),
            # border_width=0,
            corner_radius=10,
        )

        # self.app.place(x=1,y=title_height, relwidth=1, relheight=1)
        self.app.place(relx=0.5,rely=0.5, relwidth=0.97, relheight=0.97, anchor="center")
        # self.app.bind("<Map>", self.frame_mapped)

    ######## titlebar functions ########
    def geometry(self, geometry):
        super().geometry(geometry)

    # def iconbitmap(self, icon):
    #     self.icon = customtkinter.CTkImage(Image.open(icon), size=(16, 16))
    #     self.title_label.configure(image=self.icon)

    def oldxyset(self, event):
        self.oldx = event.x
        self.oldy = event.y

    def close_window(self):
        super().destroy()

    def move_window(self, event):
        if self.fullscreen == False:
            self.y = event.y_root - self.oldy
            self.x = event.x_root - self.oldx
            self.geometry(f"+{self.x}+{self.y}")

    def frame_mapped(self, e):
        self.update_idletasks()
        self.overrideredirect(True)
        self.state("normal")
        if self.minmize:
            self.fullscreen = False
            self.max_window()
        self.minmize = False

    def min_window(self):
        self.update_idletasks()
        self.overrideredirect(False)
        self.withdraw()
        self.state("iconic")
        if self.fullscreen:
            self.minmize = True
        # self.overrideredirect(True)

    def set_appwindow(self):
        hwnd = windll.user32.GetParent(self.winfo_id())
        style = windll.user32.GetWindowLongW(hwnd, self.GWL_EXSTYLE)
        style = style & ~self.WS_EX_TOOLWINDOW
        style = style | self.WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, self.GWL_EXSTYLE, style)
        self.wm_withdraw()
        self.after(10, lambda: self.wm_deiconify())

    def max_window(self):
        if self.resizable == True:
            if self.fullscreen == False:
                self.update_idletasks()
                self.overrideredirect(False)
                self.wm_state("zoomed")
                self.overrideredirect(True)
                self.after(10, lambda: self.set_appwindow())
                self.state("normal")
                self.fullscreen = True
                if self.style == "classic":
                    self.button_max.configure(text="❒")
            else:
                self.geometry(f"+{self.x}+{self.y}")
                self.fullscreen = False
                if self.style == "classic":
                    self.button_max.configure(text="□")

    def change_cursor(self, event):
        # the cursor will change when the mouse is in the range of 10 pixels from the edge of the window, the cursor will change to size_nw_se (diagonal)
        if event.x in range(
            self.app.winfo_width() - 10, self.app.winfo_width()
        ) and event.y in range(self.app.winfo_height() - 10, self.app.winfo_height()):
            self.config(cursor="size_nw_se")
            return
        else:
            self.config(cursor="")

        # the cursor will change when the mouse is in the range of 5 pixels from the edge of the window
        if event.x in range(
            self.app.winfo_width() - 5, self.app.winfo_width()
        ) and event.y in range(0, self.app.winfo_height()):
            self.config(cursor="sb_h_double_arrow")
            return
        else:
            self.config(cursor="")

        if event.x in range(0, self.app.winfo_width()) and event.y in range(
            self.app.winfo_height() - 5, self.app.winfo_height()
        ):
            self.config(cursor="sb_v_double_arrow")
            return
        else:
            self.config(cursor="")

    def resize(self, event):
        if self.cget("cursor") == "size_nw_se":
            if event.x > 100 and event.y > 100:
                self.geometry(
                    f"{event.x_root - self.x}x{event.y_root - self.y}")
        elif self.cget("cursor") == "sb_h_double_arrow":
            self.geometry(f"{event.x_root - self.x}x{self.winfo_height()}")
        elif self.cget("cursor") == "sb_v_double_arrow":
            self.geometry(f"{self.winfo_width()}x{event.y_root - self.y}")



#  run the app
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
