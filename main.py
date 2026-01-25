import tkinter as tk
from tkinter import ttk
import interface

def main():
    root = tk.Tk()
    app = interface.Interface(root)
    root.mainloop()

if __name__ == "__main__":
    main()