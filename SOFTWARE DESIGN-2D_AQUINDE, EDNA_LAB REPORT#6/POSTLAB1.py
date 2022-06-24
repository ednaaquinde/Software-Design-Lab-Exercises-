def CelsiusToFahenheit(Celsius, entry):

  #Celsius = int(input("Enter a temperature in Celsius: "))

  Fahrenheit = 9.0/5.0 * float(Celsius) + 32

  entry. delete(0, 'end')

  entry.insert(0, str(Fahrenheit))

def FahenheitToCelsius(Fahrenheit, entry):

  #!Fahrenheit = int(input("Enter a temperature in Fahrenheit: "))

  Celsius = (float(Fahrenheit) - 32) * 5.0/9.0

  entry. delete(0, 'end')

  entry.insert(0, str(Celsius))

def main():

   window = Tkinter.Tk()

   window.title("Grid")

   lb = Tkinter.Label(window, text='Fahrenheit')

   lb.grid (row=0,column=0)

   lb1=Tkinter.Label(window,text='Celsius:')

   lb1.grid (row=0,column=1)

   en =Tkinter. Entry(window, justify='right')

   en.grid(row=1,column=0)

   en.insert(0, "32.0")

   en1=Tkinter.Entry(window, justify='right')

   en1.grid(row=1,column=1)

   en1.insert(0, "0.0")

   btnFtoc =Tkinter.Button(window, text='>>>>', command=lambda: FahenheitToCelsius(en.get(), en1))

   btnFtoc.grid(row=2,column=0)

   btnCtoF =Tkinter.Button(window, text='<<<<', command=lambda:  CelsiusToFahenheit(en1.get(), en))

   btnCtoF.grid(row=2,column=1)

   window.mainloop()

if __name__ == '__main__':
    main ()

