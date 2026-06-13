import tkinter as tk

root = tk.Tk()
root.geometry("600x700")

label1 = tk.Label()
label1.pack()

textbox1 = tk.Entry()
textbox1.pack()

def palindrome():

    palindrome_name = (textbox1.get())

    if palindrome_name == palindrome_name[::-1]:
        label1.config(text = f"name is palindrome {palindrome_name}")

    else:
        label1.config(text = f"name is not palindrome {palindrome_name}")

        
button = tk.Button(text = "press here ",command = palindrome)
button.pack()





root.mainloop()