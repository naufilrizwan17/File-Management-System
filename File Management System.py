# Import necessary modules
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import re

# Function to browse files
def browse_files():
   # Use global variable source_link
   global source_link
   # Open file dialog and set the selected file path to source_link
   source_link.set(filedialog.askopenfilename())
   # If a file is selected
   if source_link.get():
      # Open the file and read its content
      with open(source_link.get(), 'r') as file:
         content = file.read()
         # Print the number of characters in the file
         print("%d characters in this file" % len(content))

# Function to get the name and extension of the selected file
def name_file():
   # Use global variable source_link
   global source_link
   # If no file is selected
   if not source_link.get():
      error_msg = "The file is not accessible!"
      # Show an error message
      messagebox.showerror("Error", error_msg)
   else:
      # Extract filename from the file path
      filename = re.search(r'[^\\/:*?"<>|\r\n]+$', source_link.get())
      # Split the filename into name and extension
      name, ext = os.path.splitext(filename)
      # Show the name and extension in a message box
      messagebox.showinfo("Information", "The name of the file is {} and its extension is {}".format(name, ext))

# Function to copy the selected file to a selected directory
def copy_file():
   # Use global variables source_link and destination_link
   global source_link, destination_link
   # If no file is selected
   if not source_link.get():
      error_msg = "The file is not accessible!"
      # Show an error message
      messagebox.showerror("Error", error_msg)
   else:
      # Open directory dialog and set the selected directory path to destination_link
      destination_link.set(filedialog.askdirectory())
      # If a directory is selected
      if destination_link.get():
         # Copy the file to the directory
         shutil.copy(source_link.get(), destination_link.get())
         msg = "The file is successfully copied!"
         # Show a success message
         messagebox.showinfo("Copying File...", msg)
      else:
         warn_msg = "Please try again!"
         # Show a warning message
         messagebox.showwarning("Warning", warn_msg)

# Function to delete the selected file
def delete_file():
   # Use global variable source_link
   global source_link
   # If no file is selected
   if not source_link.get():
      error_msg = "The file is not accessible!"
      # Show an error message
      messagebox.showerror("Error", error_msg)
   else:
      # Delete the file
      os.remove(source_link.get())
      msg = "The file is successfully deleted!"
      # Show a success message
      messagebox.showinfo("Deleting File...", msg)

# Function to initialize source_link and destination_link
def Initialize_Links():
   global source_link, destination_link
   # Initialize source_link and destination_link as StringVar
   source_link = tk.StringVar()
   destination_link = tk.StringVar()

# Function to create and place the widgets on the GUI
def Create_Widgets():
   # Create a label and place it on the GUI
   label_1 = tk.Label(manage, text="File Manager")
   label_1.configure(fg="black", font= ("arial", 30))
   label_1.place(x=100, y=5)
   
   # Create an entry and place it on the GUI
   entry_1 = tk.Entry(manage)
   entry_1.configure(fg="black", width=30)
   entry_1.place(x=50, y=100)
   
   # Create buttons and place them on the GUI
   browse_button = tk.Button(manage, text="Browse", bg="blue", fg="white", width=10,font= ("calibri", 15), command=browse_files)
   browse_button.place(x=150, y=150)
   name_button = tk.Button(manage, text="Name", bg= "grey", fg= "white", command=name_file)
   name_button.place(x=100, y=200)
   copy_button = tk.Button(manage, text="Copy", bg= "brown", fg= "white", command=copy_file)
   copy_button.place(x=100, y=250)
   delete_button = tk.Button(manage, text="Delete", bg= "red", fg= "white", command=delete_file)
   delete_button.place(x=100, y=300)

# Create a Tk instance
manage = tk.Tk()
# Set the geometry, title, and background color of the GUI
manage.geometry("500x500")
manage.title("File Management System")
manage.config(background="black")

# Initialize the links and create the widgets
Initialize_Links()
Create_Widgets()

# Start the main event loop
manage.mainloop()