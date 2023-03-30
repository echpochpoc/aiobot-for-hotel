from core.my_bot import session_factory
from db.models import Post


def test_add_post():
    session = session_factory()
    c1 = Post(
    title='Повар',
    description='Готовит, а что еще он должен делать?',
    )
    session.add(c1)
    session.commit()
