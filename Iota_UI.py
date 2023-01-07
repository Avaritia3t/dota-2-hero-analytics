import tkinter as tk

# Create a new Tk window
root = tk.Tk()

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the window size and position
window_width = screen_width // 5
window_height = screen_height // 6
window_x = (screen_width - window_width) // 2
window_y = (screen_height - window_height) // 2

# Remove the window decorations
root.overrideredirect(True)

# Set the window background color
root.config(bg='black')

# Set the window size and position
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Create a Label widget to display the main text
iotalabel = tk.Label(root, text="Iota", font=("Arial", 36), bg='black', fg='white')
iotalabel.pack(side="top", fill="both", expand=True)

# Get the width and height of the iotalabel widget
label_width = iotalabel.winfo_width()
label_height = iotalabel.winfo_height()

# Calculate the x and y coordinates of the center point
label_center_x = label_width / 2
label_center_y = label_height / 2

# Print the x and y coordinates of the center point
print(f'Center point: ({label_center_x}, {label_center_y})')

# Create a second Label widget to display the loading text
loadingLabel = tk.Label(root, text="Loading...", font=("Arial", 18), bg='black', fg='white')
loadingLabel.place(x=0, y=15, anchor=tk.NW, relx=iotalabel.winfo_x(), rely=iotalabel.winfo_y())

# Get the width and height of the iotalabel widget
label_width = loadingLabel.winfo_width()
label_height = loadingLabel.winfo_height()

# Calculate the x and y coordinates of the center point
label_center_x = label_width / 2
label_center_y = label_height / 2

# Print the x and y coordinates of the center point
print(f'Center point: ({label_center_x}, {label_center_y})')


# Force the window to redraw itself
root.update_idletasks()
root.update()

# Sleep for 5 seconds
root.after(5000, root.destroy)

# Run the main loop
root.mainloop()
