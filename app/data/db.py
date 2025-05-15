from sqlmodel import create_engine, SQLModel, Session


sqlite_file_name = "app/data/database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args, echo=True)



def init_database():
    SQLModel.metadata.create_all(engine)

