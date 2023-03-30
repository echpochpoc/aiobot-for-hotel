from core.my_bot import session_factory


def add_new_user(user):
    session = session_factory()
    session.add(user)
    session.commit()
