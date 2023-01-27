import tkinter as tk


ventana = tk.Tk()  # Objeto ventana
ventana.config(width=350, height=500, border=5,
               bg='#397cbe')  # tamaño de la ventana
ventana.wm_geometry('+550+250')
ventana.title('No soy Casio')


class button(tk.Button):
    def __init__(self, master=None, **kw):
        tk.Button.__init__(self, master, **kw)
        self.config(font=("Arial", 20), width=4,
                    height=1, relief='groove', bd=1)


i = 0
initial_0 = tk.StringVar(value='0')
upper_row = tk.StringVar()

punto = {
    'index': 0,
    'state': True
}


def agregar_numero(element):
    global i
    global initial_0
    if i == 0 and display_lower_row.get() == '0':
        initial_0.set(value='')
        display_lower_row.insert(i, element)
        i += 1
    elif i == 0:
        i += 1
        display_lower_row.insert(i, element)
        i += 1
    elif i < 19:
        display_lower_row.insert(i, element)
        i += 1
    else:
        show_error()


def agregar_signo(signo):
    global i
    global punto
    if i > 0:
        display_lower_row.insert(i, signo)
        punto['state'] = True
        i += 1


def decimal():
    global i
    global punto
    if i == 0:
        i += 1
        display_lower_row.insert(i, '.')
        punto['index'] = i
        punto['state'] = False
        i += 1
    elif i != 0 and punto['state'] == True:
        display_lower_row.insert(i, '.')
        punto['index'] = i
        punto['state'] = False
        i += 1
    else:
        pass


def borrar_caracter():
    global i
    global punto
    if i == 0:
        display_lower_row.delete(i)
    elif i > 0:
        i -= 1
        if punto['index'] == i:
            display_lower_row.delete(i)
            punto['state'] = True
        else:
            display_lower_row.delete(i)
    else:
        pass
    if display_lower_row.get() == '0' or display_lower_row.get() == '':
        initial_0.set(value='0')


def clear_all():
    global i
    display_lower_row.delete(0, 'end')
    initial_0.set(value='0')
    upper_row.set(value='')
    punto['state'] = True
    i = 0


def show_error():
    error = tk.Toplevel()
    error.config(width=100, height=100, border=3)
    error.geometry('+610+320')
    label = tk.Label(error, text='Max Digits Reached', justify='center')
    label.grid(sticky='we', row=0)
    boton = tk.Button(error, text='OK', command=error.destroy)
    boton.grid(row=1)


def operacion():
    global i
    ecuation = display_lower_row.get()
    if i != 0:
        try:
            result = str(eval(ecuation))
            display_lower_row.delete(0, 'end')
            display_lower_row.insert(0, result)
            upper_row.set(value=ecuation)
            new_i = len(result)
            i = new_i
        except:
            result = 'APRETASTE MAL SALAMIN'
            display_lower_row.delete(0, 'end')
            display_lower_row.insert(0, result)
            punto['state'] = True
            i = 0


def show_alert():
    alert = tk.Toplevel()
    alert.config(width=350, height=500, border=3)
    label = tk.Label(
        alert, text='TOLD YOU NOT TO PRESS THE BUTTON\nMOTHERF***ER', justify='center')
    label.grid(column=0, row=1, sticky='we')
    image = tk.PhotoImage(file="./jackson_small.PNG")
    image_label = tk.Label(alert, image=image, state='active')
    image_label.grid(column=0, row=0, sticky='new')
    image_label.image = image
    boton = tk.Button(alert, text='I\'m a pussy', command=alert.destroy)
    boton.grid(column=0, row=2)


display_frame = tk.Frame(ventana)
display_frame.config(bg='#3b5998', relief="sunken", bd=10)
display_frame.grid(row=0, column=0, padx=1, pady=10)

display_upper_row = tk.Label(display_frame)
display_upper_row.config(textvariable=upper_row,
                         bg='#adadad', font=('Arial', 12), anchor='e')
