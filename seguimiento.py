import pyautogui as pg
import webbrowser as web
import time
import pandas as pd

data = pd.read_csv("seguimiento.csv")
data_dict = data.to_dict('list')
celulares = data_dict['LeadNumber']
names = data_dict['FirstName']
vacantes = data_dict['vacante']
gupy = data_dict['Gupy']
encuesta = data_dict['Encuesta']

combo = zip(celulares,names,vacantes,gupy,encuesta)
first = True
for celular,name,vacante,gupy,encuesta in combo:
    time.sleep(2)
    web.open("https://web.whatsapp.com/send?phone=" + celular)
    if first:
        time.sleep(5)
    time.sleep(5)
    pg.typewrite('Hola ' + name + ', ' + 'tenemos una nueva oportunidad laboral para ti!')
    pg.press('enter')
    pg.typewrite('Obtuvimos tus datos durante tu proceso de seleccion con Salud Digna para la vacante: ' + vacante +'.')
    pg.press('enter')
    pg.typewrite('Cumples con los requisitos para esta vacante. Si deseas aplicar de nuevo haz click en este link: ' + gupy)
    pg.press('enter')
    pg.typewrite('Si ya estas trabajando con Salud Digna dejanos saber como ha sido tu experiencia aqui ' + encuesta)
    pg.press('enter')
    time.sleep(5)
    pg.hotkey('ctrl', 'w')
    time.sleep(5)