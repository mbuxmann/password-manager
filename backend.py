from sqlalchemy import create_engine, Table, Column, String, MetaData
from sqlalchemy.sql import select


metadata = MetaData()

credentials = Table('credentials', metadata,
                    Column('name', String, primary_key=True),
                    Column('username', String, nullable=False),
                    Column('password', String, nullable=False),
                    )

db = create_engine(f'sqlite:///database.db', echo=False)

metadata.create_all(db)


def add_credential(name, username, password):
    '''Add a credential to the database'''
    ins = credentials.insert().values(
        name=name, username=username, password=password)
    conn = db.connect()
    conn.execute(ins)
    conn.close()


def show_credentials():
    '''Show all credentials from the database'''
    s = select([credentials])
    conn = db.connect()
    result = conn.execute(s)
    return result


def search_credentials(name):
    '''Search the database for a name'''
    s = select([credentials]).where(credentials.c.name.like(f'%{name}%'))
    conn = db.connect()
    result = conn.execute(s)
    return result


def delete_credential(name):
    '''Delete a credential from the database'''
    conn = db.connect()
    conn.execute(credentials.delete().where(credentials.c.name == name))
    conn.close()


def check_existance(name):
    '''Check if a credential already exists with the same name in the database'''
    s = select([credentials]).where(credentials.c.name == name)
    conn = db.connect()
    result = conn.execute(s)
    for row in result:
        if row:
            conn.close()
            return True

    conn.close()
    return False


db.dispose()
