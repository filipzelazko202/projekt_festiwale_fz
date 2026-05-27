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

okno.geometry("1800x950")

okno.state("zoomed")


# ==================================================
# 🔵 STYLE
# ==================================================

button_font = ("Arial", 10, "bold")

blue = "#0d6efd"
green = "#198754"
red = "#dc3545"
orange = "#fd7e14"
purple = "#6f42c1"


# ==================================================
# 🔵 LEWA KOLUMNA
# ==================================================

ramka_lewa = tk.Frame(okno)

ramka_lewa.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky="n"
)


# ==================================================
# 🔵 FESTIWALE
# ==================================================

ramka_lista_festiwali = tk.LabelFrame(
    ramka_lewa,
    text="Lista festiwali",
    padx=8,
    pady=8,
    font=("Arial", 11, "bold")
)

ramka_lista_festiwali.pack(
    pady=5
)


listbox_lista_festiwali = tk.Listbox(
    ramka_lista_festiwali,
    width=42,
    height=8,
    font=("Arial", 10)
)

listbox_lista_festiwali.pack()

gui_data.listbox_lista_festiwali = listbox_lista_festiwali


button_odswiez = tk.Button(
    ramka_lista_festiwali,
    text="⟳ Odśwież listę",
    width=32,
    bg=blue,
    fg="white",
    font=button_font,
    relief="flat",
    command=refresh_festival_list
)

button_odswiez.pack(
    pady=3,
    ipady=2
)


button_usun = tk.Button(
    ramka_lista_festiwali,
    text="🗑 Usuń festiwal",
    width=32,
    bg=red,
    fg="white",
    font=button_font,
    relief="flat",
    command=delete_festival_gui
)

button_usun.pack(
    pady=3,
    ipady=2
)


button_mapa = tk.Button(
    ramka_lista_festiwali,
    text="📍 Otwórz mapę",
    width=32,
    bg=green,
    fg="white",
    font=button_font,
    relief="flat",
    command=show_map
)

button_mapa.pack(
    pady=3,
    ipady=2
)


# ==================================================
# 🔵 KINA
# ==================================================

ramka_kina = tk.LabelFrame(
    ramka_lewa,
    text="Zarządzanie kinami",
    padx=8,
    pady=8,
    font=("Arial", 11, "bold")
)

ramka_kina.pack(
    pady=5
)


listbox_lista_kin = tk.Listbox(
    ramka_kina,
    width=42,
    height=5,
    font=("Arial", 10)
)

listbox_lista_kin.pack()

gui_data.listbox_lista_kin = listbox_lista_kin


button_odswiez_kina = tk.Button(
    ramka_kina,
    text="⟳ Odśwież kina",
    width=32,
    bg=blue,
    fg="white",
    font=button_font,
    relief="flat",
    command=refresh_location_list
)

button_odswiez_kina.pack(
    pady=3,
    ipady=2
)


button_usun_kino = tk.Button(
    ramka_kina,
    text="🗑 Usuń kino",
    width=32,
    bg=orange,
    fg="white",
    font=button_font,
    relief="flat",
    command=delete_location_gui
)

button_usun_kino.pack(
    pady=3,
    ipady=2
)


# ==================================================
# 🔵 PRACOWNICY
# ==================================================

ramka_pracownicy = tk.LabelFrame(
    ramka_lewa,
    text="Zarządzanie pracownikami",
    padx=8,
    pady=8,
    font=("Arial", 11, "bold")
)

ramka_pracownicy.pack(
    pady=5
)


listbox_pracownicy = tk.Listbox(
    ramka_pracownicy,
    width=42,
    height=5,
    font=("Arial", 10)
)

listbox_pracownicy.pack()

gui_data.listbox_pracownicy = listbox_pracownicy


button_odswiez_pracownikow = tk.Button(
    ramka_pracownicy,
    text="⟳ Odśwież pracowników",
    width=32,
    bg=blue,
    fg="white",
    font=button_font,
    relief="flat",
    command=refresh_employee_list
)

button_odswiez_pracownikow.pack(
    pady=3,
    ipady=2
)


button_dodaj_pracownika = tk.Button(
    ramka_pracownicy,
    text="➕ Dodaj pracownika",
    width=32,
    bg=green,
    fg="white",
    font=button_font,
    relief="flat",
    command=add_employee_gui
)

button_dodaj_pracownika.pack(
    pady=3,
    ipady=2
)


