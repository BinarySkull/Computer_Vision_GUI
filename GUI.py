from Original_images import original
from gray_scale import gray_scale
from gaussian_filter import gaussian_filter
from binary_threshold_filter import Binary_Threshold
from edge_detection import Edge_detector
from Erosion import erosion
from opening import opening

import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    layout = [
             # [sg.Text('Select how you would like to view the license plates')],
              [sg.Button('*  Original Images  *',expand_x = True , expand_y=True, font = ("algerian 14"))],  
              [sg.Button('*  Gray Scale  *',expand_x = True, expand_y=True, font = ("algerian 14"))],
              [sg.Button('* Binary Threshold Filter *',expand_x = True, expand_y=True, font = ("algerian 14"))],
              [sg.Button('*  Gaussian Filter  *',expand_x = True, expand_y=True, font = ("algerian 14"))],
              [sg.Button('*  Edge Detection  *',expand_x = True, expand_y=True, font = ("algerian 14"))],
              [sg.Button('*    Erosion    *',expand_x = True, expand_y=True, font = ("algerian 14"))],
              [sg.Button('*    Opening    *',expand_x = True, expand_y=True, font = ("algerian 14"))],
              [sg.Button('Exit', expand_y=True, expand_x=True,font = "gigi 19"),
               sg.Button('Theme (hover over me)',right_click_menu=theme_menu
                         , tooltip='right click to display themes',expand_x = True, expand_y=True,
                         font="algerian 12 " )
               ]
              
       ]
    return sg.Window('License Plate Filters' , layout , size = (300,350) , no_titlebar = True)    



theme_menu = ['menu',['LightGrey1','DarkRed1', 'DarkGray8','random']]
window = create_window('DarkBlack1')


while True:
    event , values = window.read()
    if event in (sg.WIN_CLOSED ,'Exit'):
        break
    if event == '*  Original Images  *': 
        original()  
    if event == '*  Gray Scale  *':
        gray_scale()
    if event == '*  Gaussian Filter  *':
        gaussian_filter()
    if event == '* Binary Threshold Filter *':
        Binary_Threshold()
    if event == '*  Edge Detection  *':
        Edge_detector()
    if event == '*    Erosion    *':
        erosion()
    if event == '*    Opening    *':
        opening()
    if event in theme_menu[1]:
       window.close()
       window = create_window(event)
        
        
window.close()    
    