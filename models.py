from atexit import register

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    create_engine,
    func,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

PG_USER = "app"
PG_PASSWORD = "1234"
PG_DB = "app3"
PG_HOST = "127.0.0.1"
PG_PORT = "5431"
PG_DSN = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

engine = create_engine(PG_DSN)

register(engine.dispose)

Session = sessionmaker(bind=engine)
Base = declarative_base(bind=engine)


class Ad(Base):
    __tablename__ = "app_ad"

    id = Column(Integer, primary_key=True)
    # owner = Column(Integer, ForeignKey("app_user.name", ondelete="CASCADE"))
    owner = Column(String)
    title = Column(String)
    description = Column(String)
    creation_time = Column(DateTime, server_default=func.now())


# class User(Base):
#     __tablename__ = "app_user"
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False, unique=True, index=True)
#     password = Column(String, nullable=False)
#     creation_time = Column(DateTime, server_default=func.now())

Base.metadata.create_all()
