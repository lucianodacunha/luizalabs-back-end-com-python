from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    active = Column(Boolean, default=True)

    order = relationship("Order", back_populates="user")

    def __repr__(self):
        return f"<User id={self.id} name={self.name}>"


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    total = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="order")

    def __repr__(self):
        return f"<Order id={self.id} total={self.total}>"


from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent
DB_PATH = ROOT_PATH / "db.sqlite"
engine = create_engine(f"sqlite:///{DB_PATH}")

Base.metadata.create_all(engine)

from sqlalchemy import inspect

insp = inspect(engine)
print(insp.get_table_names())


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# user = User(name="Luciano", email="luciano@email.com")
# session.add(user)
# session.commit()

# user1 = User(name="User 1", email="user1@email.com")
# session.add(user1)
# user2 = User(name="User 2", email="user2@email.com")
# session.add(user2)
# user3 = User(name="User 3", email="user3@email.com", active=False)
# session.add(user3)
# session.commit()

# order1 = Order(total=100.0, user_id=1)
# order2 = Order(total=150.0, user_id=2)
# order3 = Order(total=200.0, user_id=3)
# order4 = Order(total=400.0, user_id=2)
# order5 = Order(total=50.0, user_id=3)
# order6 = Order(total=300.0, user_id=4)
# session.add(order1)
# session.add(order2)
# session.add(order3)
# session.add(order4)
# session.add(order5)
# session.add(order6)
# session.commit()


users = session.query(User).all()
print(users)

users = session.query(User).filter_by(email="luciano@email.com").first()
print(users)

users_actives = session.query(User).filter(User.active == True).all()
print(users_actives)

users = session.query(User).order_by(User.name).all()
print(users)

orders = session.query(Order).join(Order.user).filter(
    User.name == "User 1").all()
print(orders)

from sqlalchemy import func

total_users = session.query(func.count(User.id)).scalar()
print(total_users)