#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys
import argparse

from requests.exceptions import ConnectionError
from xml.dom import minidom


def download(url):
	try:

		r=requests.get(url)

		if r.status_code != 200:
			sys.stderr.write("error")
			return None

	except ConnectionError as e:
		sys.stdout.write("No hay conexion a internet. \n")
		return None
		
	return r.text

#----------------------------------------------------------------------------------------------------------------

def buscar(url,valor,txt):
			sys.stdout.write("\nBuscando: %s \n" % txt)

			r = download(url)
			if r:
				TextoWeb = r[:10000000]
				
				q = TextoWeb.find(valor)
				if (q==-1):
					sys.stdout.write("No existe el texto a buscar. \n")
				else:
					sys.stdout.write("Texto encontrado en la web. \n")

			else:
				sys.stdout.write("No existe la web. \n")
	

#----------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='%(prog)s is an ArgumentParser demo')

    parser.add_argument("-w","--web", help="Página web", default = "https://sourceforge.net/projects/zorin-os/files/15")
    parser.add_argument("-b","--buscar", help="Texto a buscar", default = "Lite")
    parser.add_argument("-t","--texto", help="Texto idenficativo", default = "Zorin 15 Lite")    
    parser.add_argument("-f","--file", help="Fichero con las webs y busquedas definidas", default = "")
    args = parser.parse_args()


    if args.file != "":
		xmldoc = minidom.parse(args.file)
		itemlist = xmldoc.getElementsByTagName("buscar")

		for i in itemlist:
			buscar(i.attributes["web"].value,i.attributes["valor"].value,i.attributes["texto"].value)
             
    else :
		buscar(args.web,args.buscar,args.texto)

    try:
        input("Press enter to continue")
    except SyntaxError:
        pass


