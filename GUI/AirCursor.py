from __future__ import annotations
import sys
import time
from typing import Tuple
import customtkinter as ctk
from PIL import Image
import cv2
import os
from random import choice


# Configuration variables
# global Smoothing_factor_1
# global Smoothing_factor_2
# global Camera_index


def _get_frames(img):
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


def play_gif(frames, label, delay=0.04):
    for frame in frames:
        label.configure(image=frame)
        label.update()
        time.sleep(delay)


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

        self.label_gif1 = None
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

        self.gif1_frames = _get_frames(Rain_gif)

        # self.label_gif1.configure(image = self.gif1_frames[12])

        # self.play_gif(self.gif1_frames, self.label_gif1)

        self.master.after(
            1000, lambda: play_gif(self.gif1_frames, self.label_gif1)
        )


def create_developer_frame(parent, img_path, name, email, github, linkedin, side):
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
        font=("Segoe UI", 25, "bold"),
        corner_radius=10,
    )
    developer_email_label = ctk.CTkLabel(
        developer_frame,
        text=email,
        font=("Segoe UI", 15),
        corner_radius=10,
    )
    developer_github_label = ctk.CTkLabel(
        developer_frame,
        text=github,
        font=("Segoe UI", 15),
        corner_radius=10,
    )
    developer_linkedin_label = ctk.CTkLabel(
        developer_frame,
        text=linkedin,
        font=("Segoe UI", 15),
        corner_radius=10,
    )

    # place the widgets
    if side == "left":
        developer_photo_label.grid(row=0, column=0, rowspan=4, sticky="nswe")
        developer_name_label.grid(row=0, column=1, columnspan=2, sticky="e", padx=50, pady=(20, 0))
        developer_email_label.grid(row=1, column=1, columnspan=2, sticky="e", padx=50)
        developer_github_label.grid(row=2, column=1, columnspan=2, sticky="e", padx=50)
        developer_linkedin_label.grid(row=3, column=1, columnspan=2, sticky="e", padx=50, pady=(0, 20))
    elif side == "right":
        developer_photo_label.grid(row=0, column=3, rowspan=4, sticky="nswe")
        developer_name_label.grid(row=0, column=0, columnspan=2, sticky="w", padx=50, pady=(20, 0))
        developer_email_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=50)
        developer_github_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=50)
        developer_linkedin_label.grid(row=3, column=0, columnspan=2, sticky="w", padx=50, pady=(0, 20))

    return developer_frame


def stop_button_click():
    sys.exit()


