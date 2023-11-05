import time
from typing import Tuple
import customtkinter as ctk
from tkinter import ttk
import ttkbootstrap as ttkbs
from PIL import Image, ImageTk
import os
from random import choice
import sys
from dotenv import load_dotenv

load_dotenv('../.env')

class SplashFrame(ctk.CTkFrame):
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

        self.main_frame = self
        # self.main_frame.config(bg = "black")
        self.main_frame.pack(expand=True, fill="both")
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        self.create_wdgets()

    def create_wdgets(self):
        self.label_gif1 = ctk.CTkLabel(
            self.main_frame, bg_color="transparent", fg_color="white", text=""
        )

        self.label_gif1.grid(row=0, column=0, sticky="nsew")

        workspace = os.path.dirname(__file__)
        assets = os.path.join(workspace, "Assets")
        Splash_Animation = os.path.join(assets, "Splash_Animation")
        # Spikes = os.path.join(assets, "Spikes.mp4")
        # Tony = os.path.join(assets, "tony-stark-iron-man.gif")
        Rain_gif = os.path.join(Splash_Animation, "rain_giphy.gif")

        self.gif1_frames = self._get_frames(Rain_gif)

        # self.label_gif1.configure(image = self.gif1_frames[12])

        # self.play_gif(self.gif1_frames, self.label_gif1)

        self.master.after(
            1000, lambda: self.play_gif(self.gif1_frames, self.label_gif1)
        )

    def _get_frames(self, img):
        with Image.open(img) as gif:
            index = 0
            frames = []
            while True:
                try:
                    gif.seek(index)
                    frame = ctk.CTkImage(
                        light_image=gif.copy(), dark_image=gif.copy(), size=(600, 400)
                    )
                    frames.append(frame)
                except EOFError:
                    break
                index += 1
        return frames

    def play_gif(self, frames, label, delay=0.04):
        for frame in frames:
            label.configure(image=frame)
            label.update()
            time.sleep(delay)


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

        self.assets_path = os.path.join(os.path.dirname(__file__), "assets")
        
        # layout
        # self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        # self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        # self.dark_background_image = ctk.CTkImage(Image.open("C:\\Users\\user\\OneDrive - iitr.ac.in\\##Projects\\Air-Cursor\\GUI\\assets\\Backgrounds\\Dark_Theme\\Dark_sky.jpg").resize((int(self.winfo_width()), int(self.winfo_height()))))
        # self.light_background_image = ctk.CTkImage(Image.open("C:\\Users\\user\\OneDrive - iitr.ac.in\\##Projects\\Air-Cursor\\GUI\\assets\\Backgrounds\\Light_Theme\\Light_sky.jpg").resize((int(self.winfo_width()), int(self.winfo_height()))))
        # self.background_image_label = ctk.CTkLabel(self, image=self.dark_background_image, corner_radius=10)
        # self.background_image_label.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")
        # self.background_image_label.pack(expand=True, fill="both")

        # set background image
        # self.dark_background_image = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\OneDrive - iitr.ac.in\\##Projects\\Air-Cursor\\GUI\\assets\\Backgrounds\\Dark_Theme\\Dark_sky.jpg").resize(500,500))
        # self.light_background_image = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\OneDrive - iitr.ac.in\\##Projects\\Air-Cursor\\GUI\\assets\\Backgrounds\\Light_Theme\\Light_sky.jpg").resize((int(self.winfo_width()), int(self.winfo_height()))))
        # self.background_image = self.dark_background_image
        # self.background_image_label = ctk.CTkLabel(self, image=self.background_image, corner_radius=10)

        self._create_base_frame()
        # self._place_base_frame()

        # self.Configure_widget = self.create_configure_widget()
        # self.Help_widget = self.create_help_widget()
        # self.About_us_widget = self.create_About_us_widget()v
        # self.Lauch_widget = self.create_launch_widget()
        # self.Tips_widget = self.create_tips_widget()

    def create_configure_widget(self):
        configure_widget = ctk.CTkFrame(
            self,
            bg_color="transparent",
            # fg_color="",
            corner_radius=10,
        )

        # a label and a button
        label = ctk.CTkLabel(
            configure_widget,
            text="Stable and Reliable\nExperience",
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
        )
        label.place(relx=0.5, rely=0.33, relwidth=0.95, relheight=0.5, anchor="center")
        button = ctk.CTkButton(
            configure_widget,
            text="Configure",
            font=("Segoe UI", 20, "bold"),
            corner_radius=50,
            fg_color="#000001",
            command=self.configure_button_click,
        )
        button.place(relx=0.5, rely=0.8, relwidth=0.8, relheight=0.33, anchor="center")
        return configure_widget

        # self.configure_widget.grid_columnconfigure(0, weight=1)
        # self.configure_widget.grid_rowconfigure((0,1,2), weight=1)

    def create_help_widget(self):
        help_widget = ctk.CTkFrame(
            self,
            bg_color="transparent",
            # fg_color="",
            corner_radius=10,
        )

        # a label and a button
        label = ctk.CTkLabel(
            help_widget,
            text="Support and Query",
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
        )
        label.place(relx=0.5, rely=0.33, relwidth=0.95, relheight=0.66, anchor="center")
        button = ctk.CTkButton(
            help_widget,
            text="Help",
            font=("Segoe UI", 20, "bold"),
            corner_radius=50,
            fg_color="#000001",
            command=self.help_button_click,
        )
        button.place(relx=0.5, rely=0.8, relwidth=0.8, relheight=0.33, anchor="center")
        return help_widget

    def create_About_us_widget(self):
        About_us_widget = ctk.CTkFrame(
            self,
            bg_color="#000001",
            fg_color="#000001",
            # fg_color="",
            corner_radius=10,
        )
        # only a button
        ctk.CTkButton(
            About_us_widget,
            text="About us",
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
            fg_color="#000001",
            border_color="white",
            border_width=1,
            command=self.about_us_button_click,
        ).pack(expand=True, fill="both")
        return About_us_widget

    def create_launch_widget(self):
        Lauch_widget = ctk.CTkFrame(
            self,
            bg_color="transparent",
            # fg_color="red",
            corner_radius=10,
        )

        """
            Label Frame takes 2/3 of the height
            Button Frame takes 1/3 of the height
        """

        # background image
        imgPath = os.path.join(
            os.path.dirname(__file__), "Assets", "Backgrounds", "Launch_bg.jpg"
        )
        img = Image.open(imgPath)
        img_obj = ctk.CTkImage(dark_image=img, light_image=img, size=(800, 200))
        # self.img_label = ctk.CTkLabel(Lauch_widget, image=img_obj, text="", corner_radius=10)
        # self.img_label.place(relx=0.5, rely=0.5, relwidth=0.99, relheight=0.99, anchor="center")

        # self._canvas = ctk.CTkCanvas(Lauch_widget)
        # self._canvas.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")
        # self._canvas.create_image(0, 0, image=img, anchor="nw")

        # create frames

        label_frame = ctk.CTkFrame(
            Lauch_widget,
            bg_color="transparent",
            fg_color="transparent",
            corner_radius=10,
        )
        button_frame = ctk.CTkFrame(
            Lauch_widget,
            bg_color="transparent",
            fg_color="transparent",
            corner_radius=10,
        )

        # place frames
        label_frame.place(
            relx=0.5, rely=0.34, relwidth=0.95, relheight=0.66, anchor="center"
        )
        button_frame.place(
            relx=0.5, rely=0.81, relwidth=0.95, relheight=0.31, anchor="center"
        )

        catchphrases = (
            "Move it like you own it",
            "You have magic hands.\nTry moving them",
            "Magic in the air",
        )
        # label frame contains a cachphrase about the app -> "Move it like you own it"
        catchphrase_label = ctk.CTkLabel(
            label_frame,
            text="Move it like you own it",
            font=("Segoe UI", 50, "bold", "italic"),
            corner_radius=10,
            fg_color="#000001",
            bg_color="transparent",
            # image=img_obj,
            text_color="gold",
        )
        catchphrase_label.pack(expand=True, fill="both")

        def update_catcphrase():
            while True:
                new_catchphrase = choice(catchphrases)
                if new_catchphrase != catchphrase_label.cget("text"):
                    break
            catchphrase_label.configure(text=new_catchphrase)
            self.after(3000, update_catcphrase) 

        update_catcphrase()

        launch_img_path = os.path.join(self.assets_path,"Buttons", "launch_gradiant.png")
        launch_img = ctk.CTkImage(
            dark_image=Image.open(launch_img_path),
            light_image=Image.open(launch_img_path),
            size=(100,50),
        )
        
        # button frame contains two buttons
        launch_button = ctk.CTkButton(
            button_frame,
            # image=launch_img,
            text="Launch",
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
            fg_color="#000001",
            border_color="white", 
            border_width=1,
            command=self.launch_button_click,
        )
        stop_button = ctk.CTkButton(
            button_frame,
            text="Stop",
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
            fg_color="#000001",
            border_color="white",
            border_width=1,
            command=self.stop_button_click,
        )

        launch_button.place(
            relx=0.45, rely=0.1, relwidth=0.25, relheight=0.89, anchor="nw"
        )
        stop_button.place(
            relx=0.75, rely=0.1, relwidth=0.25, relheight=0.89, anchor="nw"
        )

        return Lauch_widget

    def create_tips_widget(self):
        Tips_widget = ctk.CTkFrame(
            self, bg_color="transparent", fg_color="transparent", corner_radius=10
        )
        tips = (
            "You need tips! Noob 😁",
            "Do something you lazy 🤨",
            "CG kitna hai tera? 🤭",
            "Chinta mat kar,\nbandi nahi milegi 😁",
        )
        """
            Layout: <button> <tips_content> <button>
            the left button is for previous tip and the right button is for next tip
        """
        # what is the default frame color in dark mode in customtkinter?

        left_button = ctk.CTkButton(
            Tips_widget,
            text="<",
            font=("Segoe UI", 20, "bold"),
            corner_radius=20,
            fg_color="#2b2b2b",
            hover_color="#000001",
            command=lambda: previous_tip(),
        )
        right_button = ctk.CTkButton(
            Tips_widget,
            text=">",
            font=("Segoe UI", 20, "bold"),
            corner_radius=20,
            fg_color="#2b2b2b",
            hover_color="#000001",
            command=lambda: next_tip(),
        )
        # left_button.place(relx=0.01, rely=0.01, relwidth=0.1, relheight=0.98, anchor="nw")
        # right_button.place(relx=0.89, rely=0.01, relwidth=0.1, relheight=0.98, anchor="nw")
        left_button.place(relx=0, rely=0.0, relwidth=0.1, relheight=1, anchor="nw")
        right_button.place(relx=0.9, rely=0.0, relwidth=0.1, relheight=1, anchor="nw")

        tip = tips[0]
        tips_content = ctk.CTkFrame(
            Tips_widget,
            bg_color="transparent",
            fg_color="transparent",
            corner_radius=10,
        )
        tips_content.place(
            relx=0.12, rely=0.01, relwidth=0.76, relheight=0.97, anchor="nw"
        )
        tip_label = ctk.CTkLabel(
            tips_content,
            text=tip,
            font=("Segoe UI", 30, "bold"),
            corner_radius=10,
            text_color="gold",
        )
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

    # ############## Create and place the base frame ################ #
    def _create_base_frame(self):
        self.Configure_widget = self.create_configure_widget()
        self.Help_widget = self.create_help_widget()
        self.About_us_widget = self.create_About_us_widget()
        self.Lauch_widget = self.create_launch_widget()
        self.Tips_widget = self.create_tips_widget()

        self.Configure_widget.place(
            x=1, rely=0.01, relwidth=0.25, relheight=0.39, anchor="nw"
        )
        self.Help_widget.place(
            x=1, rely=0.44, relwidth=0.25, relheight=0.38, anchor="nw"
        )
        self.About_us_widget.place(
            x=1, rely=0.86, relwidth=0.25, relheight=0.13304, anchor="nw"
        )

        self.Lauch_widget.place(
            relx=0.28, rely=0.01, relwidth=0.72, relheight=0.39, anchor="nw"
        )
        self.Tips_widget.place(
            relx=0.28, rely=0.44, relwidth=0.72, relheight=0.55, anchor="nw"
        )

    # ############## Create and place the configure page ################ #
    def _create_congigure_page(self):
        """
        <Configure content>
        <Save> <Back Button>

        COnfigure content contains:
            <Smoothneing factor slider>
            <Cursor size slider>
            <Choose camera>
        """

        # create a scrollable frame
        self.Configure_Frame = ctk.CTkScrollableFrame(
            self, 
            bg_color="transparent", 
            fg_color="transparent", 
            corner_radius=10
        )

        # variables
        self.smoothness_factor_1 = 5
        self.smoothness_factor_2 = 5
        self.camera_index = 0

        # frame 1
        frame1 = ctk.CTkFrame(
            self.Configure_Frame,
            bg_color="transparent",
            fg_color="transparent",
            corner_radius=10,
        )

        frame1.grid_rowconfigure(0, weight=1)
        frame1.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        label1 = ctk.CTkLabel(
            frame1,
            text="Smoothness Factor 1",
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
        )
        slider1 = ctk.CTkSlider(
            frame1,
            orientation="horizontal",
            corner_radius=10,
            from_=0,
            to=10,
            number_of_steps=20,
        )
        slider1.set(self.smoothness_factor_1)
        value_label1 = ctk.CTkLabel(
            frame1,
            text=(self.smoothness_factor_1),
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
        )

        label1.grid(row=0, column=0, sticky="nsew")
        slider1.grid(row=0, column=1, columnspan=3, sticky="nsew")
        value_label1.grid(row=0, column=4, sticky="nsew")

        # frame 2
        frame2 = ctk.CTkFrame(
            self.Configure_Frame,
            bg_color="transparent",
            fg_color="transparent",
            corner_radius=10,
        )
        frame2.grid_rowconfigure(0, weight=1)
        frame2.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        label2 = ctk.CTkLabel(
            frame2,
            text="Smoothness Factor 2",
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
        )
        slider2 = ctk.CTkSlider(
            frame2,
            orientation="horizontal",
            corner_radius=10,
            from_=0,
            to=10,
            number_of_steps=20,
        )
        slider2.set(self.smoothness_factor_2)
        value_label2 = ctk.CTkLabel(
            frame2,
            text=(self.smoothness_factor_2),
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
        )

        label2.grid(row=0, column=0, sticky="nsew")
        slider2.grid(row=0, column=1, columnspan=3, sticky="nsew")
        value_label2.grid(row=0, column=4, sticky="nsew")

        # frame 3
        frame3 = ctk.CTkFrame(
            self.Configure_Frame,
            bg_color="transparent",
            fg_color="transparent",
            corner_radius=10,
        )
        frame3.grid_rowconfigure(0, weight=1)
        frame3.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        label3 = ctk.CTkLabel(
            frame3,
            text="Choose Camera",
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
        )
        camera_list = ctk.CTkComboBox(
            frame3,
            hover=False,
            values=("Camera 1", "Camera 2"),
            corner_radius=10,
            font=("Segoe UI", 20, "bold"),
            fg_color="#000001",
            border_color="white",
            border_width=1,
            command=lambda event: self.camera_list_selection(event, camera_list),
        )

        label3.grid(row=0, column=0, sticky="nsew")
        camera_list.grid(row=0, column=1, columnspan=3, sticky="nsew")

        # frame 4 (buttons): <Save> <Back Button>
        frame4 = ctk.CTkFrame(
            self,
            bg_color="transparent",
            fg_color="transparent",
            corner_radius=10,
            height=100,
        )
        frame4.grid_rowconfigure(0, weight=1)
        frame4.grid_columnconfigure((0, 1), weight=1)

        save_button = ctk.CTkButton(
            frame4,
            text="Save",
            font=("Segoe UI", 20, "bold"),
            height=80,
            corner_radius=10,
            fg_color="#000001",
            border_color="white",
            border_width=1,
            command=lambda: self._save_configuration(
                smoothness_factor_1=self.smoothness_factor_1,
                smoothness_factor_2=self.smoothness_factor_2,
                camera_index=self.camera_index,
            ),
        )
        back_button = ctk.CTkButton(
            frame4,
            text="Back",
            font=("Segoe UI", 20, "bold"),
            height=80,
            corner_radius=10,
            fg_color="#000001",
            border_color="white",
            border_width=1,
            command=lambda: self._back_from_configure_page(),
        )

        save_button.grid(row=0, column=0, sticky="nsew", padx=10)
        back_button.grid(row=0, column=1, sticky="nsew", padx=10)

        # remove all the widgets from the base frame
        for widget in self.winfo_children():
            widget.place_forget()

        self.Configure_Frame.place(
            relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center"
        )
        # place the frames
        frame1.pack(expand=True, fill="both", pady=20)
        frame2.pack(expand=True, fill="both", pady=20)
        frame3.pack(expand=True, fill="both", pady=50)
        frame4.place(rely=1, relwidth=0.95, anchor="sw")

        # slider1.bind("<ButtonRelease-1>", lambda event: self.smoothness_factor_slider_release(event, slider1, value_label1, factor=1))
        # slider2.bind("<ButtonRelease-1>", lambda event: self.smoothness_factor_slider_release(event, slider2, value_label2, factor=2))

        slider1.configure(
            command=lambda event: self.smoothness_factor_slider_release(
                event, slider1, value_label1, factor=1
            )
        )
        slider2.configure(
            command=lambda event: self.smoothness_factor_slider_release(
                event, slider2, value_label2, factor=2
            )
        )

    def smoothness_factor_slider_release(self, event, slider, value_label, factor):
        value = slider.get()
        value_label.configure(text=value)
        if factor == 1:
            self.smoothness_factor_1 = value
        elif factor == 2:
            self.smoothness_factor_2 = value

    def camera_list_selection(self, event, camera_list):
        if camera_list.get() == "Camera 1":
            self.camera_index = 0
        elif camera_list.get() == "Camera 2":
            self.camera_index = 1

    # ############# Create and place the About us page ################ #
    def _create_about_us_page(self):
        """
        <About us content>
        <Back Button>
        
        About us content contains:
            <Developers>
            <Contributors>
            <Contact us>
        
        There are 5 developers and no contributors, but we have mentioned the names of the people who helped us in the project.
        Developers contains:
            <Photo> <Name> <Email> <Github> <LinkedIn>
        """
        # create a scrollable frame
        self.About_us_Frame = ctk.CTkScrollableFrame(
            self, bg_color="transparent", fg_color="transparent", corner_radius=10
        )
        
        Developers_img_path = os.path.join(os.path.dirname(__file__), "Assets", "Developers")
        Panda_img_path = os.path.join(Developers_img_path, "Panda.jpg")
        Souvik_img_path = os.path.join(Developers_img_path, "Souvik.jpg")
        Sukhman_img_path = os.path.join(Developers_img_path, "Sukhman.jpg")
        
        
        
        # frame 1 -> developer 1 (Souvik)
        souvik_frame = self.create_developer_frame(
            self.About_us_Frame,
            img_path=Panda_img_path,
            name="Souvik Karmakar",
            email="souvik_k@cs.iitr.ac.in",
            github="https://github.com/souvik-13",
            linkedin="https://www.linkedin.com/in/souvik-karmakar-888202257/",
            side="left"
        )
        
        # frame 2 -> developer 2 (Raman)
        raman_frame = self.create_developer_frame(
            self.About_us_Frame,
            img_path=Panda_img_path,
            name="Raman Sharma",
            email="raman_s@cs.iitr.ac.in",
            github="https://github.com/ramansharma829455",
            linkedin="https://www.linkedin.com/in/raman-sharma-8294551b7/",
            side="right"
        )
        
        # frame 3 -> developer 3 (Yash)
        yashwanth_frame = self.create_developer_frame(
            self.About_us_Frame,
            img_path=Panda_img_path,
            name="Boda Yashwanth",
            email="boda_y@cs.iitr.ac.in",
            github="https://github.com/yashwanthboda",
            linkedin="https://www.linkedin.com/in/yashwanth-boda-3a2a1b1b9/",
            side="left"
        )
        
        # frame 4 -> developer 4 (Sukhman)
        sukhman_frame = self.create_developer_frame(
            self.About_us_Frame,
            img_path=Panda_img_path,
            name="Sukhman Singh",
            email="sukhman_s@cs.iitr.ac.in",
            github="https://github.com/sukhman-sukh",
            linkedin="https://www.linkedin.com/in/sukhman-singh-3a6a1b1b9/",
            side="right"
        )
        # frame 5 -> developer 5 (Ayush)
        ayush_frame = self.create_developer_frame(
            self.About_us_Frame,
            img_path=Panda_img_path,
            name="Ayush Ranjan",
            email="ayush_r@cs.iitr.ac.in",
            github="https://github.com/ayushr100",
            linkedin="https://www.linkedin.com/in/ayush-ranjan-3a6a1b1b9/",
            side="left"
        )
        
        self.back_button_image = ctk.CTkImage(
            dark_image=Image.open(os.path.join(os.path.dirname(__file__), "Assets", "Buttons", "arrow_white.png")),
            light_image=Image.open(os.path.join(os.path.dirname(__file__), "Assets", "Buttons", "arrow_black.png")),
            size=(50, 50),
        )
        
        # back button
        back_button = ctk.CTkButton(
            self,
            text="",
            image=self.back_button_image,
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
            fg_color="transparent",
            bg_color="transparent",
            # border_color="white",
            # border_width=1,
            command=lambda: self._back_from_about_us_page(),
            height=50,
            width=50,
        )
        
        # remove all the widgets from the base frame
        for widget in self.winfo_children():
            widget.place_forget()
            
        # place the about us frame
        back_button.place(relx=0.01, rely=0.01,  anchor="nw")
        # self.About_us_Frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")
        self.About_us_Frame.place(x=50, y=50, relwidth=0.95, relheight=0.95, anchor="nw")
        
        # pack the frames
        souvik_frame.pack(expand=True, fill="both", pady=20, padx=20)
        raman_frame.pack(expand=True, fill="both", pady=20, padx=20)
        yashwanth_frame.pack(expand=True, fill="both", pady=20, padx=20)
        sukhman_frame.pack(expand=True, fill="both", pady=20, padx=20)
        ayush_frame.pack(expand=True, fill="both", pady=20, padx=20)
        

    def create_developer_frame(self, parent, img_path, name, email, github, linkedin, side):
        developer_frame = ctk.CTkFrame(
            parent,
            # bg_color="transparent",
            # fg_color="transparent",
            corner_radius=20,
        )

        developer_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        developer_frame.grid_columnconfigure((0, 1, 2), weight=1)

        developer_photo = ctk.CTkImage(
            dark_image=Image.open(img_path),
            light_image=Image.open(img_path),
            size=(200, 200),
        )

        developer_photo_label = ctk.CTkLabel(
            developer_frame, 
            image=developer_photo, 
            corner_radius=10, 
            text="",
            fg_color="transparent",
            bg_color="transparent"
        )
        developer_name_label = ctk.CTkLabel(
            developer_frame,
            text=name,
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
        )
        developer_email_label = ctk.CTkLabel(
            developer_frame,
            text=email,
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
        )
        developer_github_label = ctk.CTkLabel(
            developer_frame,
            text=github,
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
        )
        developer_linkedin_label = ctk.CTkLabel(
            developer_frame,
            text=linkedin,
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
        )

        # place the widgets
        if side == "left":
            developer_photo_label.grid(row=0, column=0, rowspan=4, sticky="nswe")
            developer_name_label.grid(row=0, column=1, columnspan=2, sticky="e", padx=50, pady=(20,0))
            developer_email_label.grid(row=1, column=1, columnspan=2, sticky="e", padx=50)
            developer_github_label.grid(row=2, column=1, columnspan=2, sticky="e", padx=50)
            developer_linkedin_label.grid(row=3, column=1, columnspan=2, sticky="e", padx=50, pady=(0,20))
        elif side == "right":
            developer_photo_label.grid(row=0, column=3, rowspan=4, sticky="nswe")
            developer_name_label.grid(row=0, column=0, columnspan=2, sticky="w",padx=50, pady=(20,0))
            developer_email_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=50)
            developer_github_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=50)
            developer_linkedin_label.grid(row=3, column=0, columnspan=2, sticky="w", padx=50, pady=(0,20))
            
        
        return developer_frame
           
    
    # button click functions
    
    # ############### Configure page button click functions ################ #
    def configure_button_click(self):
        self._create_congigure_page()

    def _save_configuration(
        self, smoothness_factor_1, smoothness_factor_2, camera_index
    ):
        # save the configuration and go back to the base frame
        os.environ['SF1']=smoothness_factor_1;
        os.environ['SF2']=smoothness_factor_2;
        os.environ['CAMERA_INDEX']=camera_index;
        self._back_from_configure_page()

    def _back_from_configure_page(self):
        # remove all the widgets from the base frame
        for widget in self.winfo_children():
            widget.place_forget()
        self._create_base_frame()

    def help_button_click(self):
        # self.Help_widget.destroy()
        # self.Help_widget = self.create_help_widget()
        # self.Help_widget.place(x=1,rely=0.44,relwidth=0.25,relheight=0.38, anchor="nw")
        pass

    # ############### About us page button click functions ################ #
    def about_us_button_click(self):
        self._create_about_us_page()
    
    def _back_from_about_us_page(self):
        # remove all the widgets from the base frame
        for widget in self.winfo_children():
            widget.place_forget()
        self._create_base_frame()

    def launch_button_click(self):
        # os.system("cd ./../")
        os.chdir("..") 
        print(os.getcwd())
        os.system("echo \"sad\"")
        os.system("python3 control_latest.py")
        # with open("C:\scripts\other.py") as f:
        #     exec(f.read())

    def stop_button_click(self):
        sys.exit()


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
        self.width = 600
        self.height = 400
        self.x = int((self.winfo_screenwidth() - self.width) // 2)
        self.y = int((self.winfo_screenheight() - self.height) // 2)
        # self.overrideredirect(True)
        # self.resizable(resizeable, resizeable)

        # set icon
        if iconPath:
            self.iconbitmap(iconPath)

        # set title
        self.title("Air Cursor")

        transparent_color = self._apply_appearance_mode(["white", "#000001"])
        # layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)  # 0 is titlebar, 1 is base
        self.grid_rowconfigure(1, weight=1)

        self.config(background=transparent_color)

        # Splash Screen
        # self.Splash_Frame = SplashFrame(self, width=600, height=400, bg_color="white", border_width=0, border_color="black", fg_color="black")

        # base frame
        self.Base_Frame = Base(
            self,
            bg_color=("white", "#000001"),
            fg_color=("white", "#000001"),
            # border_width=0,
            corner_radius=10,
        )

        # self.Base_Frame.place(x=1,y=title_height, relwidth=1, relheight=1)
        # self.Base_Frame.place(relx=0.5,rely=0.5, relwidth=0.97, relheight=0.97, anchor="center")
        # self.app.bind("<Map>", self.frame_mapped)

        # self.show_splash()
        # self.update()
        # self.after(5640, self.show_main)
        self.show_main()

    def show_splash(self):
        # make the window appear on the top
        self.attributes("-topmost", True)
        self.overrideredirect(True)
        self.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.Splash_Frame.pack(expand=True, fill="both")

    def show_main(self):
        # self.Splash_Frame.pack_forget()
        self.attributes("-topmost", False)
        self.overrideredirect(False)
        self.width = 1000
        self.height = int(self.width * 9 / 16)
        self.geometry(f"{self.width}x{self.height}")
        self.Base_Frame.place(
            relx=0.5, rely=0.5, relwidth=0.97, relheight=0.97, anchor="center"
        )


#  run the app
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