button_usun_pracownika = tk.Button(
    ramka_pracownicy,
    text="🗑 Usuń pracownika",
    width=32,
    bg=orange,
    fg="white",
    font=button_font,
    relief="flat",
    command=delete_employee_gui
)

button_usun_pracownika.pack(
    pady=3,
    ipady=2
)


# ==================================================
# 🔵 ŚRODKOWA KOLUMNA
# ==================================================

ramka_srodek = tk.Frame(okno)

ramka_srodek.grid(
    row=0,
    column=1,
    padx=10,
    pady=10,
    sticky="n"
)


# ==================================================
# 🔵 DODAJ FESTIWAL
# ==================================================

ramka_dodaj = tk.LabelFrame(
    ramka_srodek,
    text="Dodaj festiwal",
    padx=12,
    pady=12,
    font=("Arial", 11, "bold")
)

ramka_dodaj.pack(
    pady=5
)


tk.Label(
    ramka_dodaj,
    text="Nazwa festiwalu:"
).grid(row=0, column=0, sticky="w")

entry_nazwa = tk.Entry(
    ramka_dodaj,
    width=30
)

entry_nazwa.grid(
    row=1,
    column=0,
    padx=5,
    pady=3
)

gui_data.entry_nazwa = entry_nazwa


tk.Label(
    ramka_dodaj,
    text="Miasto:"
).grid(row=2, column=0, sticky="w")

entry_miasto = tk.Entry(
    ramka_dodaj,
    width=30
)

entry_miasto.grid(
    row=3,
    column=0,
    padx=5,
    pady=3
)

gui_data.entry_miasto = entry_miasto


tk.Label(
    ramka_dodaj,
    text="Szerokość geograficzna:"
).grid(row=4, column=0, sticky="w")

entry_szerokosc = tk.Entry(
    ramka_dodaj,
    width=30
)

entry_szerokosc.grid(
    row=5,
    column=0,
    padx=5,
    pady=3
)

gui_data.entry_szerokosc = entry_szerokosc


tk.Label(
    ramka_dodaj,
    text="Długość geograficzna:"
).grid(row=6, column=0, sticky="w")

entry_dlugosc = tk.Entry(
    ramka_dodaj,
    width=30
)

entry_dlugosc.grid(
    row=7,
    column=0,
    padx=5,
    pady=3
)

gui_data.entry_dlugosc = entry_dlugosc


button_dodaj = tk.Button(
    ramka_dodaj,
    text="➕ Dodaj festiwal",
    width=30,
    bg=green,
    fg="white",
    font=button_font,
    relief="flat",
    command=add_festival_gui
)

button_dodaj.grid(
    row=8,
    column=0,
    pady=8,
    ipady=2
)


# ==================================================
# 🔵 UPDATE FESTIWAL
# ==================================================

ramka_update = tk.LabelFrame(
    ramka_srodek,
    text="Aktualizacja festiwalu",
    padx=12,
    pady=12,
    font=("Arial", 11, "bold")
)

ramka_update.pack(
    pady=5
)


entry_id_update = tk.Entry(
    ramka_update,
    width=30
)

entry_id_update.grid(
    row=0,
    column=0,
    padx=5,
    pady=3
)

gui_data.entry_id_update = entry_id_update


entry_nazwa_update = tk.Entry(
    ramka_update,
    width=30
)

entry_nazwa_update.grid(
    row=1,
    column=0,
    padx=5,
    pady=3
)

gui_data.entry_nazwa_update = entry_nazwa_update


entry_miasto_update = tk.Entry(
    ramka_update,
    width=30
)

entry_miasto_update.grid(
    row=2,
    column=0,
    padx=5,
    pady=3
)

gui_data.entry_miasto_update = entry_miasto_update


entry_szerokosc_update = tk.Entry(
    ramka_update,
    width=30
)

entry_szerokosc_update.grid(
    row=3,
    column=0,
    padx=5,
    pady=3
)

gui_data.entry_szerokosc_update = entry_szerokosc_update


entry_dlugosc_update = tk.Entry(
    ramka_update,
    width=30
)

entry_dlugosc_update.grid(
    row=4,
    column=0,
    padx=5,
    pady=3
)

gui_data.entry_dlugosc_update = entry_dlugosc_update


