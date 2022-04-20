# INICIALIZACAO
from utils.will_utils import get_json
from clockfy_utils import get_tags, get_projects, get_user, set_time_entry
from datetime import datetime
import pytz

# INTERFACE GRAFICA






from tkinter import *

def get_values():
    global lista_valores
    for valores in lista_valores:
        print(valores.get())
    print('quitting')
    master.destroy()

lista_campos = ['description', 'projeto', 'tags', 'billable', 'hora_inicio', 'hora_fim', 'data']
lista_valores = []

master = Tk()
row=0
for campo in lista_campos:
    v = StringVar(master, value='default text')
    e = Entry(master, textvariable=v)
    Label(master, text=campo).grid(row=row)
    field = Entry(master)
    field.grid(row=row, column=1)
    lista_valores.append(field)
    row +=1

Button(master, text='Enviar', command=get_values).grid(row=row, column=1, sticky=W, pady=10)

mainloop()










#
# description = Label(window ,text = "Descrição da Atividade").grid(row = 0,column = 0)
# projeto = Label(window ,text = "Projeto").grid(row = 1,column = 0)
# tags = Label(window ,text = "Tag").grid(row = 2,column = 0)
# billable = Label(window ,text = "billable").grid(row = 3,column = 0)
# hora_inicio = Label(window ,text = "Hora de Inicio").grid(row = 3,column = 0)
# hora_fim = Label(window ,text = "Hora de Termino").grid(row = 3,column = 0)
# data = Label(window ,text = "Data").grid(row = 3,column = 0)
#
# description_field = Entry(window).grid(row = 0,column = 1)
# projeto_field = Entry(window).grid(row = 1,column = 1)
# tags_field = Entry(window).grid(row = 2,column = 1)
# billable_field = Entry(window).grid(row = 3,column = 1)
# hora_inicio_field = Entry(window).grid(row = 4,column = 1)
# hora_fim_field = Entry(window).grid(row = 5,column = 1)
# data_field = Entry(window).grid(row = 6,column = 1)
#
#
#


#
# if data == "":
#     tz = pytz.timezone('America/Sao_Paulo')
#     data = datetime.now(tz=tz).strftime("%Y-%m-%d")

##################

# ARGUMENTOS

# args = {
#     "description" : description,
#     "projeto" : projeto,
#     "tags" : [tags],
#     "billable" : billable,
#     "hora_inicio" : hora_inicio,
#     "hora_fim" : hora_fim,
#     "data" : data
# }
#
# print(args)

# CARREGAR PARAMETROS

path_parameters = ".\json\parameters.json"
parameters = get_json(path_parameters)

credentials_file = get_json(parameters["CREDENTIALS_PATH"])

base_url = parameters["API_URL"]

time_entry_path = parameters["TIME_ENTRY_BASE_PATH"]
time_entry_path = time_entry_path.replace("{workspace}", credentials_file["workspace"])

credentials = credentials_file["api_key"]

workspace = credentials_file["workspace"]

headers = {'X-Api-Key': '{}'.format(credentials),
            'Content-Type': 'application/json'}

hour = {"inicio" : hora_inicio,
        "fim" : hora_fim}

# EFETUAR ACOES
# #####################################################

print("capturando usuarios: ")
user = get_user(base_url, headers)
user_id = user["id"]

# - CARREGAR INFORMAÇÔES DE TAGS

print("capturando tags: ")
tag_name = "Reunião"
tags = get_tags(base_url, headers, workspace, tag_name)
tags_list = []
for tag in tags:
    if tag["name"] == tag_name:
        tags_list.append(tag["id"])

# - CARREGAR INFORMAÇÔES DE PROJETO

print("capturando projetos: ")
projects = get_projects(base_url, headers, workspace, user_id=user_id, user_status="ACTIVE")
project_id = None
for project in projects:
    if project["name"] == "Desenvolvimento de Conteúdo":
        project_id = project['id']

# - MONTAR A CHAMADA
debbug=True
set_time_entry(base_url, headers, workspace, data, hour, description, project_id, tags_list, debbug=debbug)

