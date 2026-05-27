from festival_lib.db import Session, engine
from festival_lib.model import Base, Festival, Location, Employee, Film

import folium
import webbrowser


# 🔵 tworzenie bazy danych

def create_db():

    Base.metadata.create_all(engine)


# 🔵 dane startowe

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


# 🔵 odczyt festiwali

def read_festival_data():

    session = Session()

    festivals = session.query(Festival).all()

    session.close()

    return festivals


# 🔵 dodawanie festiwalu

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


# 🔵 usuwanie festiwalu

def delete_festival(festival_id):

    session = Session()

    festival = session.query(Festival).filter(
        Festival.id == festival_id
    ).first()

    if festival:

        session.delete(festival)

        session.commit()

    session.close()


# 🔵 aktualizacja festiwalu

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


# 🔵 mapa

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