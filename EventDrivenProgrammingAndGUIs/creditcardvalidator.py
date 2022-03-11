#Cameron Cheng

#Another note, I left print statements commented out, but I thought
#to leave them there in case you want to see certain things and how it works.

from tkinter import *
from tkinter.messagebox import *


def main():
    def validate(cardnum):
        cardnum2 = cardnum


        #Since the input is a string I compare it to the string of a number for the 4
        #different card types. After that I use a while loop to find the second digits
        #from right to left and then add them to a list. I then take the int values of
        #the numbers in the list, double them, then add them together. I do that same process but for
        #the remaining digits, add the two totals, and see if it is divisible by 10.


        if cardnum[0] == '4':
            # print('Visa')
            secdig = []
            secdigadded = 0

            while len(cardnum) > 1:
                secdig.append(cardnum[-2])
                cardnum = cardnum[0:len(cardnum) - 2]

                if len(cardnum) == 1:
                    break

            for x in secdig:
                if int(x) * 2 > 9:
                    secdigadded += ((int(x) * 2) % 10) + 1
                else:
                    secdigadded += int(x) * 2

            firdig = []
            firdigadded = 0

            while len(cardnum2) > 0:
                firdig.append(cardnum2[-1])
                cardnum2 = cardnum2[0:len(cardnum2) - 2]

                if len(cardnum2) == 0:
                    break

            for x in firdig:
                firdigadded += int(x)
            # print(secdigadded)
            # print(firdigadded)
            # print(secdigadded + firdigadded)

            if (secdigadded + firdigadded) % 10 == 0:
                showinfo('valid credit card','This is a Valid Visa')
            else:
                showinfo('Not Valid', 'This is not a valid Visa')

        elif cardnum[0] == '5':
            # print('Mastercard')
            secdig = []
            secdigadded = 0

            while len(cardnum) > 1:
                secdig.append(cardnum[-2])
                cardnum = cardnum[0:len(cardnum) - 2]

                if len(cardnum) == 1:
                    break

            for x in secdig:
                if int(x) * 2 > 9:
                    secdigadded += ((int(x) * 2) % 10) + 1
                else:
                    secdigadded += int(x) * 2

            firdig = []
            firdigadded = 0

            while len(cardnum2) > 0:
                firdig.append(cardnum2[-1])
                cardnum2 = cardnum2[0:len(cardnum2) - 2]

                if len(cardnum2) == 0:
                    break

            for x in firdig:
                firdigadded += int(x)
            # print(secdigadded)
            # print(firdigadded)
            # print(secdigadded + firdigadded)

            if (secdigadded + firdigadded) % 10 == 0:
                showinfo('valid credit card','This is a Valid Mastercard')
            else:
                showinfo('Not Valid', 'This is not a valid Mastercard')

        elif cardnum[0] == '6':
            # print('Discover')
            secdig = []
            secdigadded = 0

            while len(cardnum) > 1:
                secdig.append(cardnum[-2])
                cardnum = cardnum[0:len(cardnum) - 2]

                if len(cardnum) == 1:
                    break

            for x in secdig:
                if int(x) * 2 > 9:
                    secdigadded += ((int(x) * 2) % 10) + 1
                else:
                    secdigadded += int(x) * 2

            firdig = []
            firdigadded = 0

            while len(cardnum2) > 0:
                firdig.append(cardnum2[-1])
                cardnum2 = cardnum2[0:len(cardnum2) - 2]

                if len(cardnum2) == 0:
                    break

            for x in firdig:
                firdigadded += int(x)
            # print(secdigadded)
            # print(firdigadded)
            # print(secdigadded + firdigadded)

            if (secdigadded + firdigadded) % 10 == 0:
                showinfo('valid credit card','This is a Valid Discover')
            else:
                showinfo('Not Valid', 'This is not a valid Discover')

        elif cardnum[:2] == '37':
            # print('American Express')
            secdig = []
            secdigadded = 0

            while len(cardnum) > 1:
                secdig.append(cardnum[-2])
                cardnum = cardnum[0:len(cardnum) - 2]

                if len(cardnum) == 1:
                    break

            for x in secdig:
                if int(x) * 2 > 9:
                    secdigadded += ((int(x) * 2) % 10) + 1
                else:
                    secdigadded += int(x) * 2

            firdig = []
            firdigadded = 0

            while len(cardnum2) > 0:
                firdig.append(cardnum2[-1])
                cardnum2 = cardnum2[0:len(cardnum2) - 2]

                if len(cardnum2) == 0:
                    break

            for x in firdig:
                firdigadded += int(x)
            # print(secdigadded)
            # print(firdigadded)
            # print(secdigadded + firdigadded)

            if (secdigadded + firdigadded) % 10 == 0:
                showinfo('valid credit card','This is a Valid American Express')
            else:
                showinfo('Not Valid', 'This is not a valid American Express')

        else:
            # print('invalid number format')
            showwarning('invalid number format', 'This is an invalid format')

    def fetch():
        # print('Input => "%s"' % ent.get())

        # When this function is called it checks the length of the credit card number first
        # before allowing the program to continue.

        if len(ent.get()) > 16:
            # print("this card number is too long")
            showwarning("this card number is too long","this card number is too long")
        elif len(ent.get()) < 13:
            # print("this card number is too short")
            showwarning("this card number is too short","this card number is too short")
        else:
            validate(ent.get())





    root = Tk()
    ent = Entry(root)
    Label(root, text='Enter a credit card number:').pack(side=TOP)
    ent.pack(side=TOP, fill=X)
    ent.focus()
    ent.bind('<Return>', (lambda event: fetch()))

    btn = Button(root, text='Verify', command=fetch)
    btn.pack(side=LEFT)
    root.mainloop()


if __name__ == "__main__":
    main()