from sqlalchemy import create_engine, Table, Column, String, MetaData
from sqlalchemy.sql import select

metadata = MetaData()

credentials = Table('credentials', metadata,
                    Column('name', String, primary_key=True),
                    Column('username', String, nullable=False),
                    Column('password', String, nullable=False),
                    )

db = create_engine('sqlite:///database.db', echo=False)

metadata.create_all(db)


def add_credential(name, username, password):
    ins = credentials.insert().values(
        name=name, username=username, password=password)
    conn = db.connect()
    conn.execute(ins)
    conn.close()


# add_credential('test', 'test', 'test')
# add_credential('te', 'te', 'te')


def show_credentials():
    s = select([credentials])
    conn = db.connect()
    result = conn.execute(s)
    return result


def search_credentials(name):
    s = select([credentials]).where(credentials.c.name.like(f'%{name}%'))
    conn = db.connect()
    result = conn.execute(s)
    return result


def delete_credential(name):
    conn = db.connect()
    conn.execute(credentials.delete().where(credentials.c.name == name))
    conn.close()


def check_existance(name):
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
