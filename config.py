#! /usr/bin/python
# -*- encoding: utf-8 -*-

import secret

API_URL = "https://api.invertironline.com"

username=secret.u 
password=secret.p 

PAISES = [
    'estados_Unidos', 
    'argentina'
]


MERCADOS = [
    'bCBA', 
    'nYSE', 
    'nASDAQ', 
    'aMEX', 
    'bCS', 
    'rOFX'
]

TIPO_TITULO = [
    'oPCIONES', 
    'cEDEARS', 
    'tITULOSPUBLICOS', 
    'aCCIONES', 
    'cUPONESPRIVADOS', 
    'fONDOSDEINVERSION', 
    'aDR', 
    'iNDICES', 
    'bOCON', 
    'bONEX', 
    'cERTIFICADOSPAR', 
    'oBLIGACIONESNEGOCIABLES', 
    'oBLIGACIONESPYME', 
    'cUPONESOBL', 
    'lETRAS', 
    'lETES', 
    'bONOS', 
    'fUTURO', 
    'fondoComundeInversion'
]

TITULO_PLAZO = ['t0', 't1', 't2']

MONEDA = [
    'peso_Argentino', 
    'dolar_Estadounidense', 
    'real', 
    'peso_Mexicano', 
    'peso_Chileno', 
    'yen', 
    'libra', 
    'euro', 
    'peso_Peruano', 
    'peso_Colombiano', 
    'peso_Uruguayo'
]
