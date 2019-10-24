#!/usr/bin/python3
import pyqrcode 
# AUTHOR: MATHEUS OLIVEIRA
alvo=pyqrcode.create(input("Digite a URL"))
alvo.svg('arq.svg')
print(alvo.terminal(quiet_zone=1))
