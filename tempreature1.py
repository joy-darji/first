import tkinter as tk
import requests

root = tk.Tk()
root.geometry("700x700")

label1 = tk.Label(text = "click button for getting tempreature , wind speed , interval , wind direction")
label1.pack()

def tempreture():
    data = requests.get("https://api.open-meteo.com/v1/forecast?latitude=23.0225&longitude=72.5714&current_weather=true").json()


    temp = str(data["current_weather"]["temperature"]) + data["current_weather_units"]["temperature"]

    wind = str(data["current_weather"]["windspeed"]) + data["current_weather_units"]["windspeed"]

    interval = str(data["current_weather"]["interval"]) + data["current_weather_units"]["interval"]

    winddirection = str(data["current_weather"]["winddirection"]) + data["current_weather_units"]["winddirection"]


    label1.config(text = (f" {temp} \n {wind} \n{interval} \n{winddirection}"))

button = tk.Button(text = "press here", command = tempreture)
button.pack(side = "bottom"-)


root.mainloop()