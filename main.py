import tkinter as tk

from festival_lib.controller import *


# 🔵 baza danych

create_db()

add_test_data()


# 🔵 okno

okno = tk.Tk()

okno.title("Film Festival System")

okno.geometry("1000x650")


# 🔵 RAMKA LISTA FESTIWALI

ramka_lista_festiwali = tk.Frame(okno)

ramka_lista_festiwali.pack(
    side="left",
    padx=20,
    pady=20
)


label_lista_festiwali = tk.Label(
    ramka_lista_festiwali,
    text="Lista festiwali",
    font=("Arial", 14)
)

label_lista_festiwali.pack()


# 🔵 LISTBOX

listbox_lista_festiwali = tk.Listbox(
    ramka_lista_festiwali,
    width=45,
    height=20
)

listbox_lista_festiwali.pack(pady=10)


# 🔵 BUTTON ODŚWIEŻ

button_odswiez = tk.Button(
    ramka_lista_festiwali,
    text="Odśwież listę"
)

button_odswiez.pack(pady=5)


# 🔵 RAMKA FORMULARZ

ramka_formularz = tk.Frame(okno)

ramka_formularz.pack(
    side="left",
    padx=20,
    pady=20
)


label_formularz = tk.Label(
    ramka_formularz,
    text="Dodaj festiwal",
    font=("Arial", 14)
)

label_formularz.pack()


# 🔵 NAZWA

label_nazwa = tk.Label(
    ramka_formularz,
    text="Nazwa festiwalu"
)

label_nazwa.pack()

entry_nazwa = tk.Entry(
    ramka_formularz,
    width=35
)

entry_nazwa.pack(pady=5)


# 🔵 MIASTO

label_miasto = tk.Label(
    ramka_formularz,
    text="Miasto"
)

label_miasto.pack()

entry_miasto = tk.Entry(
    ramka_formularz,
    width=35
)

entry_miasto.pack(pady=5)


# 🔵 SZEROKOŚĆ

label_szerokosc = tk.Label(
    ramka_formularz,
    text="Szerokość geograficzna"
)

label_szerokosc.pack()

entry_szerokosc = tk.Entry(
    ramka_formularz,
    width=35
)

entry_szerokosc.pack(pady=5)


# 🔵 DŁUGOŚĆ

label_dlugosc = tk.Label(
    ramka_formularz,
    text="Długość geograficzna"
)

label_dlugosc.pack()

entry_dlugosc = tk.Entry(
    ramka_formularz,
    width=35
)

entry_dlugosc.pack(pady=5)


# 🔵 ODŚWIEŻANIE LISTY

def refresh_festival_list():

    listbox_lista_festiwali.delete(0, tk.END)

    festivals = read_festival_data()

    for festival in festivals:

        listbox_lista_festiwali.insert(
            tk.END,
            f"{festival.id} | {festival.name} | {festival.city}"
        )


# 🔵 DODAWANIE FESTIWALU

def add_festival_gui():

    name = entry_nazwa.get()

    city = entry_miasto.get()

    latitude = float(entry_szerokosc.get())

    longitude = float(entry_dlugosc.get())

    add_festival(
        name,
        city,
        latitude,
        longitude
    )

    refresh_festival_list()


# 🔵 USUWANIE FESTIWALU

def delete_festival_gui():

    selected = listbox_lista_festiwali.curselection()

    if selected:

        festival_text = listbox_lista_festiwali.get(selected)

        festival_id = int(
            festival_text.split("|")[0]
        )

        delete_festival(festival_id)

        refresh_festival_list()


# 🔵 EDYCJA FESTIWALU

def update_festival_gui():

    selected = listbox_lista_festiwali.curselection()

    if selected:

        festival_text = listbox_lista_festiwali.get(selected)

        festival_id = int(
            festival_text.split("|")[0]
        )

        name = entry_nazwa.get()

        city = entry_miasto.get()

        latitude = float(entry_szerokosc.get())

        longitude = float(entry_dlugosc.get())

        update_festival(
            festival_id,
            name,
            city,
            latitude,
            longitude
        )

        refresh_festival_list()


# 🔵 BUTTON DODAJ

button_dodaj = tk.Button(
    ramka_formularz,
    text="Dodaj festiwal",
    width=25,
    command=add_festival_gui
)

button_dodaj.pack(pady=10)


# 🔵 BUTTON EDYTUJ

button_edytuj = tk.Button(
    ramka_formularz,
    text="Edytuj festiwal",
    width=25,
    command=update_festival_gui
)

button_edytuj.pack(pady=5)


# 🔵 BUTTON USUŃ

button_usun = tk.Button(
    ramka_formularz,
    text="Usuń festiwal",
    width=25,
    command=delete_festival_gui
)

button_usun.pack(pady=5)


# 🔵 BUTTON MAPA

button_mapa = tk.Button(
    ramka_formularz,
    text="Otwórz mapę",
    width=25,
    command=show_map
)

button_mapa.pack(pady=20)


# 🔵 BUTTON ODŚWIEŻ

button_odswiez.config(
    command=refresh_festival_list
)


# 🔵 START

refresh_festival_list()

okno.mainloop()