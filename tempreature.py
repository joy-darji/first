import tkinter as tk
import requests

root = tk.Tk()
root.geometry("600x700")


label1 = tk.Label(text = "click button for tempreature and wind speed")
label1.pack()

def tempreature():
    data = requests.get("https://api.open-meteo.com/v1/forecast?latitude=23.0225&longitude=72.5714&current_weather=true").json()


    temp = str(data["current_weather"]["temperature"]) + data["current_weather_units"]["temperature"]

    label1.config(text = temp)

button = tk.Button(text = "press here for tempreature", command = tempreature)
button.pack()

def wind_speed():
    data = requests.get("https://api.open-meteo.com/v1/forecast?latitude=23.0225&longitude=72.5714&current_weather=true").json()

    wind = str(data["current_weather"]["windspeed"]) + data["current_weather_units"]["windspeed"]

    label1.config(text = wind)


button = tk.Button(text = "press here for windspeed", command = wind_speed)
button.pack()


root.mainloop()