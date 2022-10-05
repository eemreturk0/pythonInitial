from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine


Base = declarative_base()


association_table = Table(
    "lesson_teacher",
    Base.metadata,
    Column("id_lesson", ForeignKey("lesson.id"),primary_key=True),
    Column("id_teacher", ForeignKey("teacher.id"),primary_key=True),
    #teacher = relationship("teacher", back_populates="lessons")
    #lesson = relationship("lesson", back_populates="teachers")
)


class Lesson(Base):
    __tablename__ = "lesson"
    id = Column(Integer, primary_key=True)
    teachers = relationship("teacher", secondary=association_table, back_populates="lessons")
    children = relationship("room")
    id_room = Column(Integer, ForeignKey("room.id"))

class Room(Base):
    __tablename__ = "room"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("lesson.id"))


class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True)
    lessons= relationship("lesson", secondary=association_table, back_populates="teachers")



# sqlite olarak kayıtedilecek dosyayı gösteriyoruz
enginex = create_engine('sqlite:///school_system.db')

# Tanımladığımız Base üzerindeki tabloları oluşturuyoruz
Base.metadata.create_all(enginex)