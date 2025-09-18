from sqlmodel import create_engine, Session
baseUrl = "sqlite:///miniMarket.db"

engine = create_engine(baseUrl,echo=True)

def get_session():
    with Session(engine) as session:
        yield session
