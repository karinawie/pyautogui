## Relatórios de Cursos 2005

import webbrowser 
import pyautogui
import time
import os

os.chdir('/home/Karina/Downloads/relatorios2011')
downloads_dir = ''
brrt_dir = '/home/Karina/Documents/teste'

webbrowser.open('http://enadeies.inep.gov.br/enadeResultado/site/relatorioDeCurso.seam')
pyautogui.moveTo(1354, 530);pyautogui.click();time.sleep(2);pyautogui.position()
together()

def selectyear():
    pyautogui.moveTo(753,365,duration=1)
    pyautogui.click()
    pyautogui.typewrite('2005')

def selectstate():
    pyautogui.moveTo(753,400,duration=1)
    pyautogui.click()
    pyautogui.typewrite('RS')

def selectcounty():
    pyautogui.moveTo(753,435,duration=1)
    pyautogui.click()
    pyautogui.typewrite('Todos os municípios')

def selectuniversity():
    pyautogui.moveTo(753,465,duration=1)
    pyautogui.click()
    pyautogui.typewrite('Todas as Instituições')
    
def selectcourse():
    pyautogui.moveTo(753,495,duration=2)
    pyautogui.click()
    pyautogui.typewrite('Computação e Informática - Bacharelado em Ciência da COmputação')

def showall():
    pyautogui.moveTo(1160,360,duration=1)
    pyautogui.click()
    time.sleep(2)

def forall():
    pyautogui.press('enter')
    pyautogui.click()
    time.sleep(2)
    pyautogui.hotkey('tab')

def together():
    selectyear(); forall()
    selectstate(); forall()
    selectcounty(); forall()
    selectuniversity(); forall()
    selectcourse(); forall()
    pyautogui.moveTo(472,531,duration=1);pyautogui.press('pesquisar');pyautogui.click()
    showall()
