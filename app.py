#!/usr/bin/env python
# -*- coding: utf-8 -*-
#pylint: disable=locally-disabled

kbinput = ""

while (kbinput != "END"):
    kbinput = input("Insira o valor para converter no seguinte formato de exemplo: 10 PO\n")

    valor, moeda = kbinput.split(" ")
    valor = int(valor)
    moeda.upper()
    resultado = {}

    if (moeda == "PO" or moeda == "GP"):
        cobre = valor * 100
        prata = cobre/100
        ouro = prata/100
        resultado = {"PC": cobre, "PP": prata, "PO": ouro}
    elif (moeda == "PP" or moeda == "SP"):
        cobre = valor * 10
        prata = cobre/100
        ouro = prata/100
        resultado = {"PC": cobre, "PP": prata, "PO": ouro}
    elif (moeda == "PL"):
        cobre = valor * 1000
        prata = cobre/100
        ouro = prata/100
        platina = ouro/100
        resultado = {"PC": cobre, "PP": prata, "PO": ouro, "PL": platina}
    else:
        print("Parâmetros Incorretos.")
        continue

    for each in resultado:
        if (resultado[each] >= 1):
            print("{}: {}".format(each, resultado[each]))
    
        

