from gui_utils import check_value
from tkinter import *
from clockfy_time_entry import ClockfyTimeEntry


def call_time_entry():
    global lista_valores
    args = {
        "description": lista_valores["description"].get(),
        "projeto": lista_valores["projeto"].get(),
        "tags": lista_valores["tags"].get(),
        "billable": lista_valores["billable"].get(),
        "hora_inicio": lista_valores["hora_inicio"].get(),
        "hora_fim": lista_valores["hora_fim"].get(),
        "data": lista_valores["data"].get()
    }

    print(args)

    cte = ClockfyTimeEntry()
    cte.post_data_to_clockfy(args)

    print('quitting')
    master.destroy()


lista_campos = ['description', 'projeto', 'tags', 'billable', 'hora_inicio', 'hora_fim', 'data']
lista_valores = {}

master = Tk()
master.title("Automated Clockfy")
master.minsize(280, 250)
master.maxsize(280, 250)

row = 0
for campo in lista_campos:
    v = StringVar(master, value=check_value(campo))
    Label(master, text=campo).grid(row=row, padx=5)
    field = Entry(master, textvariable=v, width=30)
    field.grid(row=row, column=1, pady=5)
    lista_valores[campo] = field
    row += 1

Button(master, text='Enviar', command=call_time_entry).grid(row=row, column=1, pady=5)

mainloop()
