import tkinter as tk
from tkinter import ttk, messagebox
from sj_rates_sj import convert_to_huf_sj


class CurrencyAppSJ:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Valutaváltó SJ")
        self.amount_var = tk.StringVar()
        self.currency_var = tk.StringVar(value="EUR")
        self.result_var = tk.StringVar()
        self._build_ui_sj()

    def _build_ui_sj(self) -> None:
        for i in range(3):
            self.root.rowconfigure(i, weight=1)
            self.root.columnconfigure(i, weight=1)
            main_frame = ttk.Frame(self.root, padding=10)
            main_frame.grid(row=1, column=1)
            main_frame.columnconfigure(0, weight=0)
            main_frame.columnconfigure(1, weight=1)

        ttk.Label(main_frame, text="Összeg:").grid(
            row=0, column=0, sticky="e", pady=5
        )
        ttk.Entry(main_frame, textvariable=self.amount_var, width=25).grid(
            row=0, column=1, sticky="w", pady=5
        )

        ttk.Label(main_frame, text="Deviza:").grid(
            row=1, column=0, sticky="e", pady=5
        )
        currency_combo = ttk.Combobox(
            main_frame,
            textvariable=self.currency_var,
            values=["EUR", "USD", "GBP"],
            state="readonly",
            width=22,
        )
        currency_combo.grid(row=1, column=1, sticky="w", pady=5)
        calc_button = ttk.Button(
            main_frame,
            text="Átváltás HUF-ra",
            command=self._on_calculate_click_sj, 
        )
        calc_button.grid(row=2, column=0, columnspan=2, pady=10)

        ttk.Label(main_frame, text="Eredmény:").grid(
            row=3, column=0, sticky="e", pady=5
        )
        ttk.Label(main_frame, textvariable=self.result_var).grid(
            row=3, column=1, sticky="w", pady=5
        )
        exit_button = ttk.Button(
            main_frame,
            text="Kilépés",
            command=self.root.destroy,
        )
        exit_button.grid(row=4, column=0, columnspan=2, pady=10)

    def _on_calculate_click_sj(self) -> None:
        amount_str = self.amount_var.get().strip()
        base = self.currency_var.get().strip().upper()

        if not amount_str:
            messagebox.showwarning("Hiba", "Kérlek, add meg az összeget!")
            return

        try:
            amount = float(amount_str.replace(",", "."))
        except ValueError:
            messagebox.showerror("Hiba", "Az összeg nem megfelelő számformátum.")
            return
        huf_value = convert_to_huf_sj(amount, base)

        self.result_var.set(f"{amount:.2f} {base} = {huf_value:.2f} HUF")
