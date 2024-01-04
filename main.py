import tkinter as tk
from tkinter import ttk

def open_camera():
    # Function to handle opening the camera
    print("Opening Camera")

def close_window():
    # Function to handle closing the window
    root.destroy()

# Create the main window
root = tk.Tk()

# Calculate the width and height as 50% of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = int(screen_width * 0.5)
height = int(screen_height * 0.5)

# Set the window title
root.title("Object Detection")

# Set the window size and position it at the center of the screen
root.geometry(f"{width}x{height}+{int((screen_width - width) / 2)}+{int((screen_height - height) / 2)}")

# Create the title label
title_label = ttk.Label(root, text="Object Detection")
title_label.pack(pady=10)

# Create the "Open Camera" button
open_camera_button = ttk.Button(root, text="Open Cam", command=open_camera)
open_camera_button.pack(pady=10)

# Create the "Close Window" button
close_window_button = ttk.Button(root, text="Close Window", command=close_window)
close_window_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
