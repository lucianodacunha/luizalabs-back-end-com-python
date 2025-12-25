from __future__ import annotations

from sqlalchemy.orm import Session

from config.base import Base, engine
from models.customer import Customer
from models.order import Order


def create_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

def create_customer(session: Session, name: str, email: str) -> Customer:
    customer = Customer(name=name, email=email)
    session.add(customer)
    session.flush()
    return customer

def create_order(session: Session, customer_id: int, item: str, price: float) -> Order:
    order = Order(customer_id=customer_id, item=item, price=price)
    session.add(order)
    session.flush()
    return order

def main():
    drop_db()
    create_db()

    with Session(engine) as session:
        customer = create_customer(session, "Cliente 1", "cliente1@email.com")
        print(f"Cliente {customer} criado.")

        order1 = create_order(session, customer.id, "Óculos", 500.0)
        order2 = create_order(session, customer.id, "Smartphone", 5000.0)
        order3 = create_order(session, customer.id, "Cafeteira", 200.0)

        print(f"Pedido 1: {order1} criado.")
        print(f"Pedido 2: {order2} criado.")
        print(f"Pedido 3: {order3} criado.")

        session.commit()

        print(f"\nTodos os clientes:")
        customers = session.query(Customer).all()
        print(f"{customers}\n")

        print(f"\nPedidos do Cliente")    
        customer_orders = session.query(Order).filter(Order.customer_id == customer.id).all()
        print(f"{customer.name}: {customer_orders}\n")


if __name__ == "__main__":
    main()
