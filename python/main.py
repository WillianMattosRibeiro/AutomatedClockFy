from gui_utils import check_value
from tkinter import *
from clockfy_time_entry import ClockfyTimeEntry
import os

cte = ClockfyTimeEntry()
listbox = None


def callback_projects(selection):
    for project in cte.projects_list:
        if project["name"] == selection:
            lista_valores["project"] = project["id"]
            break


def call_add_tag(selection):
    for tag in cte.tags_list:
        if tag["name"] == selection:
            lista_valores["tags"].append(tag["id"])
            listbox.insert(0, tag["name"])
            break


def call_remove_tag():
    lista_valores["tags"] = []
    listbox.delete(0, END)


def call_time_entry():
    global lista_valores
    from datetime import datetime
    args = {
        "description": lista_valores["description"].get(),
        "project": lista_valores["project"],
        "tags": lista_valores["tags"],
        "billable": lista_valores["billable"].get(),
        "start_hour": lista_valores["start_hour"].get(),
        "end_hour": lista_valores["end_hour"].get(),
        "date": datetime.strptime(lista_valores["date"].get_date(), '%m/%d/%y').strftime("%Y-%m-%d")
    }

    cte.post_data_to_clockfy(args)

    print('quitting')
    master.destroy()


lista_campos = ['description', 'project', 'tags', 'billable', 'start_hour', 'end_hour', 'date']
lista_valores = {"tags": []}

master = Tk()
master.title("Automated Clockfy")
master.resizable(False, False)  # This code helps to disable windows from resizing
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/")
master.iconbitmap(r'{0}/images/clockify-icon.ico'.format(root_dir))
master.geometry("400x650+10+10")

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
    elif campo == "project":
        Label(fone, text=campo).grid(row=row, padx=5)
        project_list_names = [str(project["name"]) for project in cte.projects_list]
        option_value = StringVar(fone, value=project_list_names[0])
        option_value.set(project_list_names[0])
        field = OptionMenu(fone, option_value, *project_list_names, command=callback_projects)
        field.grid(row=row, column=1, pady=5)
    elif campo == "tags":
        Label(fone, text=campo).grid(row=row, padx=5)
        tag_list_names = [str(tag["name"]) for tag in cte.tags_list]

        option_value = StringVar(fone, value=tag_list_names[0])
        option_value.set(tag_list_names[0])
        field = OptionMenu(fone, option_value, *tag_list_names, command=call_add_tag)
        field.grid(row=row, column=1, pady=5)

        Button(fone, text='Clear Tags', command=call_remove_tag).grid(row=row, column=3, pady=5)

        row += 1
        listbox = Listbox(fone)
        listbox.grid(row=row, column=1, pady=5)

    else:
        v = StringVar(fone, value=check_value(campo))
        Label(fone, text=campo).grid(row=row, padx=5)
        field = Entry(fone, textvariable=v, width=30)
        field.grid(row=row, column=1, pady=5)
        lista_valores[campo] = field
    row += 1

Button(ftwo, text='Send', command=call_time_entry).grid(row=row, column=1, pady=5)

mainloop()
