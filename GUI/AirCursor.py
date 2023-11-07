from __future__ import annotations
import sys
import time
import subprocess
from typing import Tuple
import customtkinter as ctk
from PIL import Image
import cv2
import os
from random import choice
import webbrowser
import atexit

global p
p=None
file_path = "./config.txt"


def on_exit():
    # print("endinggggggggg")
    stop_button_click()
    # print("sadasdas")


atexit.register(on_exit)


def _get_frames(img):
    height = 400
    width = int(height * 1.6)
    with Image.open(img) as gif:
        index = 0
        frames = []
        while True:
            try:
                gif.seek(index)
                frame = ctk.CTkImage(
                    light_image=gif.copy(), dark_image=gif.copy(), size=(width, height)
                )
                frames.append(frame)
            except EOFError:
                break
            index += 1
    return frames


def play_gif(frames, label, delay=0.005):
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
        self.label_gif1 = ctk.CTkLabel(
            self,
            bg_color="transparent",
            fg_color="transparent",
            text="",
            corner_radius=20,
            width=int(400*1.6), height=400
        )
        self.pack(expand=True, fill="both")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.create_wdgets()

    def create_wdgets(self):
        

        self.label_gif1.grid(row=0, column=0, sticky="nsew")

        workspace = os.path.dirname(__file__)
        assets = os.path.join(workspace, "Assets")
        Splash_Animation = os.path.join(assets, "Splash_Animation")
        air_animation = os.path.join(Splash_Animation, "air_animation.gif")
        self.gif1_frames = _get_frames(air_animation)
        self.master.after(
            1000, lambda: play_gif(self.gif1_frames, self.label_gif1)
        )


