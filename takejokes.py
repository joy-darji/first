import tkinter as tk
import requests

root = tk.Tk()
root.geometry("600x700")


label1 = tk.Label(text = "click button for joke")
label1.pack()
def jokes():


    data = requests.get(f"https://v2.jokeapi.dev/joke/Any").json()

    if data["type"] == "single":
        joke_s = data["joke"]

    else:
        joke_s = (f"{data["setup"]}  \n\n   {data["delivery"]}")

    label1.config(text = joke_s)



button = tk.Button(text = "click here for get jokes0", command = jokes)
button.pack()

root.mainloop()