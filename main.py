import tkinter as tk

from festival_lib import gui_data

from festival_lib.controller import *


# ==================================================
# 🔵 BAZA
# ==================================================

create_db()

add_test_data()


# ==================================================
# 🔵 OKNO
# ==================================================

okno = tk.Tk()

okno.title("Film Festival System")

okno.geometry("1400x850")


# ==================================================
# 🔵 LEWA STRONA
# ==================================================

ramka_lewa = tk.Frame(okno)

ramka_lewa.pack(
    side="left",
    padx=20,
    pady=20
)


# ==================================================
# 🔵 LISTA FESTIWALI
# ==================================================

ramka_lista_festiwali = tk.LabelFrame(
    ramka_lewa,
    text="Lista festiwali",
    padx=10,
    pady=10
)

ramka_lista_festiwali.pack()


listbox_lista_festiwali = tk.Listbox(
    ramka_lista_festiwali,
    width=45,
    height=20
)

listbox_lista_festiwali.pack()

gui_data.listbox_lista_festiwali = listbox_lista_festiwali


# ==================================================
# 🔵 BUTTONY
# ==================================================

button_odswiez = tk.Button(
    ramka_lewa,
    text="Odśwież listę",
    width=30,
    command=refresh_festival_list
)

button_odswiez.pack(
    pady=5
)


button_usun = tk.Button(
    ramka_lewa,
    text="Usuń festiwal",
    width=30,
    command=delete_festival_gui
)

button_usun.pack(
    pady=5
)


button_mapa = tk.Button(
    ramka_lewa,
    text="Otwórz mapę",
    width=30,
    command=show_map
)

button_mapa.pack(
    pady=20
)


# ==================================================
# 🔵 ŚRODEK
# ==================================================

ramka_srodek = tk.Frame(okno)

ramka_srodek.pack(
    side="left",
    padx=20,
    pady=20
)


# ==================================================
# 🔵 DODAWANIE FESTIWALU
# ==================================================

ramka_dodaj = tk.LabelFrame(
    ramka_srodek,
    text="Dodaj festiwal",
    padx=15,
    pady=15
)

ramka_dodaj.pack()


label_nazwa = tk.Label(
    ramka_dodaj,
    text="Nazwa festiwalu"
)

label_nazwa.pack(anchor="w")


entry_nazwa = tk.Entry(
    ramka_dodaj,
    width=40
)

entry_nazwa.pack(pady=5)

gui_data.entry_nazwa = entry_nazwa


label_miasto = tk.Label(
    ramka_dodaj,
    text="Miasto"
)

label_miasto.pack(anchor="w")


entry_miasto = tk.Entry(
    ramka_dodaj,
    width=40
)

entry_miasto.pack(pady=5)

gui_data.entry_miasto = entry_miasto


label_szerokosc = tk.Label(
    ramka_dodaj,
    text="Szerokość geograficzna"
)

label_szerokosc.pack(anchor="w")


entry_szerokosc = tk.Entry(
    ramka_dodaj,
    width=40
)

entry_szerokosc.pack(pady=5)

gui_data.entry_szerokosc = entry_szerokosc


label_dlugosc = tk.Label(
    ramka_dodaj,
    text="Długość geograficzna"
)

label_dlugosc.pack(anchor="w")


entry_dlugosc = tk.Entry(
    ramka_dodaj,
    width=40
)

entry_dlugosc.pack(pady=5)

gui_data.entry_dlugosc = entry_dlugosc


button_dodaj = tk.Button(
    ramka_dodaj,
    text="Dodaj festiwal",
    width=30,
    command=add_festival_gui
)

button_dodaj.pack(
    pady=15
)


# ==================================================
# 🔵 AKTUALIZACJA
# ==================================================

ramka_update = tk.LabelFrame(
    ramka_srodek,
    text="Aktualizacja festiwalu",
    padx=15,
    pady=15
)

ramka_update.pack(
    pady=20
)


entry_id_update = tk.Entry(
    ramka_update,
    width=40
)

entry_id_update.pack(pady=5)

gui_data.entry_id_update = entry_id_update


entry_nazwa_update = tk.Entry(
    ramka_update,
    width=40
)

entry_nazwa_update.pack(pady=5)

gui_data.entry_nazwa_update = entry_nazwa_update


entry_miasto_update = tk.Entry(
    ramka_update,
    width=40
)

entry_miasto_update.pack(pady=5)

gui_data.entry_miasto_update = entry_miasto_update


entry_szerokosc_update = tk.Entry(
    ramka_update,
    width=40
)

entry_szerokosc_update.pack(pady=5)

gui_data.entry_szerokosc_update = entry_szerokosc_update


entry_dlugosc_update = tk.Entry(
    ramka_update,
    width=40
)

entry_dlugosc_update.pack(pady=5)

gui_data.entry_dlugosc_update = entry_dlugosc_update


button_update = tk.Button(
    ramka_update,
    text="Aktualizuj festiwal",
    width=30,
    command=update_festival_gui
)

button_update.pack(
    pady=15
)


# ==================================================
# 🔵 PRAWA STRONA
# ==================================================

ramka_prawa = tk.Frame(okno)

ramka_prawa.pack(
    side="left",
    padx=20,
    pady=20
)


ramka_szczegoly = tk.LabelFrame(
    ramka_prawa,
    text="Szczegóły festiwalu",
    padx=10,
    pady=10
)

ramka_szczegoly.pack()


label_szczegoly = tk.Label(
    ramka_szczegoly,
    text="Wybierz festiwal z listy",
    justify="left"
)

label_szczegoly.pack()

gui_data.label_szczegoly = label_szczegoly


# ==================================================
# 🔵 START
# ==================================================

refresh_festival_list()

listbox_lista_festiwali.bind(
    "<<ListboxSelect>>",
    load_selected_festival
)

okno.mainloop()