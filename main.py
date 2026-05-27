import tkinter as tk

from festival_lib.controller import *


# 🔵 baza danych

create_db()

add_test_data()


# 🔵 okno

okno = tk.Tk()

okno.title("Film Festival System")

okno.geometry("1500x950")


# ==================================================
# 🔵 LEWA STRONA
# ==================================================

ramka_lewa = tk.Frame(okno)

ramka_lewa.pack(
    side="left",
    padx=15,
    pady=15
)


# 🔵 lista festiwali

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


# 🔵 buttony lista

ramka_buttony_lista = tk.Frame(ramka_lewa)

ramka_buttony_lista.pack(pady=10)


button_odswiez = tk.Button(
    ramka_buttony_lista,
    text="Odśwież listę",
    width=20
)

button_odswiez.grid(
    row=0,
    column=0,
    padx=5
)


button_wyczysc = tk.Button(
    ramka_buttony_lista,
    text="Wyczyść pola",
    width=20
)

button_wyczysc.grid(
    row=0,
    column=1,
    padx=5
)


# 🔵 operacje festiwal

ramka_operacje = tk.LabelFrame(
    ramka_lewa,
    text="Operacje na festiwalu",
    padx=10,
    pady=10
)

ramka_operacje.pack(
    pady=10,
    fill="x"
)


button_usun = tk.Button(
    ramka_operacje,
    text="Usuń festiwal",
    width=30
)

button_usun.pack(pady=5)


button_edytuj = tk.Button(
    ramka_operacje,
    text="Edytuj festiwal",
    width=30
)

button_edytuj.pack(pady=5)


button_szczegoly = tk.Button(
    ramka_operacje,
    text="Pokaż szczegóły",
    width=30
)

button_szczegoly.pack(pady=5)


# 🔵 mapa

button_mapa = tk.Button(
    ramka_lewa,
    text="Otwórz mapę festiwali",
    width=40,
    height=2
)

button_mapa.pack(pady=15)


# ==================================================
# 🔵 ŚRODEK
# ==================================================

ramka_srodek = tk.Frame(okno)

ramka_srodek.pack(
    side="left",
    padx=15,
    pady=15
)


# 🔵 dodawanie

ramka_dodaj = tk.LabelFrame(
    ramka_srodek,
    text="Dodaj festiwal",
    padx=15,
    pady=15
)

ramka_dodaj.pack()


# 🔵 nazwa

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


# 🔵 miasto

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


# 🔵 szerokość

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


# 🔵 długość

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


# 🔵 button dodaj

button_dodaj = tk.Button(
    ramka_dodaj,
    text="Dodaj festiwal",
    width=30
)

button_dodaj.pack(pady=15)


# 🔵 aktualizacja

ramka_update = tk.LabelFrame(
    ramka_srodek,
    text="Aktualizacja festiwalu",
    padx=15,
    pady=15
)

ramka_update.pack(
    pady=15
)


entry_id_update = tk.Entry(
    ramka_update,
    width=40
)

entry_id_update.pack(pady=5)


entry_nazwa_update = tk.Entry(
    ramka_update,
    width=40
)

entry_nazwa_update.pack(pady=5)


entry_miasto_update = tk.Entry(
    ramka_update,
    width=40
)

entry_miasto_update.pack(pady=5)


entry_szerokosc_update = tk.Entry(
    ramka_update,
    width=40
)

entry_szerokosc_update.pack(pady=5)


entry_dlugosc_update = tk.Entry(
    ramka_update,
    width=40
)

entry_dlugosc_update.pack(pady=5)


button_update = tk.Button(
    ramka_update,
    text="Zaktualizuj festiwal",
    width=30
)

button_update.pack(pady=15)


# ==================================================
# 🔵 PRAWA STRONA
# ==================================================

ramka_prawa = tk.Frame(okno)

ramka_prawa.pack(
    side="left",
    padx=15,
    pady=15
)


# 🔵 szczegóły

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

label_szczegoly.pack(anchor="w")


# 🔵 kina

ramka_kina = tk.LabelFrame(
    ramka_prawa,
    text="Lokalizacje festiwalu",
    padx=10,
    pady=10
)

ramka_kina.pack(
    pady=10
)


listbox_kina = tk.Listbox(
    ramka_kina,
    width=50,
    height=8
)

listbox_kina.grid(
    row=0,
    column=0,
    rowspan=3
)


button_dodaj_kino = tk.Button(
    ramka_kina,
    text="Dodaj lokalizację",
    width=20
)

button_dodaj_kino.grid(
    row=0,
    column=1,
    padx=10,
    pady=5
)


button_edytuj_kino = tk.Button(
    ramka_kina,
    text="Edytuj lokalizację",
    width=20
)

button_edytuj_kino.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)


button_usun_kino = tk.Button(
    ramka_kina,
    text="Usuń lokalizację",
    width=20
)

button_usun_kino.grid(
    row=2,
    column=1,
    padx=10,
    pady=5
)


# 🔵 pracownicy

ramka_pracownicy = tk.LabelFrame(
    ramka_prawa,
    text="Pracownicy lokalizacji",
    padx=10,
    pady=10
)

ramka_pracownicy.pack(
    pady=10
)


listbox_pracownicy = tk.Listbox(
    ramka_pracownicy,
    width=50,
    height=8
)

listbox_pracownicy.grid(
    row=0,
    column=0,
    rowspan=3
)


button_dodaj_pracownika = tk.Button(
    ramka_pracownicy,
    text="Dodaj pracownika",
    width=20
)

button_dodaj_pracownika.grid(
    row=0,
    column=1,
    padx=10,
    pady=5
)


button_edytuj_pracownika = tk.Button(
    ramka_pracownicy,
    text="Edytuj pracownika",
    width=20
)

button_edytuj_pracownika.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)


button_usun_pracownika = tk.Button(
    ramka_pracownicy,
    text="Usuń pracownika",
    width=20
)

button_usun_pracownika.grid(
    row=2,
    column=1,
    padx=10,
    pady=5
)


# 🔵 filmy

ramka_filmy = tk.LabelFrame(
    ramka_prawa,
    text="Filmy festiwalu",
    padx=10,
    pady=10
)

ramka_filmy.pack(
    pady=10
)


listbox_filmy = tk.Listbox(
    ramka_filmy,
    width=50,
    height=8
)

listbox_filmy.grid(
    row=0,
    column=0,
    rowspan=3
)


button_dodaj_film = tk.Button(
    ramka_filmy,
    text="Dodaj film",
    width=20
)

button_dodaj_film.grid(
    row=0,
    column=1,
    padx=10,
    pady=5
)


button_edytuj_film = tk.Button(
    ramka_filmy,
    text="Edytuj film",
    width=20
)

button_edytuj_film.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)


button_usun_film = tk.Button(
    ramka_filmy,
    text="Usuń film",
    width=20
)

button_usun_film.grid(
    row=2,
    column=1,
    padx=10,
    pady=5
)


# ==================================================
# 🔵 ODŚWIEŻANIE LISTY
# ==================================================

def refresh_festival_list():

    listbox_lista_festiwali.delete(
        0,
        tk.END
    )

    festivals = read_festival_data()

    for festival in festivals:

        listbox_lista_festiwali.insert(
            tk.END,
            f"{festival.id} | {festival.name} | {festival.city}"
        )


# ==================================================
# 🔵 BUTTONY
# ==================================================

button_odswiez.config(
    command=refresh_festival_list
)

button_mapa.config(
    command=show_map
)


# ==================================================
# 🔵 START
# ==================================================

refresh_festival_list()

okno.mainloop()