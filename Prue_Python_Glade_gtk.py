#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from xml.dom import minidom

def GrabarcionInicialXML():

	comprobar = ET.Element('Comprobador')
	buscar1 = ET.SubElement(comprobar, 'buscar')
	buscar1.set('web','https://sourceforge.net/projects/zorin-os/files/15')
	buscar1.set('valor','lite')
	buscar1.set('texto','Zorin 15 lite (SI HAY INTERNET LO ENCONTRARA)')

	buscar2 = ET.SubElement(comprobar, 'buscar')
	buscar2.set('web','http://mirrors.evowise.com/linuxmint/stable/')
	buscar2.set('valor','19.2')
	buscar2.set('texto','linux Mint 19.2')

	buscar3 = ET.SubElement(comprobar, 'buscar')
	buscar3.set('web','https://sourceforge.net/projects/zorin-os/files/15')
	buscar3.set('valor','Lite')
	buscar3.set('texto','Zorin 15 Lite')


	# create a new XML file with the results
	mydata = ET.tostring(comprobar)
	myfile = open("BuscarEnWeb.xml", "w")
	myfile.write(mydata)

def GrabarXML():
	if len(mc) != 0:
		comprobar = ET.Element('Comprobador')
		for i in range(len(mc)):
			buscar = ET.SubElement(comprobar, 'buscar')
			iter = mc.get_iter(i)			 
			buscar.set('web',mc[iter][0])
			buscar.set('valor',mc[iter][1])
			buscar.set('texto',mc[iter][2])

			#mc.remove(iter)
			
		mydata = ET.tostring(comprobar)
		myfile = open("BuscarEnWeb.xml", "w")
		myfile.write(mydata)

def CargarXML():
	print("Cargar xml...")
	xmldoc = minidom.parse("BuscarEnWeb.xml")
	itemlist = xmldoc.getElementsByTagName("buscar")

	for i in itemlist:
		web = i.attributes["web"].value
		val = i.attributes["valor"].value
		txt = i.attributes["texto"].value
		mc.append([web,val,txt])

def mainQuit(builder):
    Gtk.main_quit()

def onAnadirClicked(builder):
	web = eWeb.get_text()
	val = eValor.get_text()
	txt = eTexto.get_text()
	mc.append([web,val,txt])
    
	GrabarXML()

def onEliminarClicked(builder):
	if len(mc) != 0:
		(model, iter) = selec.get_selected()
		if iter is not None:
			print("%s has been removed" % (model[iter][0]))
			mc.remove(iter)
		else:
			print("Select a title to remove")
	else:
		print("Empty list")
	
	GrabarXML()
	

builder = Gtk.Builder()
builder.add_from_file("Comprobador.glade")

signals = { "on_bEliminar_clicked" : onEliminarClicked,
			"on_bAñadir_clicked" : onAnadirClicked,
            "gtk_main_quit" : mainQuit }


builder.connect_signals(signals)

eWeb   = builder.get_object("eWeb")
eValor = builder.get_object("eValor")
eTexto = builder.get_object("eTexto")
selec  = builder.get_object("tSelec")
mc     = builder.get_object("modeloComprobador")

#GrabarcionInicialXML()
CargarXML()

window = builder.get_object("window1")
window.show_all()

Gtk.main()

