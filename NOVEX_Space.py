import tkinter as tk
import datetime

window = tk.Tk()
window.title("NOVEX Space")
window.geometry("600x450")
window.configure(bg="#383636")

title = tk.Label(window, text = "NOVEX Space", font = ("Arial", 30), bg="#383636", fg="white")
title.pack(pady=20)

clock = tk.Label(window, font=("Arial", 20), bg="#383636", fg="white")
def update_clock():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(1000, update_clock)


clock.pack(pady=20)
update_clock()

memo = tk.Text(window, height=5, width=50, font=("Arial", 12), bg="#383636", fg="white", insertbackground="white")

memo.pack(pady=20)

save_and_load = tk.Button(window, text = "")


def save_memo():
    with open("memo.txt", "w") as f:
        f.write(memo.get("1.0", "end-1c"))
        save_and_load.config(text="Memo saved!", font=("Arial", 12), bg="#383636", fg="white")
        

save_button = tk.Button(window, text="Save Memo", command=save_memo, font=("Arial", 12), bg="#383636", fg="#383636")
save_button.pack(pady=10)




def load_memo():
    try:
        with open("memo.txt", "r") as f:
            memo.delete("1.0", "end")
            memo.insert("1.0", f.read())
            save_and_load.config(text="Memo loaded!", font=("Arial", 12), bg="#383636", fg="white") 

    except FileNotFoundError:
        save_and_load.config(text="No memo.txt found.", font=("Arial", 12), bg="#383636", fg="white")

load_button = tk.Button(window, text="Load Memo", command=load_memo, font=("Arial", 12), bg="#383636", fg="#383636")
load_button.pack(pady=10)
        



window.mainloop()