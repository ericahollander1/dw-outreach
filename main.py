import tkinter as Tk

def main():
    color = input("Enter a color: ")
    pluralNoun = input("Enter a plural noun: ")
    celebrity = input("Enter a celebrity: ")
    print("Roses are", color)
    print(pluralNoun + " are blue")
    print("I love", celebrity)
    label = Tk.Label(
                        None,
                        text='The text you want to display',
                        font=('Times', '18'),
                        fg='blue'
                     )
    label.pack()
    label.mainloop()


if __name__ == "__main__":
    main()


