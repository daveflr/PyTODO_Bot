from pony.orm import Database, Required, Optional, Set, PrimaryKey

db = Database()


class Chat(db.Entity):
    id = PrimaryKey(str)
    type = Required(str)
    title = Optional(str, nullable=True)
    username = Optional(str, nullable=True)
    first_name = Optional(str, nullable=True)
    last_name = Optional(str, nullable=True)
    photo = Optional(str, nullable=True)
    description = Optional(str, nullable=True)
    invite_link = Optional(str, nullable=True)
    pinned_message = Optional(str, nullable=True)

    task = Set(lambda: Task)  # A Chat can contain many Task


class Task(db.Entity):
    id = PrimaryKey(int, auto=True)
    task = Required(str)
    chat = Required(Chat)  # A task belongs to a chat
    complete = Required(bool)


db.bind(provider='sqlite', filename='../database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)