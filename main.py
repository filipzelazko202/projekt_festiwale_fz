import tkinter as tk

from festival_lib.controller import *


# 🔵 baza danych

create_db()

add_test_data()


# 🔵 okno główne

okno = tk.Tk()

okno.geometry("900x600")

okno.title("Film Festival System")


# 🔵 ramka lista festiwali

ramka_lista_festiwali = tk.Frame(okno)

ramka_lista_festiwali.pack(side="left", padx=20, pady=20)


label_lista_festiwali = tk.Label(
    ramka_lista_festiwali,
    text="Lista festiwali"
)

label_lista_festiwali.pack()


# 🔵 listbox

listbox_lista_festiwali = tk.Listbox(
    ramka_lista_festiwali,
    width=40,
    height=20
)

listbox_lista_festiwali.pack()


# 🔵 ramka formularz

ramka_formularz = tk.Frame(okno)

ramka_formularz.pack(side="left", padx=20, pady=20)


label_formularz = tk.Label(
    ramka_formularz,
    text="Dodaj festiwal"
)

label_formularz.pack()


# 🔵 nazwa

label_nazwa_festiwalu = tk.Label(
    ramka_formularz,
    text="Nazwa festiwalu"
)

label_nazwa_festiwalu.pack()

entry_nazwa_festiwalu = tk.Entry(
    ramka_formularz,
    width=30
)

entry_nazwa_festiwalu.pack()


# 🔵 miasto

label_miasto = tk.Label(
    ramka_formularz,
    text="Miasto"
)

label_miasto.pack()

entry_miasto = tk.Entry(
    ramka_formularz,
    width=30
)

entry_miasto.pack()


# 🔵 szerokość

label_szerokosc = tk.Label(
    ramka_formularz,
    text="Szerokość"
)

label_szerokosc.pack()

entry_szerokosc = tk.Entry(
    ramka_formularz,
    width=30
)

entry_szerokosc.pack()


# 🔵 długość

label_dlugosc = tk.Label(
    ramka_formularz,
    text="Długość"
)

label_dlugosc.pack()

entry_dlugosc = tk.Entry(
    ramka_formularz,
    width=30
)

entry_dlugosc.pack()


# 🔵 odświeżanie listy

def refresh_festival_list():

    listbox_lista_festiwali.delete(0, tk.END)

    festivals = read_festival_data()

    for festival in festivals:

        listbox_lista_festiwali.insert(
            tk.END,
            f"{festival.id} | {festival.name} | {festival.city}"
        )


# 🔵 dodawanie festiwalu

def add_festival_gui():

    name = entry_nazwa_festiwalu.get()

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


# 🔵 button dodaj festiwal

button_dodaj_festiwal = tk.Button(
    ramka_formularz,
    text="Dodaj festiwal",
    command=add_festival_gui
)

button_dodaj_festiwal.pack(pady=10)


# 🔵 button mapa

button_mapa = tk.Button(
    ramka_formularz,
    text="Otwórz mapę",
    command=show_map
)

button_mapa.pack(pady=10)


# 🔵 start

refresh_festival_list()

okno.mainloop()