# pip install qrcode pillow

# Importing the modules
import qrcode
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

# Define Functions
def createQR(*args):
    data = text_entry.get()

    if data:
        img = qrcode.make(data)
        resized_img = img.resize((280, 250))
        tkimage = ImageTk.PhotoImage(resized_img)
        qr_canvas.delete("all")
        qr_canvas.create_image(0, 0, anchor=tk.NW, image=tkimage)
        qr_canvas.image = tkimage  # Keep reference
    else:
        messagebox.showwarning("Error", "Enter Some Data First")

def saveQR(*args):
    data = text_entry.get()

    if data:
        img = qrcode.make(data)
        resized_img = img.resize((280, 250))

        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            resized_img.save(path)
            messagebox.showinfo("Success", "QR Code is Saved")
    else:
        messagebox.showwarning("Error", "Enter Some Data First")

# GUI Code
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("300x380")
root.config(bg="White")
root.resizable(0, 0)

frame1 = tk.Frame(root, bd=2, relief=tk.RAISED)
frame1.place(x=10, y=0, width=280, height=250)

frame2 = tk.Frame(root, bd=2, relief=tk.SUNKEN)
frame2.place(x=10, y=260, width=280, height=100)

# Load a cover image safely
if os.path.exists("qrCodeCover.png"):
    cover_img = tk.PhotoImage(file="qrCodeCover.png")
else:
    cover_img = None
    print("Warning: 'qrCodeCover.png' not found. Using blank canvas.")

qr_canvas = tk.Canvas(frame1)
if cover_img:
    qr_canvas.create_image(0, 0, anchor=tk.NW, image=cover_img)
    qr_canvas.image = cover_img
qr_canvas.bind("<Double-1>", saveQR)
qr_canvas.pack(fill=tk.BOTH)

text_entry = ttk.Entry(frame2, width=26, font=("Sitka Small", 11), justify=tk.CENTER)
text_entry.bind("<Return>", createQR)
text_entry.place(x=5, y=5)

btn_1 = ttk.Button(frame2, text="Create", width=10, command=createQR)
btn_1.place(x=25, y=50)

btn_2 = ttk.Button(frame2, text="Save", width=10, command=saveQR)
btn_2.place(x=100, y=50)

btn_3 = ttk.Button(frame2, text="Exit", width=10, command=root.quit)
btn_3.place(x=175, y=50)

root.mainloop()