def create_developer_frame(parent, img_path, name, role, email, github, linkedin, instagram, phone, side):
    developer_frame = ctk.CTkFrame(
        parent,
        bg_color="transparent",
        fg_color=("#89A6A6", "#2E4343"),
        corner_radius=20,
    )

    developer_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
    developer_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

    developer_frame.bind("<Configure>", lambda event: get_size(event))
    width = 350
    height = 200

    def get_size(event):
        width = event.width
        height = event.height

    width = width * 0.70
    # height = width

    developer_photo = ctk.CTkImage(
        dark_image=Image.open(img_path),
        light_image=Image.open(img_path),
        size=(width, width),
    )

    brand_icons = os.path.join(os.path.dirname(__file__), "Assets", "Brand_icons")
    github_img = ctk.CTkImage(
        dark_image=Image.open(os.path.join(brand_icons, "github_dark.png")),
        light_image=Image.open(os.path.join(brand_icons, "github_light.png")),
        size=(20, 20),
    )
    gmail_img = ctk.CTkImage(
        dark_image=Image.open(os.path.join(brand_icons, "gmail_dark.png")),
        light_image=Image.open(os.path.join(brand_icons, "gmail_light.png")),
        size=(20, 20),
    )
    linkedin_img = ctk.CTkImage(
        dark_image=Image.open(os.path.join(brand_icons, "linkedin_dark.png")),
        light_image=Image.open(os.path.join(brand_icons, "linkedin_light.png")),
        size=(20, 20),
    )
    instagram_img = ctk.CTkImage(
        dark_image=Image.open(os.path.join(brand_icons, "instagram_dark.png")),
        light_image=Image.open(os.path.join(brand_icons, "instagram_light.png")),
        size=(20, 20),
    )
    phone_img = ctk.CTkImage(
        dark_image=Image.open(os.path.join(brand_icons, "phone_dark.png")),
        light_image=Image.open(os.path.join(brand_icons, "phone_light.png")),
        size=(20, 20),
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
    developer_contribution = ctk.CTkTextbox(
        developer_frame,
        font=("Segoe UI", 15, 'bold'),
        corner_radius=10,
        bg_color="transparent",
        fg_color="transparent",
        wrap="word",
    )
    developer_contribution.insert("1.0", role)
    developer_contribution.configure(state="disabled")
    developer_email_label = ctk.CTkLabel(
        developer_frame,
        text="",
        image=gmail_img,
        bg_color="transparent",
        fg_color="transparent",
        font=("Segoe UI", 15),
        corner_radius=10,
    )
    developer_github_label = ctk.CTkLabel(
        developer_frame,
        text="",
        image=github_img,
        bg_color="transparent",
        fg_color="transparent",
        font=("Segoe UI", 15),
        corner_radius=10,
    )
    developer_linkedin_label = ctk.CTkLabel(
        developer_frame,
        text="",
        image=linkedin_img,
        bg_color="transparent",
        fg_color="transparent",
        font=("Segoe UI", 15),
        corner_radius=10,
    )
    developer_phone_label = ctk.CTkLabel(
        developer_frame,
        text="",
        image=phone_img,
        bg_color="transparent",
        fg_color="transparent",
        font=("Segoe UI", 15),
        corner_radius=10,
    )
    developer_instagram_label = ctk.CTkLabel(
        developer_frame,
        text="",
        image=instagram_img,
        bg_color="transparent",
        fg_color="transparent",
        font=("Segoe UI", 15),
        corner_radius=10,
    )

    developer_email_label.bind("<Enter>", lambda event: onHover(event, developer_email_label))
    developer_email_label.bind("<Leave>", lambda event: onLeave(event, developer_email_label))
    developer_email_label.bind("<Button-1>", lambda event: webbrowser.open_new_tab("mailto:" + email))

    developer_github_label.bind("<Enter>", lambda event: onHover(event, developer_github_label))
    developer_github_label.bind("<Leave>", lambda event: onLeave(event, developer_github_label))
    developer_github_label.bind("<Button-1>", lambda event: webbrowser.open_new_tab(github))

    developer_linkedin_label.bind("<Enter>", lambda event: onHover(event, developer_linkedin_label))
    developer_linkedin_label.bind("<Leave>", lambda event: onLeave(event, developer_linkedin_label))
    developer_linkedin_label.bind("<Button-1>", lambda event: webbrowser.open_new_tab(linkedin))

    developer_phone_label.bind("<Enter>", lambda event: onHover(event, developer_phone_label))
    developer_phone_label.bind("<Leave>", lambda event: onLeave(event, developer_phone_label))
    developer_phone_label.bind("<Button-1>", lambda event: webbrowser.open_new_tab("tel:" + str(phone)))

    developer_instagram_label.bind("<Enter>", lambda event: onHover(event, developer_instagram_label))
    developer_instagram_label.bind("<Leave>", lambda event: onLeave(event, developer_instagram_label))
    developer_instagram_label.bind("<Button-1>", lambda event: webbrowser.open_new_tab(instagram))

    def onHover(event, widget):
        widget.configure(fg_color=("#89A6A6", "#2E4343"))
        widget.configure(cursor="hand2")

    def onLeave(event, widget):
        widget.configure(fg_color="transparent")
        widget.configure(cursor="arrow")

    # place the widgets
    if side == "left":
        developer_photo_label.grid(row=0, column=0, rowspan=4, sticky="nsw", padx=20, pady=20)
        developer_name_label.grid(row=0, column=2, columnspan=4, sticky="n", padx=(50, 50), pady=(20, 0))
        developer_contribution.grid(row=1, column=2, rowspan=1, columnspan=4, sticky="nswe", padx=(50, 50), pady=(0, 0))
        developer_email_label.grid(row=2, column=2, columnspan=1, sticky="s", padx=(20, 5), pady=(0, 30))
        developer_github_label.grid(row=2, column=3, columnspan=1, sticky="s", padx=(5, 5), pady=(0, 30))
        developer_linkedin_label.grid(row=2, column=4, columnspan=1, sticky="s", padx=(5, 5), pady=(0, 30))
        developer_phone_label.grid(row=2, column=5, columnspan=1, sticky="s", padx=(5, 20), pady=(0, 30))
        # developer_instagram_label.grid(row=3, column=6, columnspan=1, sticky="n", padx=(5, 20), pady=(0, 10))
    elif side == "right":
        developer_photo_label.grid(row=0, column=6, rowspan=4, sticky="nse", padx=(50, 20), pady=20)
        developer_name_label.grid(row=0, column=0, columnspan=4, sticky="n", padx=50, pady=(20, 0))
        developer_contribution.grid(row=1, column=0, rowspan=1, columnspan=4, sticky="nsew", padx=50, pady=(0, 0))
        developer_email_label.grid(row=2, column=0, columnspan=1, sticky="s", padx=(20, 5), pady=(0, 30))
        developer_github_label.grid(row=2, column=1, columnspan=1, sticky="s", padx=(5, 5), pady=(0, 30))
        developer_linkedin_label.grid(row=2, column=2, columnspan=1, sticky="s", padx=(5, 5), pady=(0, 30))
        developer_phone_label.grid(row=2, column=3, columnspan=1, sticky="s", padx=(5, 20), pady=(0, 30))
        # developer_instagram_label.grid(row=3, column=4, columnspan=1, sticky="n", padx=(5, 20), pady=(0, 10))

    return developer_frame


global running
running = False


def stop_button_click():
    global running
    running = False
    # sys.exit()
    # p.kill()
    global p
    if p:
        p.terminate()
        p.wait()
        # print("process ended")
    else:
        return


def launch_button_click():
    global p
    global running
    if running:
        return
    running = True
    control_latest = "../control_latest.py"
    p = subprocess.Popen(["python", control_latest])



def open_camera(camera_index: int = 0):
    cap = cv2.VideoCapture(camera_index)
    return cap


def close_camera(cap):
    cap.release()


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
            theme: str = "Dark",
            camera_index: int = 0,
            smoothness_factor_2: float = 10,
            smoothness_factor_1: float = 10,
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
        self.cap = None
        self.Show_camera = False

        self._create_base_frame()

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
        return configure_widget

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
        return help_widget

    def create_About_us_widget(self):
        About_us_widget = ctk.CTkFrame(
            self,
            bg_color="transparent",
            fg_color="transparent",
            corner_radius=20,
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
            "Launch here to get in\nthe world of adventure"
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
        """
            Layout: <button> <tips_content> <button>
            the left button is for previous tip and the right button is for next tip
        """
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
        left_button.place(relx=0, rely=0.0, relwidth=0.1, relheight=1, anchor="nw")
        right_button.place(relx=0.9, rely=0.0, relwidth=0.1, relheight=1, anchor="nw")

        # create a frame for tips content
        tips_content = ctk.CTkFrame(
            Tips_widget,
            bg_color="transparent",
            fg_color=("#89A6A6", "#2E4343"),
            corner_radius=10,
        )
        tips_content.place(
            relx=0.12, rely=0.01, relwidth=0.76, relheight=0.99, anchor="nw"
        )
        tips_content.bind("<Configure>", lambda event: reset_image_size(event))

        # get the tips images
        dark_tip_img_path = os.path.join(self.assets_path, "Tips", "Dark")
        light_tip_img_path = os.path.join(self.assets_path, "Tips", "Light")

        tip_img_1 = ctk.CTkImage(
            dark_image=Image.open(os.path.join(dark_tip_img_path, "change_tab_dark.png")),
            light_image=Image.open(os.path.join(light_tip_img_path, "change_tab_light.png")),
            size=(600, 400)
        )
        tip_img_2 = ctk.CTkImage(
            dark_image=Image.open(os.path.join(dark_tip_img_path, "drag_drop_dark.png")),
            light_image=Image.open(os.path.join(light_tip_img_path, "drag_drop_light.png")),
            # size=(width, height)
            size=(600, 400)
        )
        tip_img_3 = ctk.CTkImage(
            dark_image=Image.open(os.path.join(dark_tip_img_path, "left_click_dark.png")),
            light_image=Image.open(os.path.join(light_tip_img_path, "left_click_light.png")),
            # size=(width, height)
            size=(600, 400)
        )
        tip_img_4 = ctk.CTkImage(
            dark_image=Image.open(os.path.join(dark_tip_img_path, "right_click_dark.png")),
            light_image=Image.open(os.path.join(light_tip_img_path, "right_click_light.png")),
            # size=(width, height)
            size=(600, 400)
        )
        tip_img_5 = ctk.CTkImage(
            dark_image=Image.open(os.path.join(dark_tip_img_path, "scroll_dark.png")),
            light_image=Image.open(os.path.join(light_tip_img_path, "scroll_light.png")),
            # size=(width, height)
            size=(600, 400)
        )
        tip_img_6 = ctk.CTkImage(
            dark_image=Image.open(os.path.join(dark_tip_img_path, "volume_dark.png")),
            light_image=Image.open(os.path.join(light_tip_img_path, "volume_light.png")),
            # size=(width, height)
            size=(600, 400)
        )
        tip_img_7 = ctk.CTkImage(
            dark_image=Image.open(os.path.join(dark_tip_img_path, "cursor_move_dark.png")),
            light_image=Image.open(os.path.join(light_tip_img_path, "cursor_move_light.png")),
            # size=(width, height)
            size=(600, 400)
        )

        def reset_image_size(event):
            width = event.width * 0.70
            # height = event.height * 0.50
            height = width * (1309 / 3464)
            tip_img_1.configure(size=(width, height))
            tip_img_2.configure(size=(width, height))
            tip_img_3.configure(size=(width, height))
            tip_img_4.configure(size=(width, height))
            tip_img_5.configure(size=(width, height))
            tip_img_6.configure(size=(width, height))
            tip_img_7.configure(size=(width, height))

        tips = [tip_img_1, tip_img_2, tip_img_3, tip_img_4, tip_img_5, tip_img_6, tip_img_7]
        tip_label = ctk.CTkLabel(
            tips_content,
            # text=tip,
            text="",
            image=tips[6],
            bg_color="transparent",
            fg_color="transparent",
            font=("Segoe UI", 30, "bold"),
            corner_radius=10,
            # text_color="gold",
        )
        tip_label.place(relx=0.5, rely=0.5, relwidth=0.99, relheight=0.99, anchor="center")

        def previous_tip():
            tip = tip_label.cget("image")
            i = tips.index(tip)
            if i == 0:
                i = len(tips) - 1
            else:
                i -= 1
            tip_label.configure(image=tips[i])

        def next_tip():
            tip = tip_label.cget("image")
            i = tips.index(tip)
            if i == len(tips) - 1:
                i = 0
            else:
                i += 1
            tip_label.configure(image=tips[i])

        def update_tip():
            next_tip()
            self.after(5000, update_tip)

        update_tip()

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
            text="Smoothness (cursor)   ",
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
        slider1.set(float(self.smoothness_factor_1))
        value_label1 = ctk.CTkLabel(
            frame1,
            text=f"{self.smoothness_factor_1}",
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
        )
        label1.grid(row=0, column=0, sticky="nsew")
        slider1.grid(row=0, column=1, columnspan=3, sticky="ew")
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
            text="Smoothness (scrolling)",
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
        slider2.set(float(self.smoothness_factor_2))
        value_label2 = ctk.CTkLabel(
            frame2,
            text=f"{self.smoothness_factor_2}",
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
        )
        label2.grid(row=0, column=0, sticky="nsew")
        slider2.grid(row=0, column=1, columnspan=3, sticky="ew")
        value_label2.grid(row=0, column=4, sticky="nsew")

        # note: For low end devices, the smoothness factor ( cursor ) should be below 5
        # configure both values as per your convenience
        # note_frame = ctk.CTkFrame(
        #     self.Configure_Frame,
        #     bg_color="transparent",
        #     fg_color="red",
        #     corner_radius=10,
        # )
        # note_frame.grid_rowconfigure(0, weight=1)
        note_text = "   Note: For low end devices, the smoothness factor ( cursor ) should be below 5. Configure both values as per your convenience   "
        note_textbox = ctk.CTkLabel(
            self.Configure_Frame,
            text=note_text,
            font=("Segoe UI", 15, "bold"),
            corner_radius=10,
            bg_color="transparent",
            fg_color="transparent",
        )
        # note_textbox.grid(row=0, sticky="nsew")

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
            text="Choose Theme ",
            font=("Segoe UI", 22, "bold"),
            corner_radius=10,
        )
        theme_list = ctk.CTkOptionMenu(
            frame3,
            hover=False,
            values=["Dark", "Light", "System"],
            font=("Segoe UI", 15, "bold"),
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
            font=("Segoe UI", 15, "bold"),
            corner_radius=10,
            bg_color="transparent",
            fg_color=("#89A6A6", "#2E4343"),
            dropdown_fg_color=("#89A6A6", "#2E4343"),
            dropdown_hover_color=("#89A6A6", "#2E4343"),
            command=lambda event: self.camera_list_selection(event, camera_list),
        )
        camera_list.set(f"Camera {self.camera_index + 1}")
        label4.grid(row=0, column=0, sticky="nsew")
        camera_list.grid(row=0, column=1, columnspan=3, sticky="nsew")

        # frame 5 (show the camera feed with a toogle button)
        frame5 = ctk.CTkFrame(
            self.Configure_Frame,
            bg_color="transparent",
            fg_color="transparent",
            corner_radius=10,
            width=20,
        )
        label5 = ctk.CTkLabel(
            frame5,
            text="Show the camera feed",
            font=("Segoe UI", 22, "bold"),
            corner_radius=10,
        )
        switch_var = ctk.StringVar(value="off")
        switch = ctk.CTkSwitch(
            frame5,
            text="",
            # width=300,
            # height=80,
            command=lambda: show_camera_feed(),
            variable=switch_var,
            onvalue="on",
            offvalue="off"
        )
        label5.pack(expand=True, fill="both", side="left")
        switch.pack(expand=True, fill="both", side="left")
        camera_feed_frame = ctk.CTkFrame(
            self.Configure_Frame,
            bg_color="transparent",
            fg_color="transparent",
            corner_radius=10,
            width=400,
            height=300,
        )
        img_label = ctk.CTkLabel(
            camera_feed_frame,
            text="",
            corner_radius=10,
            bg_color="transparent",
            fg_color="transparent",
            font=("Segoe UI", 30, "bold"),
            # text_color="gold",
        )

        def show_frames(cap, img_label):
            if self.Show_camera:
                _, frame = cap.read()
                frame = cv2.flip(frame, 1)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (400, 300))
                img = Image.fromarray(frame)
                img_obj = ctk.CTkImage(
                    dark_image=img,
                    light_image=img,
                    size=(400, 300),
                )
                img_label.configure(image=img_obj)
                img_label.after(1, show_frames, cap, img_label)

        def show_camera_feed():
            if switch_var.get() == "on":
                frame5.configure(width=400)
                self.Show_camera = True
                self.cap = open_camera(self.camera_index)
                img_label.pack(expand=True, fill="both", side="left")
                show_frames(self.cap, img_label)

            else:
                # turn the camera off, and remove the image label
                self.Show_camera = False
                img_label.pack_forget()
                close_camera(self.cap)

        # frame 6 (buttons): <Save> <Back Button>
        frame6 = ctk.CTkFrame(
            self,
            bg_color="transparent",
            fg_color="transparent",
            corner_radius=10,
            height=200,
        )
        frame6.grid_rowconfigure(0, weight=1)
        frame6.grid_columnconfigure((0, 1), weight=1)
        save_button = ctk.CTkButton(
            frame6,
            text="Save",
            font=("Segoe UI", 20, "bold"),
            text_color=("black", "white"),
            corner_radius=10,
            bg_color="transparent",
            fg_color=("#7DAEC2", "#4A6667"),
            hover_color=("#648FA1", "#6A9092"),
            command=lambda: self._save_configuration(
                smoothness_factor_1=self.smoothness_factor_1,
                smoothness_factor_2=self.smoothness_factor_2,
                camera_index=self.camera_index,
            ),
        )
        back_button = ctk.CTkButton(
            frame6,
            text="Back",
            font=("Segoe UI", 20, "bold"),
            text_color=("black", "white"),
            corner_radius=10,
            bg_color="transparent",
            fg_color="transparent",
            border_width=1,
            border_color=("black", "white"),
            hover_color=("#6A9092", "#6A9092"),
            command=lambda: self._back_from_configure_page(),
        )
        save_button.grid(row=0, column=1, sticky="nsew", padx=30, pady=0)
        back_button.grid(row=0, column=0, sticky="nsew", padx=30, pady=0)
        # remove all the widgets from the base frame
        for widget in self.winfo_children():
            widget.place_forget()

        self.Configure_Frame.place(
            relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center"
        )
        # place the frames
        frame1.pack(expand=True, fill="both", pady=(20, 10))
        frame2.pack(expand=True, fill="both", pady=(0, 20))
        note_textbox.pack(expand=True, fill="both", pady=(0, 20))
        frame3.pack(expand=True, fill="both", pady=(0, 20))
        frame4.pack(expand=True, fill="both", pady=(0, 20))
        frame5.pack(expand=True, fill="both", pady=(0, 20))
        camera_feed_frame.pack(expand=True, fill="both", pady=(0, 50))
        frame6.place(relx=0.5, rely=0.96, relwidth=0.9, anchor="s")
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
            self.theme = "Dark"
        elif theme_list.get() == "Light":
            self.theme = "Light"
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
        # create a scrollable frame
        self.About_us_Frame = ctk.CTkScrollableFrame(
            self, bg_color="transparent", fg_color="transparent", corner_radius=10
        )

        # frame 0 ( Description )
        frame0 = ctk.CTkFrame(
            self.About_us_Frame,
            bg_color="transparent",
            fg_color="transparent",
            corner_radius=10,
        )
        label0 = ctk.CTkLabel(
            frame0,
            text="Description",
            font=("Segoe UI", 30, "bold"),
            corner_radius=10,
        )
        label0.pack(side='left', padx=20, pady=(0, 0))
        description = ctk.CTkTextbox(
            self.About_us_Frame,
            bg_color="transparent",
            fg_color=("#89A6A6", "#2E4343"),
            corner_radius=10,
            font=("Segoe UI", 18),
            activate_scrollbars=False,
            height=250,
            wrap="word",
        )
        description.insert(
            "1.0",
            "The 'Air Cursor' desktop application redefines human-computer interaction, allowing users to navigate and control computer operations using intuitive hand gestures. With a user-friendly interface and easy and simple to use gestures, it enhances accessibility, particularly for individuals with physical limitations. Users can easily download the application to enjoy a more natural and intuitive approach to navigation. Join the future of effortless interaction with Air Cursor.\n\n"
            "This project has been completed under the guidance of Mr. Sandeep Kumar Garg, Professor, Department of Computer Science and Engineering, IIT Roorkee along with continuous reviewing by the teaching assistants. ",
        )
        description.configure(state="disabled")

        Developers_img_path = os.path.join(os.path.dirname(__file__), "Assets", "Developers")
        Panda_img_path = os.path.join(Developers_img_path, "Panda.jpg")
        Souvik_img_path = os.path.join(Developers_img_path, "Souvik.png")
        Sukhman_img_path = os.path.join(Developers_img_path, "Sukhman.png")
        Raman_img_path = os.path.join(Developers_img_path, "Raman.png")
        Yashwanth_img_path = os.path.join(Developers_img_path, "Yashwanth.png")
        Ayush_img_path = os.path.join(Developers_img_path, "Ayush.png")

        # label1 frame
        dev_label_frame = ctk.CTkFrame(
            self.About_us_Frame,
            bg_color="transparent",
            fg_color="transparent",
            corner_radius=10,
        )
        label1 = ctk.CTkLabel(
            dev_label_frame,
            text="Developers",
            font=("Segoe UI", 30, "bold"),
            corner_radius=10,
        )
        label1.pack(side='left', padx=20)

        # frame 1 -> developer 1 (Souvik)
        souvik_frame = create_developer_frame(
            self.About_us_Frame,
            img_path=Souvik_img_path,
            name="Souvik Karmakar",
            role="Contributed to the designing and development of the User interface and user experience. Involved in proper testing at all stages with debugging.",
            email="souvik_k@cs.iitr.ac.in",
            github="https://github.com/souvik-13",
            linkedin="https://www.linkedin.com/in/souvik-karmakar-888202257/",
            instagram="https://www.instagram.com/souv1k_13/",
            phone="+918642924659",
            side="right"
        )

        # frame 2 -> developer 2 (Raman)
        raman_frame = create_developer_frame(
            self.About_us_Frame,
            img_path=Raman_img_path,
            name="Raman Sharma",
            role="Served as Team leader. Designed the whole UI along with document formatting and writing. Also, contributed to the design of the algorithm and simple gesture technique for a seamless experience. Involved in proper testing at all stages with debugging. ",
            email="raman_s@cs.iitr.ac.in",
            github="https://github.com/ramansharma829455",
            linkedin="https://www.linkedin.com/in/raman-sharma-8294551b7/",
            instagram="https://www.instagram.com/ramansharma829455/",
            phone="+917521829455",
            side="left"
        )

        # frame 3 -> developer 3 (Yash)
        yashwanth_frame = create_developer_frame(
            self.About_us_Frame,
            img_path=Yashwanth_img_path,
            name="Boda Yashwanth",
            role="Contributed to designing and implementing the hand tracking, gesture detection and computer automation algorithms. Also, contributed majorly in writing the various paperwork related to the project.",
            email="boda_y@cs.iitr.ac.in",
            github="https://github.com/yashwanthboda",
            linkedin="https://www.linkedin.com/in/yashwanth-boda-555224299/",
            instagram="https://www.instagram.com/yashwanth_boda/",
            phone="+918977925111",
            side="left"
        )

        # frame 4 -> developer 4 (Sukhman)
        sukhman_frame = create_developer_frame(
            self.About_us_Frame,
            img_path=Sukhman_img_path,
            name="Sukhman Singh",
            role="Contributed to the analysis of the project feasibility and designed project pipeline. Integration of the front end with the back end.",
            email="sukhman_s@cs.iitr.ac.in",
            github="https://github.com/sukhman-sukh",
            linkedin="https://www.linkedin.com/in/sukhman-singh-291a8b252/",
            instagram="https://www.instagram.com/sukhman_sukh/",
            phone="+9119415860440",
            side="right"
        )
        # frame 5 -> developer 5 (Ayush)
        ayush_frame = create_developer_frame(
            self.About_us_Frame,
            img_path=Ayush_img_path,
            name="Ayush Ranjan",
            role="Contributed to the design and implementation of the algorithms and logic behind the various gesture-driven computer operations along with the speed, accuracy and reliability testing across various systems.",
            email="ayush_r@cs.iitr.ac.in",
            github="https://github.com/ayushr100",
            linkedin="https://www.linkedin.com/in/ayush-ranjan-b363a7250",
            instagram="https://www.instagram.com/ayush_ranjan_100/",
            phone="+917482958551",
            side="left"
        )

        self.back_button_image = ctk.CTkImage(
            dark_image=Image.open(os.path.join(os.path.dirname(__file__), "Assets", "Buttons", "arrow_white.png")),
            light_image=Image.open(os.path.join(os.path.dirname(__file__), "Assets", "Buttons", "arrow_black.png")),
            size=(30, 30),
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
            hover_color=("#89A6A6", "#2E4343"),
            # border_color="white",
            # border_width=1,
            command=lambda: self._back_from_about_us_page(),
            height=30,
            width=30,
        )

        # remove all the widgets from the base frame
        for widget in self.winfo_children():
            widget.place_forget()

        # place the about us frame
        back_button.place(relx=0.01, rely=0.02, anchor="nw")
        self.About_us_Frame.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.96, anchor="nw")

        # pack the frames
        frame0.pack(expand=True, fill="both", pady=0, padx=0)
        description.pack(expand=True, fill="both", padx=20, pady=20)
        dev_label_frame.pack(expand=True, fill="both", pady=20, padx=0)
        raman_frame.pack(expand=True, fill="both", pady=20, padx=20)
        souvik_frame.pack(expand=True, fill="both", pady=20, padx=20)
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
        # os.environ['SF1'] = str(smoothness_factor_1)
        # os.environ['SF2'] = str(smoothness_factor_2)
        # os.environ['CAMERA_INDEX'] = str(camera_index)
        with open(file_path, "w") as f:
            f.write(f"{smoothness_factor_1}\n")
            f.write(f"{smoothness_factor_2}\n")
            f.write(f"{camera_index}\n")
        self._back_from_configure_page()

    def _back_from_configure_page(self):
        # stop the camera feed
        self.Show_camera = False
        if self.cap:
            close_camera(self.cap)
        else:
            pass
        # remove all the widgets from the base frame
        for widget in self.winfo_children():
            widget.place_forget()
        self._create_base_frame()

    def help_button_click(self):
        # open this "https://github.com/RAYS-Group-of-Software-Developer/Air-Cursor/discussions" link in browser
        webbrowser.open_new_tab(
            "https://github.com/RAYS-Group-of-Software-Developer/Air-Cursor/discussions"
        )

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
        self.height = int(400)
        self.width = int(self.height * 1.6)
        self.x = int((self.winfo_screenwidth() * 1.5 - self.width * 1.5) // 2)
        self.x_1 = int((self.winfo_screenwidth() - self.width) // 2)
        self.y = int((self.winfo_screenheight() * 1.5 - self.height * 1.5) // 2)
        self.y_1 = int((self.winfo_screenheight() - self.height) // 2)

        with open(file_path, "r") as f:
            _smoothness_factor_1 = float(f.readline())
            _smoothness_factor_2 = float(f.readline())
            _camera_index = int(f.readline())
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
        self.Splash_Frame = SplashFrame(
            self,
            width=self.width,
            height=self.height,
            bg_color="black",
            border_width=2,
            border_color="black",
            fg_color="black",
            corner_radius=20,
        )

        # base frame
        self.Base_Frame = Base(
            self,
            bg_color=("#B8D8D8", "#152E2E"),
            fg_color=("#B8D8D8", "#152E2E"),
            # border_width=0,
            corner_radius=10,
            smoothness_factor_1=_smoothness_factor_1,
            smoothness_factor_2=_smoothness_factor_2,
            camera_index=_camera_index,
        )

        self.show_splash()
        self.update()
        self.after(7250, self.show_main)
        # self.show_main()

    def show_splash(self):
        # make the window appear on the top
        # self.attributes("-topmost", True)
        self.overrideredirect(True)
        self.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.Splash_Frame.pack(expand=True, fill="both")

    def show_main(self):
        self.Splash_Frame.pack_forget()
        self.attributes("-topmost", False)
        self.overrideredirect(False)
        self.width = 1000
        self.height = int(self.width * 9 / 16)
        self.geometry(f"{self.width}x{self.height}+{self.x_1}+{self.y_1}")
        self.minsize(self.width, self.height)
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
