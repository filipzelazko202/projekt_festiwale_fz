import tkinter as tk
import webbrowser

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import folium

from festival_lib.db import Base
from festival_lib.model import Festival, Location, Employee
from festival_lib import gui_data


engine = create_engine(
    "sqlite:///film_festival.db"
)

Session = sessionmaker(
    bind=engine
)


# ==================================================
# DB
# ==================================================

def create_db():

    Base.metadata.create_all(engine)


# ==================================================
# TEST DATA
# ==================================================

def add_test_data():

    session = Session()

    if session.query(Festival).count() == 0:

        festival_1 = Festival(
            name="Warszawski Festiwal Filmowy",
            city="Warszawa",
            latitude=52.2297,
            longitude=21.0122
        )

        festival_2 = Festival(
            name="Krakowski Festiwal Filmowy",
            city="Kraków",
            latitude=50.0647,
            longitude=19.9450
        )

        session.add_all([
            festival_1,
            festival_2
        ])

        session.commit()

    if session.query(Location).count() == 0:

        location_1 = Location(
            name="Kino Luna",
            city="Warszawa",
            latitude=52.22,
            longitude=21.00,
            festival_id=1
        )

        location_2 = Location(
            name="Kino Pod Baranami",
            city="Kraków",
            latitude=50.06,
            longitude=19.93,
            festival_id=2
        )

        session.add_all([
            location_1,
            location_2
        ])

        session.commit()

    if session.query(Employee).count() == 0:

        employee_1 = Employee(
            name="Jan Kowalski",
            role="Koordynator",
            latitude=52.22,
            longitude=21.00,
            location_id=1
        )

        employee_2 = Employee(
            name="Anna Nowak",
            role="Technik",
            latitude=50.06,
            longitude=19.93,
            location_id=2
        )

        session.add_all([
            employee_1,
            employee_2
        ])

        session.commit()

    session.close()


# ==================================================
# FESTIWALE
# ==================================================

def read_festival_data():

    session = Session()

    festivals = session.query(Festival).all()

    session.close()

    return festivals


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


def add_festival_gui():

    session = Session()

    festival = Festival(
        name=gui_data.entry_nazwa.get(),
        city=gui_data.entry_miasto.get(),
        latitude=float(gui_data.entry_szerokosc.get()),
        longitude=float(gui_data.entry_dlugosc.get())
    )

    session.add(festival)

    session.commit()

    session.close()

    refresh_festival_list()

    refresh_system_status()


def delete_festival_gui():

    selected = gui_data.listbox_lista_festiwali.curselection()

    if selected:

        festival_text = gui_data.listbox_lista_festiwali.get(selected)

        festival_id = int(
            festival_text.split("|")[0]
        )

        session = Session()

        festival = session.query(Festival).filter(
            Festival.id == festival_id
        ).first()

        if festival:

            session.delete(festival)

            session.commit()

        session.close()

        refresh_festival_list()

        refresh_system_status()


def update_festival_gui():

    session = Session()

    festival = session.query(Festival).filter(
        Festival.id == int(gui_data.entry_id_update.get())
    ).first()

    if festival:

        festival.name = gui_data.entry_nazwa_update.get()

        festival.city = gui_data.entry_miasto_update.get()

        festival.latitude = float(
            gui_data.entry_szerokosc_update.get()
        )

        festival.longitude = float(
            gui_data.entry_dlugosc_update.get()
        )

        session.commit()

    session.close()

    refresh_festival_list()


def load_selected_festival(event):

    selected = gui_data.listbox_lista_festiwali.curselection()

    if selected:

        festival_text = gui_data.listbox_lista_festiwali.get(selected)

        festival_id = int(
            festival_text.split("|")[0]
        )

        session = Session()

        festival = session.query(Festival).filter(
            Festival.id == festival_id
        ).first()

        session.close()

        gui_data.label_szczegoly.config(
            text=
            f"ID: {festival.id}\n\n"
            f"Nazwa: {festival.name}\n\n"
            f"Miasto: {festival.city}\n\n"
            f"Szerokość: {festival.latitude}\n\n"
            f"Długość: {festival.longitude}"
        )

        gui_data.entry_id_update.delete(0, tk.END)
        gui_data.entry_id_update.insert(0, festival.id)

        gui_data.entry_nazwa_update.delete(0, tk.END)
        gui_data.entry_nazwa_update.insert(0, festival.name)

        gui_data.entry_miasto_update.delete(0, tk.END)
        gui_data.entry_miasto_update.insert(0, festival.city)

        gui_data.entry_szerokosc_update.delete(0, tk.END)
        gui_data.entry_szerokosc_update.insert(0, festival.latitude)

        gui_data.entry_dlugosc_update.delete(0, tk.END)
        gui_data.entry_dlugosc_update.insert(0, festival.longitude)


