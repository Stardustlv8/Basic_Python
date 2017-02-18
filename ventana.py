#Primer Ventana
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file('ventana1.glade')

window = builder.get_object('window1')
label1 = builder.get_object('label1')
label1.set_text("Hola mundo!")
window.show_all()

Gtk.main()

