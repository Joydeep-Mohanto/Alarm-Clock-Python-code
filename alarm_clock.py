import tkinter as tk
from PIL import ImageTk, Image
import datetime
import winsound

def check_alarm():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    alarm_time = text_time.get()
    global freq, dur
    freq = 500
    dur = 1000
    if now == alarm_time and alarm_on:
        label_alarm.config(text="Alarm Ringing!", fg="red")
        for i in range(0,5):
            winsound.Beep(freq, dur)  # Beep for 7 seconds (500 Hz)
            freq+=100
    else:
        label_alarm.config(text="", fg="black")
    root.after(1000, check_alarm)  # Recheck every second if alarm is on

def set_alarm():
    global alarm_on
    alarm_on = True
    alarm_time = text_time.get()
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
        label_alarm.config(text=f"Alarm set for {alarm_time}", fg="black")
    except ValueError:
        label_alarm.config(text="Invalid time format! Use HH:MM", fg="red")
'''
def stop_alarm():
    global alarm_on
    alarm_on = False
    label_alarm.config(text="", fg="black")
'''
def update_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    time_display.config(text=current_time)
    root.after(1000, update_time)  # Update time every second

root = tk.Tk()
root.title('Alarm Clock')
root.geometry("600x450")

alarm_on = False
text_time = tk.StringVar()

img = Image.open("alarm_clock.jpg")
img = img.resize((220, 250))
test = ImageTk.PhotoImage(img)
label1 = tk.Label(image=test)
label1.image = test
label1.place(x=204, y=25)

time_display = tk.Label(root, text="", bd=8, font='Arial')
time_display.place(x=1, y=50)

alarm_input = tk.Label(root, text='Input', bd=7, font='Arial')
alarm_input.place(x=274, y=280)

inputbox = tk.Entry(root, width=25, borderwidth=1, textvariable=text_time)
inputbox.place(x=230, y=320)

btn_set_alarm = tk.Button(root, text='Set Alarm', bd=9, font='Arial', activebackground='red', command=set_alarm)
btn_set_alarm.place(x=250, y=350)

#btn_stop_alarm = tk.Button(root, text='Stop Alarm', bd=9, font='Arial', activebackground='red', command=stop_alarm)
#btn_stop_alarm.place(x=350, y=350)

label_alarm = tk.Label(root, text="", width=20, foreground='black', font='bold')
label_alarm.place(x=200, y=415)

update_time()  # Start updating time
check_alarm()  # Start checking alarm condition

root.mainloop()
