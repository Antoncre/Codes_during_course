from admin import Admin
from database import Database
from user import User

a = Admin('rolf', '1234', 3)
u = User('Anton', '4532')

a.save()

