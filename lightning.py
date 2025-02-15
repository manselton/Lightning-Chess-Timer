import os
import sys
import tkinter as ttk
import pygame           

# Initialize pygame mixer
pygame.mixer.init()

def play():
    global user_input
    global timer_id
    user_input = int(spinbox.get()) * 1000

    # Determine the path where the executable or script is located
    if getattr(sys, 'frozen', False):  # If running as an executable
        app_path = sys._MEIPASS
    else:  # If running from the source code
        app_path = os.path.dirname(os.path.abspath(__file__))

    # Define the path to the MP3 file
    mp3_path = os.path.join(app_path, 'foghorn.mp3')

    # Check if the MP3 file exists
    if os.path.exists(mp3_path):
        pygame.mixer.music.load(mp3_path)
        pygame.mixer.music.play()
    else:
        print("MP3 file not found!")
        
	# Re-schedule this function to run after user_input seconds.
    timer_id = win.after(user_input, play)
    
def stop():
    global timer_id
    win.after_cancel(timer_id)
    
win = ttk.Tk()
win.title("Lightning Chess Timer")
win.geometry("300x180")

user_input = ttk.StringVar()
user_input.set("9")

spinbox_label = ttk.Label(win, text="5 to 30 second cycle.", font=("Helvetica", 8))
spinbox_label.grid(row=1, column=1, columnspan=2, sticky=ttk.S, padx=5, pady=3)
spinbox = ttk.Spinbox(win, from_=5, to=30, increment=1,  font=("Helvetica", 10), wrap=True, 
    state="readonly", width=5, textvariable=user_input, command=None, justify=ttk.RIGHT)
spinbox.grid(row=2, column=1, sticky=ttk.N, padx=5, pady=3)

play_button = ttk.Button(win, text="Play", font=("Helvetica", 8), bg="pale green", command=play)
play_button.grid(row=3, column=1, sticky=ttk.W, padx=5, pady=3) 

stop_button = ttk.Button(win, text="Stop", font=("Helvetica", 8), bg="pink", command=stop)
stop_button.grid(row=3, column=2, sticky=ttk.W, padx=5, pady=3)

quit_button = ttk.Button(win, text="Quit", font=("Helvetica", 8), command=win.destroy)
quit_button.grid(row=4, column=1, sticky=ttk.W, padx=5, pady=3) 

win.mainloop()