# ==================================================
# KINA
# ==================================================

def refresh_location_list():

    gui_data.listbox_lista_kin.delete(
        0,
        tk.END
    )

    session = Session()

    locations = session.query(Location).all()

    session.close()

    for location in locations:

        gui_data.listbox_lista_kin.insert(
            tk.END,
            f"{location.id} | {location.name} | {location.city}"
        )


def add_location_gui():

    session = Session()

    location = Location(
        name=gui_data.entry_nazwa_kina.get(),
        city=gui_data.entry_miasto_kina.get(),
        latitude=float(gui_data.entry_szerokosc_kina.get()),
        longitude=float(gui_data.entry_dlugosc_kina.get()),
        festival_id=int(gui_data.entry_festival_id_kina.get())
    )

    session.add(location)

    session.commit()

    session.close()

    refresh_location_list()

    refresh_system_status()


def delete_location_gui():

    selected = gui_data.listbox_lista_kin.curselection()

    if selected:

        location_text = gui_data.listbox_lista_kin.get(selected)

        location_id = int(
            location_text.split("|")[0]
        )

        session = Session()

        location = session.query(Location).filter(
            Location.id == location_id
        ).first()

        if location:

            session.delete(location)

            session.commit()

        session.close()

        refresh_location_list()

        refresh_system_status()


# ==================================================
# PRACOWNICY
# ==================================================

def refresh_employee_list():

    gui_data.listbox_pracownicy.delete(
        0,
        tk.END
    )

    session = Session()

    employees = session.query(Employee).all()

    session.close()

    for employee in employees:

        gui_data.listbox_pracownicy.insert(
            tk.END,
            f"{employee.id} | {employee.name} | {employee.role}"
        )


def add_employee_gui():

    session = Session()

    employee = Employee(
        name=gui_data.entry_imie_pracownika.get(),
        role=gui_data.entry_rola_pracownika.get(),
        latitude=float(gui_data.entry_szerokosc_pracownika.get()),
        longitude=float(gui_data.entry_dlugosc_pracownika.get()),
        location_id=int(gui_data.entry_location_id_pracownika.get())
    )

    session.add(employee)

    session.commit()

    session.close()

    refresh_employee_list()

    refresh_system_status()


def delete_employee_gui():

    selected = gui_data.listbox_pracownicy.curselection()

    if selected:

        employee_text = gui_data.listbox_pracownicy.get(selected)

        employee_id = int(
            employee_text.split("|")[0]
        )

        session = Session()

        employee = session.query(Employee).filter(
            Employee.id == employee_id
        ).first()

        if employee:

            session.delete(employee)

            session.commit()

        session.close()

        refresh_employee_list()

        refresh_system_status()


# ==================================================
# MAPA
# ==================================================

def show_map():

    festivals = read_festival_data()

    mapa = folium.Map(
        location=[52.0, 19.0],
        zoom_start=6
    )

    for festival in festivals:

        folium.Marker(
            [festival.latitude, festival.longitude],
            popup=f"{festival.name} | {festival.city}"
        ).add_to(mapa)

    mapa.save("mapa.html")

    webbrowser.open("mapa.html")


# ==================================================
# STATUS
# ==================================================

def refresh_system_status():

    session = Session()

    festival_count = session.query(Festival).count()

    location_count = session.query(Location).count()

    employee_count = session.query(Employee).count()

    session.close()

    gui_data.label_status.config(
        text=
        f"Liczba festiwali: {festival_count}\n\n"
        f"Liczba kin: {location_count}\n\n"
        f"Liczba pracowników: {employee_count}\n\n"
        f"Status bazy danych: ONLINE"
    )