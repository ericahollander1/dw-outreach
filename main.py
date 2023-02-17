import tkinter as Tk

def main():
    verbing = input("Enter a verb that ends in ing: ")
    number = input("Enter a number: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter a another noun: ")
    adjective = input("Enter an adjective: ")
    kid_name = input("Enter name: ")
    age = input("Enter an age: ")

    # text = f"Roses are {color} \n {plural_noun} are blue \n I love {celebrity}"
    story = f"Computers are amazing pieces of technology that are really great at {verbing}.\n You would be suprised by the amount of computers you see a day! \n " \
            f"In an average day, you see {number} computers. \n Computers can be as big as a {noun1} or as small as a {noun2}.\n  Did you know that {adjective} calculators " \
            f"are computers too?\n  Technology can do so much! \n I wonder what technology will do {kid_name} is {age}!!"


    label = Tk.Label(
                        None,
                        text=story,
                        font=('Times', '24'),
                        fg='blue'
                     )
    label.pack()
    label.mainloop()


if __name__ == "__main__":
    main()


