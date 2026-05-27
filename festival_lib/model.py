from sqlalchemy import Column, Integer, String, Float, ForeignKey

from festival_lib.db import Base


class Festival(Base):
    __tablename__ = "festival"

    id = Column(Integer, primary_key=True)

    name = Column(String)
    city = Column(String)

    latitude = Column(Float)
    longitude = Column(Float)


class Location(Base):
    __tablename__ = "location"

    id = Column(Integer, primary_key=True)

    name = Column(String)
    city = Column(String)

    latitude = Column(Float)
    longitude = Column(Float)

    festival_id = Column(Integer, ForeignKey("festival.id"))


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)

    name = Column(String)
    role = Column(String)

    latitude = Column(Float)
    longitude = Column(Float)

    location_id = Column(Integer, ForeignKey("location.id"))


class Film(Base):
    __tablename__ = "film"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    festival_id = Column(Integer, ForeignKey("festival.id"))