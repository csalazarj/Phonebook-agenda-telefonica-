# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:58:13 2020

@author: ThunderWolf3299
"""

import os
import time

FOLDER = 'contacts/'  # carpeta de contactos
EXTENSION = '.txt'
LAPSE = 0.8

# contactos
class Contact:
    def __init__(self, name, phone, category):
        self.name = name
        self.phone = phone
        self.category = category

def app():
    # REVISA SI LA CARPETA YA EXISTE
    create_directory()
    
    # MUESTRA EL MENÚ DE OPCIONES
    show_menu()
    
    # PREGUNTAR AL USUARIO LA ACCIÓN A UTILIZAR
    ask = True
    while ask:
        option = input('Select an option: \r\n')
        option = int(option)
        
    # EJECUTAR LAS OPCIONES
        if option == 1:
            time.sleep(LAPSE)
            add_contact()
            ask = False
            
        elif option == 2:
            time.sleep(LAPSE)
            update_contact()
            ask = False
        
        elif option == 3:
            time.sleep(LAPSE)
            see_contacts()
            ask = False
            
        elif option == 4:
            time.sleep(LAPSE)
            search_contact()
            ask = False
            
        elif option == 5:
            time.sleep(LAPSE)
            delete_contact()
            ask = False
        
        elif option == 6:
            ask = False
            print('-------------GOOD BYE!!-----------')
            time.sleep(LAPSE)
            break
        
        else:
            print('OPTION INVALID, TRY AGAIN')

        
def add_contact():
    print('\r\nWrite the data to add new contact\r\n')
    name_contact = input('Name´s contact:\r\n')
    
    # REVISAR SI YA EXISTE EL NOMBRE ANTES DE CREARLO
    exist = os.path.isfile(FOLDER + name_contact + EXTENSION)
    
    if not exist:
        with open(FOLDER + name_contact + EXTENSION, 'w') as file:
            
            phone_contact = input('Enter the phone number: \r\n')
            category_contact = input('Enter the category: \r\n')
            
            # INSTANCIAR LA CLASE
            contact = Contact(name_contact,phone_contact,category_contact)
            
            # ESCRIBIR EN EL ARCHIVO
            file.write('Name: ' + name_contact + '\r\n')
            file.write('Phone Number: ' + contact.phone + '\r\n')
            file.write('Name: ' + contact.category + '\r\n')
            
            print('\r\nCONTACT CREATED SUCCESFULLY !! \r\n')
            
    else:
        print('\r\nTHE CONTACT ALREADY EXIST\r\n')
    
    # REINICIAR LA APP
    time.sleep(LAPSE)
    app()
    
    
def update_contact():
    print('\r\n')
    previous_name = input('Contact´s name to update:\r\n')
    
    # REVISAR SI YA EXISTE EL NOMBRE ANTES DE EDITARLO
    exist = contact_exist(previous_name)
    
    if exist:
        with open(FOLDER + previous_name + EXTENSION, 'w') as file:
            name_contact = input('Enter new name:\r\n')
            phone_contact = input('Enter new phone number: \r\n')
            category_contact = input('Enter new the category: \r\n')
            
            # INSTANCIAR
            contact = Contact(name_contact,phone_contact,category_contact)
        
            # ESCRIBIR EN EL ARCHIVO
            file.write('Name: ' + name_contact + '\r\n')
            file.write('Phone Number: ' + contact.phone + '\r\n')
            file.write('Category: ' + contact.category + '\r\n')
            
            # CERRAR ARCHIVO
            file.close()
            
            # RENOMBRAR EL ARCHIVO
            os.rename(FOLDER + previous_name + EXTENSION , FOLDER + name_contact + EXTENSION)
            
            print('\r\nCONTACT UPDATED SUCCESFULLY !!\r\n')
        
    else:
        print('\r\nTHE CONTACT DOESN´T EXIST\r\n')
    
    # REINICIAR LA APP
    time.sleep(LAPSE)
    app()
    

def see_contacts():

    print('\r\n----------------------')
    files = os.listdir(FOLDER)
    
    folder_txt = [i for i in files if i.endswith(EXTENSION)]
    
    for file in folder_txt:
        with open(FOLDER + file) as contact:
            for line in contact:
                # IMPRIME LOS CONTENIDOS
                print(line.rstrip())
            
            print('----------------------\r\n')
    
    time.sleep(LAPSE)
    app()
            

def search_contact():
    print('\r\n')
    name_contact = input('Enter the contact to search:\r\n')
    
    try:
        with open(FOLDER + name_contact + EXTENSION) as contact:
            print('\r\n -------Contact´s Info-------\r\n')
            for line in contact:
                print(line.rstrip())
            print('\r\n')
        
        print('\r\n --------------------------------\r\n')
        
    except IOError:
        print('THE CONTACT DOESN´T EXIST')
        
    #REINICAR LA APP
    time.sleep(LAPSE)
    app()


def delete_contact():
    print('\r\n')
    name_contact = input('Enter the contact to search:\r\n')
    
    try:
        os.remove(FOLDER + name_contact + EXTENSION)
        print('\r\nCONTACT DELETED SUCCESFULLY\r\n')
    except:
        print('\r\nTHE CONTACT DOESN´T EXIST\r\n')
    
    # REINICIAR LA APP
    time.sleep(LAPSE)
    app()

def show_menu():
    print('OPTIONS:\r\n ')
    print('(1) Add new contact')
    print('(2) Update contact')
    print('(3) See contacts')
    print('(4) Search contact')
    print('(5) Delete contact')
    print('(6) Quit')

    
def create_directory():
    
    if not os.path.exists(FOLDER):
        #crear la carpeta
        os.makedirs(FOLDER)

def contact_exist(name):
    return os.path.isfile(FOLDER + name + EXTENSION)
    
app()