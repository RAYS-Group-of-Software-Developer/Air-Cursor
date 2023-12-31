import customtkinter as ctk
from PIL import Image
import cv2
import os

window = ctk.CTk()
window.title('Image Viewer')
window.geometry('800x600')

brand_icons = os.path.join(os.path.dirname(__file__), "Assets", "Brand_icons")
github_img = ctk.CTkImage(
    dark_image=Image.open(os.path.join(brand_icons, "github_dark.png")),
    light_image=Image.open(os.path.join(brand_icons, "github_light.png")),
    size=(100, 100),
)

label = ctk.CTkLabel(
    window,
    text="",
    image=github_img
)
label.pack()

canvas = ctk.CTkCanvas(
    window,
    background="red",
    width=800,
    height=600,
)
canvas.pack()

# cap = cv2.VideoCapture(0)


# Define function to show frame
def show_frames():
    # Get the latest frame and convert into Image
    cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    # Show image in label
    ctk_img = ctk.CTkImage(
        dark_image=img,
        light_image=img,
        size=(800, 600),
    )
    label.configure(image=ctk_img)
    # Repeat after 1ms
    label.after(20, show_frames)


# show_frames()
window.mainloop()