display_upper_row.grid(columnspan=4, column=0, row=1, sticky='we')

display_lower_row = tk.Entry(display_frame)
display_lower_row.config(textvariable=initial_0,
                         bg='#c2c2c2', font=('Arial', 20), justify='right')
display_lower_row.grid(columnspan=4, column=0, row=2, sticky='we')

buttons_frame = tk.Frame(ventana, bg='#397cbe')
buttons_frame.grid(rowspan=4, columnspan=4, column=0,
                   padx=1, pady=10)

button_1 = button(buttons_frame, text='1',
                  command=lambda: agregar_numero('1'), bg='light grey')
button_1.grid(column=0, row=1, padx=1, pady=1)

button_2 = button(buttons_frame, text='2',
                  command=lambda: agregar_numero('2'), bg='light grey')
button_2.grid(column=1, row=1, padx=1, pady=1)

button_3 = button(buttons_frame, text='3',
                  command=lambda: agregar_numero('3'), bg='light grey')
button_3.grid(column=2, row=1, padx=1, pady=1)

button_4 = button(buttons_frame, text='4',
                  command=lambda: agregar_numero('4'), bg='light grey')
button_4.grid(column=0, row=2, padx=1, pady=1)

button_5 = button(buttons_frame, text='5',
                  command=lambda: agregar_numero('5'), bg='light grey')
button_5.grid(column=1, row=2, padx=1, pady=1)

button_6 = button(buttons_frame, text='6',
                  command=lambda: agregar_numero('6'), bg='light grey')
button_6.grid(column=2, row=2, padx=1, pady=1)

button_7 = button(buttons_frame, text='7',
                  command=lambda: agregar_numero('7'), bg='light grey')
button_7.grid(column=0, row=3, padx=1, pady=1)

button_8 = button(buttons_frame, text='8',
                  command=lambda: agregar_numero('8'), bg='light grey')
button_8.grid(column=1, row=3, padx=1, pady=1)

button_9 = button(buttons_frame, text='9',
                  command=lambda: agregar_numero('9'), bg='light grey')
button_9.grid(column=2, row=3, padx=1, pady=1)

button_0 = button(buttons_frame, text='0',
                  command=lambda: agregar_numero('0'), bg='light grey')
button_0.grid(column=1, row=4, padx=1, pady=1)

button_punto = button(
    buttons_frame, text='.', command=lambda: decimal())
button_punto.grid(column=0, row=4, padx=1, pady=1)

button_suma = button(buttons_frame, text='+',
                     command=lambda: agregar_signo('+'))
button_suma.grid(column=4, row=1, padx=1, pady=1)

button_resta = button(buttons_frame, text='-',
                      command=lambda: agregar_signo('-'))
button_resta.grid(column=4, row=2, padx=1, pady=1)

button_multiplicacion = button(
    buttons_frame, text='x', command=lambda: agregar_signo('*'))
button_multiplicacion.grid(column=4, row=3, padx=1, pady=1)

button_division = button(buttons_frame, text='÷',
                         command=lambda: agregar_signo('/'))
button_division.grid(column=4, row=4, padx=1, pady=1)

button_erase = button(buttons_frame, text='<<',
                      command=lambda: borrar_caracter())
button_erase.grid(column=4, row=0, padx=1, pady=1)

button_clear = button(buttons_frame, text='C', command=lambda: clear_all())
button_clear.grid(column=0, row=0, padx=1, pady=1)

button_igual = button(buttons_frame, text='=',
                      command=lambda: operacion(), bg='light blue')
button_igual.grid(column=2, row=4, padx=1, pady=1)

button_fake = tk.Button(
    buttons_frame, text='DO NOT PRESS\nOUT OF SERVICE', command=lambda: show_alert(),
    justify='center')
button_fake.config(font=("Arial", 10), height=1, relief='groove', bd=1)
button_fake.grid(column=1, row=0, padx=1, pady=1, columnspan=2, sticky='wens')

ventana.mainloop()
