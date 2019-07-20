#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def mainQuit(builder):
    Gtk.main_quit()

def onAnadirClicked(builder):
    web = eWeb.get_text()
    val = eValor.get_text()
    txt = eTexto.get_text()
    mc.append([web,val,txt])
	#FALTA GRABAR EL FICHERO XML


def onEliminarClicked(builder):
        if len(mc) != 0:
            # get the selection
            (model, iter) = selec.get_selected()
            # if there is a selection, print a message in the terminal
            # and remove it from the model
            if iter is not None:
                print("%s has been removed" % (model[iter][0]))
                mc.remove(iter)
            # otherwise, ask the user to select something to remove
            else:
                print("Select a title to remove")
        # else, if there are no entries in the model, print "Empty list"
        # in the terminal
        else:
            print("Empty list")
	

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

window = builder.get_object("window1")
window.show_all()

Gtk.main()

