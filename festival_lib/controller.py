from festival_lib.db import Session, engine
from festival_lib.model import Base, Festival

from festival_lib import gui_data

import tkinter as tk

import folium
import webbrowser


# ==================================================
# 🔵 BAZA DANYCH
# ==================================================

def create_db():

    Base.metadata.create_all(engine)


# ==================================================
# 🔵 DANE STARTOWE
# ==================================================

def add_test_data():

    session = Session()

    festivals = session.query(Festival).all()

    if len(festivals) == 0:

        fest1 = Festival(
            name="Warszawski Festiwal Filmowy",
            city="Warszawa",
            latitude=52.23,
            longitude=21.01
        )

        fest2 = Festival(
            name="Krakowski Festiwal Filmowy",
            city="Kraków",
            latitude=50.06,
            longitude=19.94
        )

        session.add_all([fest1, fest2])

        session.commit()

    session.close()


# ==================================================
# 🔵 ODCZYT FESTIWALI
# ==================================================

def read_festival_data():

    session = Session()

    festivals = session.query(Festival).all()

    session.close()

    return festivals


# ==================================================
# 🔵 DODAWANIE FESTIWALU
# ==================================================

def add_festival(name, city, latitude, longitude):

    session = Session()

    festival = Festival(
        name=name,
        city=city,
        latitude=latitude,
        longitude=longitude
    )

    session.add(festival)

    session.commit()

    session.close()


# ==================================================
# 🔵 USUWANIE FESTIWALU
# ==================================================

def delete_festival(festival_id):

    session = Session()

    festival = session.query(Festival).filter(
        Festival.id == festival_id
    ).first()

    if festival:

        session.delete(festival)

        session.commit()

    session.close()


# ==================================================
# 🔵 AKTUALIZACJA FESTIWALU
# ==================================================

def update_festival(
        festival_id,
        name,
        city,
        latitude,
        longitude
):

    session = Session()

    festival = session.query(Festival).filter(
        Festival.id == festival_id
    ).first()

    if festival:

        festival.name = name

        festival.city = city

        festival.latitude = latitude

        festival.longitude = longitude

        session.commit()

    session.close()


# ==================================================
# 🔵 ODŚWIEŻANIE LISTY
# ==================================================

def refresh_festival_list():

    gui_data.listbox_lista_festiwali.delete(
        0,
        tk.END
    )

    festivals = read_festival_data()

    for festival in festivals:

        gui_data.listbox_lista_festiwali.insert(
            tk.END,
            f"{festival.id} | {festival.name} | {festival.city}"
        )


# ==================================================
# 🔵 DODAWANIE FESTIWALU GUI
# ==================================================

def add_festival_gui():

    name = gui_data.entry_nazwa.get()

    city = gui_data.entry_miasto.get()

    latitude = float(
        gui_data.entry_szerokosc.get()
    )

    longitude = float(
        gui_data.entry_dlugosc.get()
    )

    add_festival(
        name,
        city,
        latitude,
        longitude
    )

    refresh_festival_list()


# ==================================================
# 🔵 USUWANIE FESTIWALU GUI
# ==================================================

def delete_festival_gui():

    selected = gui_data.listbox_lista_festiwali.curselection()

    if selected:

        festival_text = gui_data.listbox_lista_festiwali.get(selected)

        festival_id = int(
            festival_text.split("|")[0]
        )

        delete_festival(festival_id)

        refresh_festival_list()


# ==================================================
# 🔵 AKTUALIZACJA FESTIWALU GUI
# ==================================================

def update_festival_gui():

    festival_id = int(
        gui_data.entry_id_update.get()
    )

    name = gui_data.entry_nazwa_update.get()

    city = gui_data.entry_miasto_update.get()

    latitude = float(
        gui_data.entry_szerokosc_update.get()
    )

    longitude = float(
        gui_data.entry_dlugosc_update.get()
    )

    update_festival(
        festival_id,
        name,
        city,
        latitude,
        longitude
    )

    refresh_festival_list()


# ==================================================
# 🔵 ŁADOWANIE FESTIWALU
# ==================================================

def load_selected_festival(event):

    selected = gui_data.listbox_lista_festiwali.curselection()

    if selected:

        festival_text = gui_data.listbox_lista_festiwali.get(selected)

        festival_id = int(
            festival_text.split("|")[0]
        )

        festivals = read_festival_data()

        for festival in festivals:

            if festival.id == festival_id:

                gui_data.entry_id_update.delete(0, tk.END)
                gui_data.entry_id_update.insert(0, festival.id)

                gui_data.entry_nazwa_update.delete(0, tk.END)
                gui_data.entry_nazwa_update.insert(0, festival.name)

                gui_data.entry_miasto_update.delete(0, tk.END)
                gui_data.entry_miasto_update.insert(0, festival.city)

                gui_data.entry_szerokosc_update.delete(0, tk.END)
                gui_data.entry_szerokosc_update.insert(
                    0,
                    festival.latitude
                )

                gui_data.entry_dlugosc_update.delete(0, tk.END)
                gui_data.entry_dlugosc_update.insert(
                    0,
                    festival.longitude
                )

                gui_data.label_szczegoly.config(
                    text=
                    f"ID: {festival.id}\n"
                    f"Nazwa: {festival.name}\n"
                    f"Miasto: {festival.city}\n"
                    f"Szerokość: {festival.latitude}\n"
                    f"Długość: {festival.longitude}"
                )


# ==================================================
# 🔵 MAPA
# ==================================================

def show_map():

    session = Session()

    festivals = session.query(Festival).all()

    mapa = folium.Map(
        location=[52.0, 19.0],
        zoom_start=6
    )

    for festival in festivals:

        folium.Marker(
            location=[
                festival.latitude,
                festival.longitude
            ],

            popup=f"{festival.name} ({festival.city})",

            icon=folium.Icon(color="red")

        ).add_to(mapa)

    mapa.save("mapa.html")

    webbrowser.open("mapa.html")

    session.close()