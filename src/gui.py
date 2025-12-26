import customtkinter as ctk
from utils.file import load_config

CONFIG = load_config("src/config.json")
APP_NAME = CONFIG["info"]["name"]

class JudgeGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(APP_NAME)
        self.geometry("600x400")
        ctk.set_appearance_mode(CONFIG["gui"]["mode"])
        ctk.set_default_color_theme(CONFIG["gui"]["theme"])

        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(self, text="Welcome to CP Judge!", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.pack(pady=20)

        self.entry = ctk.CTkEntry(self, placeholder_text="Enter test case ID")
        self.entry.pack(pady=10)

        self.run_button = ctk.CTkButton(self, text="Run Test", command=None)
        self.run_button.pack(pady=10)

        self.output_box = ctk.CTkTextbox(self, width=500, height=200)
        self.output_box.pack(pady=10)


if __name__ == "__main__":
    app = JudgeGUI()
    app.mainloop()
