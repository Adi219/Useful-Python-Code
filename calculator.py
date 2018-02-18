## GUI application which serves as a               It was designed by Aditya Chaurasia on 26/02/2017 and
## Calculator, with a 'Command Line'               was last edited on 26/02/2017 14:51 AM. It had 283 lines!


from tkinter import *

class Application(Frame):
    """ GUI application which is a Calculator. """ 
    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)  
        self.grid()
        self.calculation = ""
        self.calculation2 = ""
        self.array = []
        self.array2 = []
        self.create_widgets()

    def create_widgets(self):
        """ Create button and text widgets. """


        ## create the digits buttons
 
        self.digits_1 = Button(self, text = "     1     ", command = self.append1)
        self.digits_1.grid(row = 1, column = 2, sticky = W)

        self.digits_2 = Button(self, text = "    2    ", command = self.append2)
        self.digits_2.grid(row = 1, column = 3, sticky = W)

        self.digits_3 = Button(self, text = "   3    ", command = self.append3)
        self.digits_3.grid(row = 1, column = 4, sticky = W)
        
        self.digits_4 = Button(self, text = "     4     ", command = self.append4)
        self.digits_4.grid(row = 2, column = 2, sticky = W)

        self.digits_5 = Button(self, text = "    5    ", command = self.append5)
        self.digits_5.grid(row = 2, column = 3, sticky = W)

        self.digits_6 = Button(self, text = "   6    ", command = self.append6)
        self.digits_6.grid(row = 2, column = 4, sticky = W)

        self.digits_7 = Button(self, text = "     7     ", command = self.append7)
        self.digits_7.grid(row = 3, column = 2, sticky = W)

        self.digits_8 = Button(self, text = "    8    ", command = self.append8)
        self.digits_8.grid(row = 3, column = 3, sticky = W)

        self.digits_9 = Button(self, text = "   9    ", command = self.append9)
        self.digits_9.grid(row = 3, column = 4, sticky = W)

        self.digits_0 = Button(self, text = "     0     ", command = self.append0)
        self.digits_0.grid(row = 4, column = 2, sticky = W)


        ## Create the other buttons

        self.operator_a = Button(self, text = "    +    ", command = self.appenda)
        self.operator_a.grid(row = 1, column = 5, sticky = W)

        self.operator_s = Button(self, text = "    -     ", command = self.appends)
        self.operator_s.grid(row = 1, column = 6, sticky = W)

        self.operator_mc = Button(self, text = "  MC  ", command = self.appendmc)
        self.operator_mc.grid(row = 1, column = 7, sticky = W)

        self.operator_m = Button(self, text = "    X    ", command = self.appendm)
        self.operator_m.grid(row = 2, column = 5, sticky = W)

        self.operator_d = Button(self, text = "     /    ", command = self.appendd)
        self.operator_d.grid(row = 2, column = 6, sticky = W)

        self.other_lb = Button(self, text = "     (    ", command = self.appendlb)
        self.other_lb.grid(row = 3, column = 5, sticky = W)

        self.other_rb = Button(self, text = "     )    ", command = self.appendrb)
        self.other_rb.grid(row = 3, column = 6, sticky = W)

        self.other_sq = Button(self, text = "Power", command = self.appendp)
        self.other_sq.grid(row = 3, column = 7, sticky = W)

        self.other_r = Button(self, text = " Back ", command = self.appendr)
        self.other_r.grid(row = 4, column = 3, sticky = W)

        self.other_c = Button(self, text = "Clear", command = self.appendc)
        self.other_c.grid(row = 4, column = 4, sticky = W)

        self.other_k = Button(self, text = "Bcksp", command = self.appendk)
        self.other_k.grid(row = 4, column = 5, sticky = W)

        self.other_e = Button(self, text = "Equal ", command = self.appende)
        self.other_e.grid(row = 4, column = 6, sticky = W)

        self.other_ans = Button(self, text = "  Ans  ", command = self.appendans)
        self.other_ans.grid(row = 4, column = 7, sticky = W)

        self.digits_e2 = Button(self, text = "Equal2", command = self.appende2)
        self.digits_e2.grid(row = 5, column = 2, sticky = W)

        self.other_ans = Button(self, text = "Ans2 ", command = self.appendans2)
        self.other_ans.grid(row = 5, column = 3, sticky = W)



        ## create text widget to display result

        self.calc_ent = Entry(self, width = 46)
        self.calc_ent.grid(row = 5, column = 0, columnspan = 1, sticky = W)

        self.result = Text(self, width = 35, height = 10, wrap = WORD)
        self.result.grid(row = 0, column = 0, columnspan = 1, sticky = W)


    def append1(self):
        """ Append "1" to the Calculation """
        self.calculation += "1"
        self.show_calc()

    def append2(self):
        """ Append "2" to the Calculation String """
        self.calculation += "2"
        self.show_calc()

    def append3(self):
        """ Append "3" to the Calculation String """
        self.calculation += "3"
        self.show_calc()

    def append4(self):
        """ Append "4" to the Calculation String """
        self.calculation += "4"
        self.show_calc()

    def append5(self):
        """ Append "5" to the Calculation String """
        self.calculation += "5"
        self.show_calc()

    def append6(self):
        """ Append "6" to the Calculation String """
        self.calculation += "6"
        self.show_calc()

    def append7(self):
        """ Append "7" to the Calculation String """
        self.calculation += "7"
        self.show_calc()

    def append8(self):
        """ Append "8" to the Calculation String """
        self.calculation += "8"
        self.show_calc()
        
    def append9(self):
        """ Append "9" to the Calculation String """
        self.calculation += "9"
        self.show_calc()

    def append0(self):
        """ Append "0" to the Calculation String """
        self.calculation += "0"
        self.show_calc()

    def appenda(self):
        """ Append "+" to the Calculation String """
        self.calculation += "+"
        self.show_calc()

    def appends(self):
        """ Append "-" to the Calculation String """
        self.calculation += "-"
        self.show_calc()

    def appendmc(self):
        """ Clear the Answer Memories """
        self.array = []
        self.array2 = []
        self.show_calc()

    def appendm(self):
        """ Append "*" to the Calculation String """
        self.calculation += "*"
        self.show_calc()
        
    def appendd(self):
        """ Append "/" to the Calculation String """
        self.calculation += "/"
        self.show_calc()

    def appendlb(self):
        """ Append "(" to the Calculation String """
        self.calculation += "("
        self.show_calc()

    def appendrb(self):
        """ Append "/" to the Calculation String """
        self.calculation += ")"
        self.show_calc()

    def appendp(self):
        """ Append "**" to the Calculation String """
        self.calculation += "**"
        self.show_calc()



    def appendr(self):
        """ Revert back to the Calculation """
        self.show_calc()

    def appendc(self):
        """ Clear the Calculator """
        self.calculation = ""
        self.calculation = ""
        self.show_calc()

    def appendk(self):
        """ Remove the last character """
        TempS = ""
        i = 0
        while i <= len(self.calculation)-1:
            if i != len(self.calculation)-1:
                TempS += self.calculation[i]
            i += 1
        self.calculation = TempS
        del TempS
        self.show_calc()

    def appende(self):
        """ Calculate the Answer """
        try:
            self.calculation = eval(self.calculation)
            self.result.delete(0.0, END)
            self.result.insert(0.0, self.calculation)
            self.calculation = str(self.calculation)
            self.array.append(self.calculation)
        except SyntaxError as e:
            self.result.delete(0.0, END)
            self.result.insert(0.0, "There was a error in your calculation. Please fix it.")

    def appendans(self):
        """ Retrieve the previous Answer """
        try:
            self.calculation += "float(self.array[len(self.array)-1])"
        except IndexError as e:
            self.calculation += "0"
        self.show_calc()

    def appendans2(self):
        """ Retrieve the previous typed Answer """
        try:
            self.calculation += "float(self.array2[len(self.array2)-1])"
        except IndexError as e:
            self.calculation += "0"
        self.show_calc()

    def appende2(self):
        """ Calculate the Answer of the typed Calculation """
        try:
            self.calculation2 = self.calc_ent.get()
            self.calculation2 = eval(self.calculation2)
            self.result.delete(0.0, END)
            self.result.insert(0.0, self.calculation2)
            self.calculation2 = str(self.calculation2)
            self.array2.append(self.calculation2)
        except SyntaxError as e:
            self.result.delete(0.0, END)
            self.result.insert(0.0, "There was a error in your calculation. Please fix it.")

    def show_calc(self):
        self.result.delete(0.0, END)
        self.result.insert(0.0, self.calculation)


# main
root = Tk()
root.title("Calculator")
root.geometry("550x300")

app = Application(root)

root.mainloop()
