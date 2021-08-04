# Anti-Idle

## Objetivo

Ejercicio práctico realizado con la finalidad de darle solución al proyecto propuesto [Looking Busy - Chapter 18: Controlling the Keyboard and Mouse with GUI Atomation - Automate the Boring Stuff with Python, 1st Edition](https://nostarch.com/automatestuff2)

## Descripción

El script detecta cuando no se tiene ninguna interacción por el cursor y da de alta un timer para realizar un movimiento horizontal del cursor a la mitad de la pantalla cada 10 segundos. En cuanto el usuario realiza una interacción el timer se libera y vuelve a entrar en acción si vuelve a detectar que no hay movimiento.

## Instalación

### Windows

>py.exe -m pip3 install -r win-requirements.txt

### MacOS

>pip3 install -r macos-requirements.txt

### Linux

>sudo apt install scrot python3-tk python3-dev

>pip3 install -r linux-requirements.txt


## Uso

>python3 anti-idle.py

### Demo

![Demo](images/demo.gif)