def launch_button_click():
    # os.system("cd ./../")
    os.chdir("..")
    print(os.getcwd())
    os.system("echo \"sad\"")
    os.system("python control.py")
    # with open("C:\scripts\other.py") as f:
    #     exec(f.read())


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
            theme: str = "dark",
            camera_index: int = 0,
            smoothness_factor_2: int = 10,
            smoothness_factor_1: int = 10,
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

        self.master = master
        self.theme = theme
        self.camera_index = camera_index
        self.smoothness_factor_2 = smoothness_factor_2
        self.smoothness_factor_1 = smoothness_factor_1
        self.assets_path = os.path.join(os.path.dirname(__file__), "assets")

        self._create_base_frame()

        # self.Configure_widget = self.create_configure_widget()
        # self.Help_widget = self.create_help_widget()
        # self.About_us_widget = self.create_About_us_widget()v
        # self.Lauch_widget = self.create_launch_widget()
        # self.Tips_widget = self.create_tips_widget()

    def create_configure_widget(self):
        configure_widget = ctk.CTkFrame(
            self,
            bg_color="transparent",
            fg_color=("#92BBAF", "#374A44"),
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
            fg_color=("#647E76", "#647E76"),
            hover_color=("#4A5F59", "#7C9F94"),
            command=self.configure_button_click,
        )
        button.place(relx=0.5, rely=0.79, relwidth=0.9, relheight=0.30, anchor="center")
        # button.bind("<Enter>", lambda event: button.configure(fg_color="#D4ADFC"))
        # button.bind("<Leave>", lambda event: button.configure(fg_color="#5C469C"))
        return configure_widget

        # self.configure_widget.grid_columnconfigure(0, weight=1)
        # self.configure_widget.grid_rowconfigure((0,1,2), weight=1)

    def create_help_widget(self):
        help_widget = ctk.CTkFrame(
            self,
            bg_color="transparent",
            fg_color=("#29465B", "#243745"),
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
            fg_color=("#8C9CB4", "#969B85"),
            hover_color=("#68768C", "#CFDAB0"),
            bg_color="transparent",
            command=self.help_button_click,
        )
        button.place(relx=0.5, rely=0.79, relwidth=0.9, relheight=0.30, anchor="center")

        # button.bind("<Enter>", lambda event: button.configure(image=arrow_img))
        # button.bind("<Leave>", lambda event: button.configure(image=launch_img))

        return help_widget

    def create_About_us_widget(self):
        About_us_widget = ctk.CTkFrame(
            self,
            bg_color="transparent",
            fg_color="transparent",
            # fg_color=("#58563F", "#344F32"),
            # fg_color="",
            corner_radius=10,
        )
        # only a button
        ctk.CTkButton(
            About_us_widget,
            text="About us",
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
            bg_color="transparent",
            fg_color=("#7E7B59", "#344F32"),
            hover_color=("#58563F", "#4E724B"),
            command=self.about_us_button_click,
        ).pack(expand=True, fill="both")
        return About_us_widget

    def create_launch_widget(self):
        Lauch_widget = ctk.CTkFrame(
            self,
            bg_color="transparent",
            fg_color=("#ABA67B", "#36352A"),
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
            relx=0.5, rely=0.81, relwidth=1, relheight=0.31, anchor="center"
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
            fg_color="transparent",
            bg_color="transparent",
            # image=img_obj,
            text_color=("#654B32", "#CFA58E")
        )
        catchphrase_label.pack(fill="both", side="left")

        def update_catcphrase():
            while True:
                new_catchphrase = choice(catchphrases)
                if new_catchphrase != catchphrase_label.cget("text"):
                    break
            catchphrase_label.configure(text=new_catchphrase)
            self.after(3000, update_catcphrase)

        update_catcphrase()

        launch_img_path = os.path.join(self.assets_path, "Buttons", "launch_gradiant.png")
        launch_img = ctk.CTkImage(
            dark_image=Image.open(launch_img_path),
            light_image=Image.open(launch_img_path),
            size=(100, 50),
        )

        # button frame contains two buttons
        launch_button = ctk.CTkButton(
            button_frame,
            # image=launch_img,
            text="Launch",
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
            bg_color="transparent",
            fg_color=("#648C60", "#32532F"),
            hover_color=("#32532F", "#648C60"),
            command=launch_button_click,
        )
        stop_button = ctk.CTkButton(
            button_frame,
            text="Stop",
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
            bg_color="transparent",
            fg_color=("#E65151", "#6D3030"),
            hover_color=("#6D3030", "#E65151"),
            # border_color="white",
            # border_width=1,
            command=stop_button_click,
        )

        stop_button.place(
            relx=0.36, rely=0.1, relwidth=0.3, relheight=0.89, anchor="nw"
        )
        launch_button.place(
            relx=0.68, rely=0.1, relwidth=0.3, relheight=0.89, anchor="nw"
        )

        return Lauch_widget

    def create_tips_widget(self):
        Tips_widget = ctk.CTkFrame(
            self, bg_color="transparent", fg_color="transparent", corner_radius=10
        )
        # tips = (
        #     "You need tips! Noob 😁",
        #     "Do something you lazy 🤨",
        #     "CG kitna hai tera? 🤭",
        #     "Chinta mat kar,\nbandi nahi milegi 😁",
        # )
        """
            Layout: <button> <tips_content> <button>
            the left button is for previous tip and the right button is for next tip
        """
        # what is the default frame color in dark mode in customtkinter?

        left_button_img_path = os.path.join(self.assets_path, "Buttons", "left_tip.png")
        right_button_img_path = os.path.join(self.assets_path, "Buttons", "right_tip.png")

        left_button_img = ctk.CTkImage(
            dark_image=Image.open(left_button_img_path),
            light_image=Image.open(left_button_img_path),
            size=(50, 50),
        )
        right_button_img = ctk.CTkImage(
            dark_image=Image.open(right_button_img_path),
            light_image=Image.open(right_button_img_path),
            size=(50, 50),
        )

        left_button = ctk.CTkButton(
            Tips_widget,
            text="",
            image=left_button_img,
            font=("Segoe UI", 20, "bold"),
            corner_radius=20,
            bg_color="transparent",
            fg_color="transparent",
            hover_color=("#89A6A6", "#2E4343"),
            command=lambda: previous_tip(),
        )
        right_button = ctk.CTkButton(
            Tips_widget,
            text="",
            image=right_button_img,
            font=("Segoe UI", 20, "bold"),
            corner_radius=20,
            bg_color="transparent",
            fg_color="transparent",
            hover_color=("#89A6A6", "#2E4343"),
            command=lambda: next_tip(),
        )
        # left_button.place(relx=0.01, rely=0.01, relwidth=0.1, relheight=0.98, anchor="nw")
        # right_button.place(relx=0.89, rely=0.01, relwidth=0.1, relheight=0.98, anchor="nw")
        left_button.place(relx=0, rely=0.0, relwidth=0.1, relheight=1, anchor="nw")
        right_button.place(relx=0.9, rely=0.0, relwidth=0.1, relheight=1, anchor="nw")

        tip_img_path_1 = os.path.join(self.assets_path, "Tips", "tip_1.png")
        tip_img_1 = ctk.CTkImage(
            dark_image=Image.open(tip_img_path_1),
            light_image=Image.open(tip_img_path_1),
            size=(700, 300),
        )

        tips = [tip_img_1]
        tip = choice(tips)

        tips_content = ctk.CTkFrame(
            Tips_widget,
            bg_color="transparent",
            fg_color=("#89A6A6", "#2E4343"),
            corner_radius=10,
        )
        tips_content.place(
            relx=0.12, rely=0.01, relwidth=0.76, relheight=0.99, anchor="nw"
        )
        tip_label = ctk.CTkLabel(
            tips_content,
            # text=tip,
            text="",
            image=tip,
            bg_color="transparent",
            fg_color="transparent",
            font=("Segoe UI", 30, "bold"),
            corner_radius=10,
            # text_color="gold",
        )
        tip_label.place(relx=0.5, rely=0.5, relwidth=0.99, relheight=0.99, anchor="center")

        def previous_tip():
            i = tips.index(tip)
            if i == 0:
                i = len(tips) - 1
            else:
                i -= 1
            tip_label.configure(image=tips[i])

        def next_tip():
            i = tips.index(tip)
            if i == len(tips) - 1:
                i = 0
            else:
                i += 1
            tip_label.configure(image=tips[i])

        return Tips_widget

    # ############## Create and place the base frame ################ #
    def _create_base_frame(self):
        self.Configure_widget = self.create_configure_widget()
        self.Help_widget = self.create_help_widget()
        self.About_us_widget = self.create_About_us_widget()
        self.Launch_widget = self.create_launch_widget()
        self.Tips_widget = self.create_tips_widget()

        self.Configure_widget.place(
            relx=0.02, rely=0.03, relwidth=0.25, relheight=0.39, anchor="nw"
        )
        self.Help_widget.place(
            relx=0.02, rely=0.448, relwidth=0.25, relheight=0.38, anchor="nw"
        )
        self.About_us_widget.place(
            relx=0.02, rely=0.85, relwidth=0.25, relheight=0.13, anchor="nw"
        )
        self.Launch_widget.place(
            relx=0.286, rely=0.03, relwidth=0.7, relheight=0.39, anchor="nw"
        )
        self.Tips_widget.place(
            relx=0.286, rely=0.448, relwidth=0.7, relheight=0.53, anchor="nw"
        )

    # ############## Create and place the configure page ################ #
    def _create_configure_page(self):
        """
        <Configure content>
        <Save> <Back Button>

        Configure content contains:
            <Smoothness factor slider>
            <Cursor size slider>
            <Choose camera>
            <Show the camera feed>
        """

        # create a scrollable frame
        self.Configure_Frame = ctk.CTkScrollableFrame(
            self,
            bg_color="transparent",
            fg_color="transparent",
            corner_radius=10
        )

        # frame 1 (smoothness factor 1)
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
            font=("Segoe UI", 22, "bold"),
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
            text=f"{self.smoothness_factor_1}",
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
        )

        label1.grid(row=0, column=0, sticky="nsew")
        slider1.grid(row=0, column=1, columnspan=3, sticky="nsew")
        value_label1.grid(row=0, column=4, sticky="nsew")

        # frame 2 (smoothness factor 2)
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
            font=("Segoe UI", 22, "bold"),
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
            text=f"{self.smoothness_factor_2}",
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
        )

        label2.grid(row=0, column=0, sticky="nsew")
        slider2.grid(row=0, column=1, columnspan=3, sticky="nsew")
        value_label2.grid(row=0, column=4, sticky="nsew")

        # frame 3 (theme selection)
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
            text="Choose Theme",
            font=("Segoe UI", 22, "bold"),
            corner_radius=10,
        )
        theme_list = ctk.CTkOptionMenu(
            frame3,
            hover=False,
            values=["Dark", "Light", "System"],
            height=40,
            corner_radius=10,
            bg_color="transparent",
            fg_color=("#89A6A6", "#2E4343"),
            dropdown_fg_color=("#89A6A6", "#2E4343"),
            dropdown_hover_color=("#89A6A6", "#2E4343"),
            command=lambda event: self.theme_list_selection(event, theme_list),
        )
        theme_list.set(self.theme)

        label3.grid(row=0, column=0, sticky="nsew")
        theme_list.grid(row=0, column=1, columnspan=3, sticky="nsew")

        # frame 4 (choose camera)
        frame4 = ctk.CTkFrame(
            self.Configure_Frame,
            bg_color="transparent",
            fg_color="transparent",
            corner_radius=10,
        )
        frame4.grid_rowconfigure(0, weight=1)
        frame4.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        label4 = ctk.CTkLabel(
            frame4,
            text="Choose Camera",
            font=("Segoe UI", 22, "bold"),
            corner_radius=10,
        )
        camera_list = ctk.CTkOptionMenu(
            frame4,
            hover=False,
            height=40,
            values=["Camera 1", "Camera 2"],
            corner_radius=10,
            bg_color="transparent",
            fg_color=("#89A6A6", "#2E4343"),
            dropdown_fg_color=("#89A6A6", "#2E4343"),
            dropdown_hover_color=("#89A6A6", "#2E4343"),
            command=lambda event: self.camera_list_selection(event, camera_list),
        )
        camera_list.set(f"Camera {self.camera_index+1}")

        label4.grid(row=0, column=0, sticky="nsew")
        camera_list.grid(row=0, column=1, columnspan=3, sticky="nsew")

        # frame 5 (buttons): <Save> <Back Button>
        frame5 = ctk.CTkFrame(
            self,
            bg_color="transparent",
            fg_color="transparent",
            corner_radius=10,
            height=100,
        )
        frame5.grid_rowconfigure(0, weight=1)
        frame5.grid_columnconfigure((0, 1), weight=1)

        save_button = ctk.CTkButton(
            frame5,
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
            frame5,
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

        # frame 5

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
        frame4.pack(expand=True, fill="both", pady=50)
        frame5.place(rely=1, relwidth=0.95, anchor="sw")
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

    def theme_list_selection(self, event, theme_list):
        if theme_list.get() == "Dark":
            self.theme = "dark"
        elif theme_list.get() == "Light":
            self.theme = "light"
        elif theme_list.get() == "System":
            self.theme = "system"
        self.master.change_theme(self.theme)

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
        souvik_frame = create_developer_frame(
            self.About_us_Frame,
            img_path=Panda_img_path,
            name="Souvik Karmakar",
            email="souvik_k@cs.iitr.ac.in",
            github="https://github.com/souvik-13",
            linkedin="https://www.linkedin.com/in/souvik-karmakar-888202257/",
            side="left"
        )

        # frame 2 -> developer 2 (Raman)
        raman_frame = create_developer_frame(
            self.About_us_Frame,
            img_path=Panda_img_path,
            name="Raman Sharma",
            email="raman_s@cs.iitr.ac.in",
            github="https://github.com/ramansharma829455",
            linkedin="https://www.linkedin.com/in/raman-sharma-8294551b7/",
            side="right"
        )

        # frame 3 -> developer 3 (Yash)
        yashwanth_frame = create_developer_frame(
            self.About_us_Frame,
            img_path=Panda_img_path,
            name="Boda Yashwanth",
            email="boda_y@cs.iitr.ac.in",
            github="https://github.com/yashwanthboda",
            linkedin="https://www.linkedin.com/in/yashwanth-boda-3a2a1b1b9/",
            side="left"
        )

        # frame 4 -> developer 4 (Sukhman)
        sukhman_frame = create_developer_frame(
            self.About_us_Frame,
            img_path=Panda_img_path,
            name="Sukhman Singh",
            email="sukhman_s@cs.iitr.ac.in",
            github="https://github.com/sukhman-sukh",
            linkedin="https://www.linkedin.com/in/sukhman-singh-3a6a1b1b9/",
            side="right"
        )
        # frame 5 -> developer 5 (Ayush)
        ayush_frame = create_developer_frame(
            self.About_us_Frame,
            img_path=Panda_img_path,
            name="Ayush Ranjan",
            email="ayush_r@cs.iitr.ac.in",
            github="https://github.com/ayushr100",
            linkedin="https://www.linkedin.com/in/ayush-ranjan-b363a7250",
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
        back_button.place(relx=0.01, rely=0.01, anchor="nw")
        # self.About_us_Frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")
        self.About_us_Frame.place(x=50, y=50, relwidth=0.95, relheight=0.95, anchor="nw")

        # pack the frames
        souvik_frame.pack(expand=True, fill="both", pady=20, padx=20)
        raman_frame.pack(expand=True, fill="both", pady=20, padx=20)
        yashwanth_frame.pack(expand=True, fill="both", pady=20, padx=20)
        sukhman_frame.pack(expand=True, fill="both", pady=20, padx=20)
        ayush_frame.pack(expand=True, fill="both", pady=20, padx=20)

    # button click functions

    # ############### Configure page button click functions ################ #
    def configure_button_click(self):
        self._create_configure_page()

    def _save_configuration(
            self, smoothness_factor_1, smoothness_factor_2, camera_index
    ):
        # save the configuration and go back to the base frame
        self._back_from_configure_page()

    def _back_from_configure_page(self):
        # remove all the widgets from the base frame
        for widget in self.winfo_children():
            widget.place_forget()
        self._create_base_frame()

    def help_button_click(self):
        pass

    # ############### About us page button click functions ################ #
    def about_us_button_click(self):
        self._create_about_us_page()

    def _back_from_about_us_page(self):
        # remove all the widgets from the base frame
        for widget in self.winfo_children():
            widget.place_forget()
        self._create_base_frame()


class MainWindow(ctk.CTk):
    def __init__(
            self,
            fg_color: str | Tuple[str, str] | None = None,
            icon_path: str = None,  # path to icon
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
        if icon_path:
            self.iconbitmap(icon_path)

        # set title
        self.title("Air Cursor")

        background_color = self._apply_appearance_mode(["#B8D8D8", "#152E2E"])
        # layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)  # 0 is titlebar, 1 is base
        self.grid_rowconfigure(1, weight=1)

        self.config(background=background_color)

        # Splash Screen
        # self.Splash_Frame = SplashFrame(self, width=600, height=400, bg_color="white", border_width=0,
        #                                 border_color="black", fg_color="black")

        # base frame
        self.Base_Frame = Base(
            self,
            bg_color=("#B8D8D8", "#152E2E"),
            fg_color=("#B8D8D8", "#152E2E"),
            # border_width=0,
            corner_radius=10,
            smoothness_factor_1=7,
            smoothness_factor_2=5,
            camera_index=0,
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
            relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center"
        )

    def change_theme(self, theme):
        self.Base_Frame.theme = theme
        ctk.set_appearance_mode(theme)
        self.config(background=self._apply_appearance_mode(["#B8D8D8", "#152E2E"]))


#  run the app
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
