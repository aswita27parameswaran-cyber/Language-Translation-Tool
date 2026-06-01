from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

def translate_text():
    try:
        text = input_text.get("1.0", END).strip()

        if not text:
            messagebox.showwarning("Warning", "Please enter text")
            return

        source = source_lang.get()
        target = target_lang.get()

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_text():
    input_text.delete("1.0", END)
    output_text.delete("1.0", END)

root = Tk()
root.title("Language Translation Tool")
root.geometry("700x500")

Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 16, "bold")
).pack(pady=10)

Label(root, text="Enter Text").pack()

input_text = Text(root, height=8, width=70)
input_text.pack(pady=5)

frame = Frame(root)
frame.pack(pady=10)

Label(frame, text="Source").grid(row=0, column=0)

source_lang = ttk.Combobox(frame, width=10)
source_lang["values"] = (
    "en",
    "ta",
    "hi",
    "fr",
    "de",
    "es"
)
source_lang.set("en")
source_lang.grid(row=0, column=1)

Label(frame, text="Target").grid(row=0, column=2)

target_lang = ttk.Combobox(frame, width=10)
target_lang["values"] = (
    "ta",
    "en",
    "hi",
    "fr",
    "de",
    "es"
)
target_lang.set("ta")
target_lang.grid(row=0, column=3)

Button(
    frame,
    text="Translate",
    command=translate_text
).grid(row=0, column=4, padx=10)

Button(
    frame,
    text="Clear",
    command=clear_text
).grid(row=0, column=5)

Label(root, text="Translated Text").pack()

output_text = Text(root, height=8, width=70)
output_text.pack(pady=5)

root.mainloop()
