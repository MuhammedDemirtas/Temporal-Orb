from tkinter import Tk, Canvas, Label, Entry, Button
import time
import math
import threading
import requests
from tkinter import messagebox
import winsound

"""
Analog Clock with Weather, Timer, and Digital Time
Author: M. Demirtas
GitHub: https://github.com/MuhammedDemirtas/Temporal-Orb-Python
"""

def update_clock():
    canvas.delete("all")

    # Draw the circular frame of the clock
    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, fill="black", outline="white", width=5)

    # Place hour numbers on the clock face
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        x = center_x + radius * 0.85 * math.cos(angle)
        y = center_y + radius * 0.85 * math.sin(angle)
        canvas.create_text(x, y, text=str(i), fill="white", font=("Arial", 14, "bold"))

    # Get current time
    current_time = time.localtime()
    hour = current_time.tm_hour % 12
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Calculate and draw the hour hand
    hour_angle = math.radians((hour * 30) + (minute / 2) - 90)
    hour_x = center_x + radius * 0.5 * math.cos(hour_angle)
    hour_y = center_y + radius * 0.5 * math.sin(hour_angle)
    canvas.create_line(center_x, center_y, hour_x, hour_y, fill="white", width=6)

    # Calculate and draw the minute hand
    minute_angle = math.radians((minute * 6) - 90)
    minute_x = center_x + radius * 0.7 * math.cos(minute_angle)
    minute_y = center_y + radius * 0.7 * math.sin(minute_angle)
    canvas.create_line(center_x, center_y, minute_x, minute_y, fill="white", width=4)

    # Calculate and draw the second hand
    second_angle = math.radians((second * 6) - 90)
    second_x = center_x + radius * 0.9 * math.cos(second_angle)
    second_y = center_y + radius * 0.9 * math.sin(second_angle)
    canvas.create_line(center_x, center_y, second_x, second_y, fill="red", width=2)

    # Draw the center point of the clock
    canvas.create_oval(center_x - 5, center_y - 5, center_x + 5, center_y + 5, fill="white")

    # Update the clock every 100 milliseconds
    canvas.after(100, update_clock)

def update_date_time_info():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%d %B %Y")
    date_time_label.config(text=f"{current_date}\{current_time}")
    date_time_label.after(1000, update_date_time_info)

def fetch_weather():
    try:
        response = requests.get("http://wttr.in/?format=%l:+%c+%t")
        if response.status_code == 200:
            weather_label.config(text=response.text)
        else:
            weather_label.pack_forget()
    except Exception as e:
        weather_label.pack_forget()

def start_timer():
    try:
        seconds = int(timer_input.get())
        threading.Thread(target=run_timer, args=(seconds,), daemon=True).start()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

def run_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_label.config(text=f"{mins:02}:{secs:02}")

        # Draw and keep showing the yellow line
        angle = math.radians((60 - seconds % 60) * 6 - 90)
        end_x = center_x + radius * 0.9 * math.cos(angle)
        end_y = center_y + radius * 0.9 * math.sin(angle)

        line_id = canvas.create_line(center_x, center_y, end_x, end_y, fill="yellow", width=2)

        time.sleep(1)

        seconds -= 1

    # Play the beep sound and show notification when the timer ends
    for _ in range(4):  # 4 beep sounds
        winsound.Beep(1000, 200)  # Beep sound: 1000 Hz frequency, 200 ms duration
        time.sleep(0.2)
    messagebox.showinfo("Notification", "Timer has ended!")
    timer_label.config(text="Timer: 00:00")

# Create the main window
app_window = Tk()
app_window.title("Analog Clock and Info")
app_window.geometry("500x600")
app_window.resizable(0, 0)
app_window.configure(bg="black")

# Create and place the canvas
canvas = Canvas(app_window, width=400, height=400, bg="black", highlightthickness=0)
canvas.pack()

# Center coordinates and radius of the clock
center_x = 200
center_y = 200
radius = 180

# Date and time label
date_time_label = Label(app_window, font=("Arial", 12), bg="black", fg="white")
date_time_label.pack(pady=10)

# Weather label
weather_label = Label(app_window, font=("Arial", 12), bg="black", fg="white")
weather_label.pack(pady=5)
fetch_weather()

# Timer input and buttons
timer_input = Entry(app_window, font=("Arial", 14), width=10, justify="center")
timer_input.pack(pady=10)
timer_input.insert(0, "")

start_button = Button(app_window, text="Start Timer", font=("Arial", 12), command=start_timer)
start_button.pack(pady=5)

# Timer label
timer_label = Label(app_window, text="Timer: 00:00", font=("Arial", 14), bg="black", fg="white")
timer_label.pack(pady=10)

# Start the clock
update_clock()

# Update date and time info
update_date_time_info()

# Run the main loop
app_window.mainloop()
