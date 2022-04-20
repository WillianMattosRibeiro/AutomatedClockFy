from gui_utils import check_value
from tkinter import *
from clockfy_time_entry import ClockfyTimeEntry


def call_time_entry():
    global lista_valores
    from datetime import datetime
    args = {
        "description": lista_valores["description"].get(),
        "projeto": lista_valores["project"].get(),
        "tags": lista_valores["tags"].get(),
        "billable": lista_valores["billable"].get(),
        "start_hour": lista_valores["start_hour"].get(),
        "end_hour": lista_valores["end_hour"].get(),
        "date": datetime.strptime(lista_valores["date"].get_date(), '%m/%d/%y').strftime("%Y-%m-%d")
    }

    cte = ClockfyTimeEntry()
    cte.post_data_to_clockfy(args)

    print('quitting')
    master.destroy()


lista_campos = ['description', 'project', 'tags', 'billable', 'start_hour', 'end_hour', 'date']
lista_valores = {}

master = Tk()
master.title("Automated Clockfy")
master.resizable(None, None)
fone = Frame(master)
ftwo = Frame(master)

fone.pack(pady=10)
ftwo.pack(pady=10)

row = 0
for campo in lista_campos:
    if campo == "date":
        from tkcalendar import Calendar
        from datetime import datetime
        field = Calendar(
            ftwo,
            selectmode="day",
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day
        )
        field.grid(row=row, column=1, pady=5)
        lista_valores[campo] = field
    else:
        v = StringVar(fone, value=check_value(campo))
        Label(fone, text=campo).grid(row=row, padx=5)
        field = Entry(fone, textvariable=v, width=30)
        field.grid(row=row, column=1, pady=5)
        lista_valores[campo] = field
    row += 1

Button(ftwo, text='Send', command=call_time_entry).grid(row=row, column=1, pady=5)

mainloop()