button_update = tk.Button(
    ramka_update,
    text="✏ Aktualizuj festiwal",
    width=30,
    bg=blue,
    fg="white",
    font=button_font,
    relief="flat",
    command=update_festival_gui
)

button_update.grid(
    row=5,
    column=0,
    pady=8,
    ipady=2
)


# ==================================================
# 🔵 DODAJ PRACOWNIKA
# ==================================================

ramka_dodaj_pracownika = tk.LabelFrame(
    ramka_srodek,
    text="Dodaj pracownika",
    padx=12,
    pady=12,
    font=("Arial", 11, "bold")
)

ramka_dodaj_pracownika.pack(
    pady=5
)


entry_imie_pracownika = tk.Entry(
    ramka_dodaj_pracownika,
    width=30
)

entry_imie_pracownika.grid(
    row=0,
    column=0,
    padx=5,
    pady=3
)

gui_data.entry_imie_pracownika = entry_imie_pracownika


entry_rola_pracownika = tk.Entry(
    ramka_dodaj_pracownika,
    width=30
)

entry_rola_pracownika.grid(
    row=1,
    column=0,
    padx=5,
    pady=3
)

gui_data.entry_rola_pracownika = entry_rola_pracownika


entry_szerokosc_pracownika = tk.Entry(
    ramka_dodaj_pracownika,
    width=30
)

entry_szerokosc_pracownika.grid(
    row=2,
    column=0,
    padx=5,
    pady=3
)

gui_data.entry_szerokosc_pracownika = entry_szerokosc_pracownika


entry_dlugosc_pracownika = tk.Entry(
    ramka_dodaj_pracownika,
    width=30
)

entry_dlugosc_pracownika.grid(
    row=3,
    column=0,
    padx=5,
    pady=3
)

gui_data.entry_dlugosc_pracownika = entry_dlugosc_pracownika


entry_location_id_pracownika = tk.Entry(
    ramka_dodaj_pracownika,
    width=30
)

entry_location_id_pracownika.grid(
    row=4,
    column=0,
    padx=5,
    pady=3
)

gui_data.entry_location_id_pracownika = entry_location_id_pracownika


# ==================================================
# 🔵 PRAWA KOLUMNA
# ==================================================

ramka_prawa = tk.Frame(okno)

ramka_prawa.grid(
    row=0,
    column=2,
    padx=10,
    pady=10,
    sticky="n"
)


ramka_szczegoly = tk.LabelFrame(
    ramka_prawa,
    text="Szczegóły festiwalu",
    padx=12,
    pady=12,
    font=("Arial", 11, "bold")
)

ramka_szczegoly.pack(
    pady=5
)


label_szczegoly = tk.Label(
    ramka_szczegoly,
    text="Wybierz festiwal z listy",
    justify="left",
    font=("Arial", 10)
)

label_szczegoly.pack()

gui_data.label_szczegoly = label_szczegoly


# ==================================================
# 🔵 MAPA
# ==================================================

ramka_mapa = tk.LabelFrame(
    ramka_prawa,
    text="Mapa festiwali",
    padx=10,
    pady=10,
    font=("Arial", 11, "bold")
)

ramka_mapa.pack(
    pady=10
)


canvas_mapa = tk.Canvas(
    ramka_mapa,
    width=350,
    height=250,
    bg="#d9d9d9"
)

canvas_mapa.pack()


button_mapa_duza = tk.Button(
    ramka_mapa,
    text="📍 Otwórz interaktywną mapę",
    width=35,
    bg=green,
    fg="white",
    font=button_font,
    relief="flat",
    command=show_map
)

button_mapa_duza.pack(
    pady=10,
    ipady=2
)


# ==================================================
# 🔵 STATUS SYSTEMU
# ==================================================

ramka_status = tk.LabelFrame(
    ramka_prawa,
    text="Status systemu",
    padx=10,
    pady=10,
    font=("Arial", 11, "bold")
)

ramka_status.pack(
    pady=10,
    fill="x"
)


label_status = tk.Label(
    ramka_status,
    text="Ładowanie danych...",
    justify="left",
    font=("Arial", 10)
)

label_status.pack(
    anchor="w"
)

gui_data.label_status = label_status


# ==================================================
# 🔵 START
# ==================================================

refresh_festival_list()

refresh_location_list()

refresh_employee_list()

refresh_system_status()

listbox_lista_festiwali.bind(
    "<<ListboxSelect>>",
    load_selected_festival
)

okno.mainloop()