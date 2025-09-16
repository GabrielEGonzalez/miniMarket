from sqlmodel import SQLModel, create_engine , Session

baseUrl = ""

engine = create_engine(baseUrl,echo=True)

def get_session():
    with Session(engine) as session:
        yield session
