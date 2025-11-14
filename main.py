import tkinter as tk
from sj_gui_sj import CurrencyAppSJ

def main():
    root = tk.Tk()

    root.geometry("600x300")

    app = CurrencyAppSJ(root)

    root.mainloop()

if __name__ == "__main__":
    main()
