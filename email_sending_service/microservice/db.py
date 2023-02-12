from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from .settings import settings

engine = create_engine(settings.database_uri)
SessionLocal = sessionmaker(engine, expire_on_commit=False)
session = SessionLocal()


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)

    def save(self):
        session.add(self)
        session.commit()

    @classmethod
    def clear_table(cls):
        session.query(cls).delete()
        session.commit()


Base = declarative_base(cls=PreBase)
Base.metadata.create_all(engine)
