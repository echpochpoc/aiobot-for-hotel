
import db.my_db
from db.models import Post


def test_add_post():
    session = db.my_db.db_session()
    c1 = Post(
    title='Уборшик',
    description='Убирается, а что он еще должен делать?',
    )
    session.add(c1)
    session.commit()

def ddd():
    print('хуй')
