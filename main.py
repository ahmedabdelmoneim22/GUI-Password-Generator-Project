import random # Random Library.
###########################################
def Generate_The_Password():
    #print("Welcome to the PyPassword Generator!")
    # Enter the Number of Letters;
    #letters_num = int(input("How many letters would you like in your password?\n"))
    letters_num= int(letterE.get())
    # Enter the Number of Symbols;
    #symbols_num = int(input("How many symbols would you like?\n"))
    symbols_num = int(symbolE.get())
    # Enter the Number of Numbers;
    #numbers_num = int(input("How many numbers would you like?\n"))
    numbers_num = int(numberE.get())
    if letters_num >=0 and letters_num <=26 and symbols_num>=0 and symbols_num<=12 and numbers_num>=0 and numbers_num<10:
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                   "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        new_letters = []
        new_symbols = []
        new_numbers = []
        # Generate the Letters;
        for letter in range(0, letters_num):
            new_letters.append(random.choice(letters))
        # Generate the Symbols;
        for symbol in range(0, symbols_num):
            new_symbols.append(random.choice(symbols))
        # Generate the Numbers;
        for num in range(0, numbers_num):
            new_numbers.append(random.choice(numbers))
        new_pass = ""  # The Password Fild;
        for num in range(0, len(new_letters + new_symbols + new_numbers)):
            new_pass += random.choice(new_letters + new_symbols + new_numbers)
        # The final Result;
        #print(f"Here is your Password: {new_pass}")
        result.configure(text=f"{new_pass}")
    else:
        result.configure(text="InCorrect Input")

import tkinter as tk
mainWindow = tk.Tk()
mainWindow.config(background="green")
mainWindow.title("Random Password Generator")
mainWindow.geometry("420x200")
welcomeLabel = tk.Label(mainWindow,text="Random Password Generator",fg="RED",
                        font=("Helvetica", 20, "bold"),background="green")
welcomeLabel.grid(row=0,column=0,columnspan=2)
letterLabel = tk.Label(mainWindow,text="Number of Letters    ",
                       font=("Helvetica",12,"bold"),background="green")
letterLabel.grid(row=1,column=0)
symbolLabel = tk.Label(mainWindow,text="Number of Symbols ",
                       font=("Helvetica",12,"bold"),background="green")
symbolLabel.grid(row=2,column=0)
NumberLabel = tk.Label(mainWindow,text="Number of Numbers",
                       font=("Helvetica",12,"bold"),background="green")
NumberLabel.grid(row=3,column=0)
letterE = tk.Entry()
letterE.grid(row=1,column=1)
symbolE = tk.Entry()
symbolE.grid(row=2,column=1)
numberE = tk.Entry()
numberE.grid(row=3,column=1)
resultButton = tk.Button(mainWindow,text="Generate",
                         font=("Helvetica",14,"bold"),command=Generate_The_Password,
                         fg="RED",width=10,padx=0,pady=0,background="black")
resultButton.grid(row=4,column=1)
passwordresult = tk.Label(mainWindow,text="The Password:",
                          font=("Helvetica",15,"bold"),background="green")
passwordresult.grid(row=5,column=0)
result = tk.Label(mainWindow,text="-------------------------",
                  font=("Helvetica",15,"bold"),background="green",fg="black")
result.grid(row=5,column=1)
mainWindow.resizable(False, False)
mainWindow.mainloop()
##############################################


