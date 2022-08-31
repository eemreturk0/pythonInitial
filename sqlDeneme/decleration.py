from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Ogretmen(Base):
    __tablename__ = 'ogretmen'

    id = Column(Integer, primary_key=True)
    isim = Column(String(250), nullable=False)

class Ders(Base):
    __tablename__ = 'ders'

    id = Column(Integer, primary_key=True)
    isim = Column(String(250), nullable=False)
    ogretmen_id = Column(Integer, ForeignKey('ogretmen.id'))
    ogretmen = relationship(Ogretmen, backref='ders')


# sqlite olarak kayıtedilecek dosyayı gösteriyoruz
engine = create_engine('sqlite:///okul_sistemi.db')

# Tanımladığımız Base üzerindeki tabloları oluşturuyoruz
Base.metadata.create_all(engine)