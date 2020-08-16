
from test_platform.tools.login_api import db, User

def test_add_user():
    admin = User(username='admin', email='admin@example.com',password='123456')
    guest = User(username='guest', email='guest@example.com',password='123456')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()



