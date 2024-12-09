"""Connection"""

import os
from dotenv import load_dotenv
from rich.console import Console
from sqlalchemy import Engine, text, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import (
    database_exists as db_exist,
    create_database as create_db,
)

csl: Console = Console()
load_dotenv(override=True)

db_name: str = "bank"
db_url: str = (
    f"postgresql+psycopg://{os.getenv('USER')}:"
    f"{os.getenv('PASSWORD')}@{os.getenv('HOST')}:"
    f"{os.getenv('PORT')}/{db_name}"
)

engine: Engine = create_engine(db_url)


def db_check() -> tuple:
    """Vypis info o databázi"""
    Session = sessionmaker(bind=engine)
    session = Session()
    with session.connection() as conn:
        verze = conn.execute(text("SELECT version();")).fetchone()
        databaze = conn.execute(
            text("SELECT current_database();")
        ).fetchone()

    verze_info: str = verze[0] if verze else "Není dostupná verze."
    name_db: str = (
        databaze[0] if databaze else "Není dostupná databáze."
    )

    return verze_info, name_db


def create_database(name: str) -> None:
    """Creating database"""
    csl.clear()

    if not db_exist(engine.url):
        csl.log(
            f"Vytvarim DB: {name}",
            style="red bold",
        )
        create_db(engine.url, encoding="utf-8")
        csl.log("databaze vytvorena", style="blue")
        verze, databaze = db_check()
        csl.log(f"verze DB: {verze}")
        csl.log(f"jmeno DB: {databaze}")
    else:
        csl.log("Databaze jiz existuje", style="blue")
        verze, databaze = db_check()
        csl.log(f"verze DB: {verze}")
        csl.log(f"jmeno DB: {databaze}")


if __name__ == "__main__":
    create_database(db_name)
