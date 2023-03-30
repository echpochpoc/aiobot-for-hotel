from core.my_bot import session_factory


def create_new_task(task):
    session = session_factory()
    session.add(task)
    session.commit()
