import time
import threading
import pynput.mouse as m
import pynput.keyboard as k

from customtkinter import *
import webbrowser

st_key = "8"
exit_key = "9"
button = m.Button.left


class Autoclick(threading.Thread):
    def __init__(self, delay, button):
        super(Autoclick, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)

def on_press(key):
    try:
        if key.char == st_key:
            if click1.running:
                click1.stop_clicking()
            else:
                click1.start_clicking()
        elif key.char == exit_key:
            click1.exit()
            listen_thread.stop()
    except AttributeError:
        pass

mouse = m.Controller()
click1 = Autoclick(1, button)
click1.start()

#CTk STUFF BELOW


app = CTk(fg_color="#1e293b")
app.geometry("350x450")
app.title("Autoclicker")

def save():
    global st_key
    if keyEntry.get().isspace() or keyEntry.get() == "":
        st_key = st_key
    elif keyEntry.get() == exit_key:
        st_key = st_key
    else:
        st_key = keyEntry.get()
    keyEntry.delete(0,END)
    keyLabel.configure(text=f"Key Label: {st_key}")

    if dEntry.get().replace(".", "").isnumeric():
        click1.delay = float(dEntry.get())
    dLabel.configure(text=f"Delay: {click1.delay}")


saveButton = CTkButton(
    app, text="Save Changes", command=save, fg_color="#64748b", text_color="black",
    border_color="#475569", border_width=5, hover=True, hover_color="#374151",
    font=("Helvetica", 14), state="normal", width=150, height=50, anchor="center"
)


title = CTkLabel(app, text="Autoclicker", text_color="black",font=((""),50))
keyLabel = CTkLabel(app, text=f"Key Label: {st_key}")
keyEntry = CTkEntry(app, placeholder_text="Keybinds...")

dLabel = CTkLabel(app, text=f"Delay: {click1.delay}")
dEntry = CTkEntry(app, placeholder_text="Delay")

gLabel = CTkLabel(app, text= "github.com/alm0st01",font=("Arial", 16,'underline'))

statusLabel = CTkLabel(app, text="Status: OFF", text_color="red", font=((""),20))

title.place(x=175,y=50, anchor=CENTER)
saveButton.place(x=175,y=350,anchor=CENTER)

keyLabel.place(x=80, y=140,anchor=CENTER)
keyEntry.place(x=80, y=180,anchor=CENTER)

dLabel.place(x=270,y=140,anchor=CENTER)
dEntry.place(x=270,y=180,anchor=CENTER)

gLabel.place(x=25,y=400)
gLabel.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/alm0st01"))

statusLabel.place(x=175, y=90, anchor=CENTER)


def listen():
    while click1.program_running:
        with k.Listener(on_press=on_press) as listener:
            listener.join()

def checks():
    while click1.program_running:
        if len(keyEntry.get()) >1:
            keyEntry.delete(1,END)

        if click1.running:
            statusLabel.configure(text_color="green",text="Status: ON")
        else:
            statusLabel.configure(text_color="red",text="Status: OFF")
        if click1.program_running is False:
            statusLabel.configure(text_color="red",text="Status: FULLY STOPPED")

listen_thread = threading.Thread(target=listen)
listen_thread.start()
entry_thread = threading.Thread(target=checks)
entry_thread.start()

app.mainloop()