from ast import For
from numpy import integer
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import VARCHAR, Column, Integer
from sqlalchemy.sql.schema import ForeignKey


class Admin_user(Base):
    __tablename__ = 'user_table'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    role_id = Column(Integer, ForeignKey(
        "role.id", ondelete="CASCADE"), nullable=False)
    username = Column(VARCHAR(50), unique=True, nullable=False)
    email = Column(VARCHAR(50), nullable=False)
    password = Column(VARCHAR(100), nullable=False, unique=True)
    adress = Column(VARCHAR(50), nullable=False)

    owner = relationship("Admin_role")


class Admin_role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True, autoincrement=True)
    permission_id = Column(Integer, ForeignKey(
        "permission.id", ondelete="CASCADE"), nullable=False)
    employee = Column(VARCHAR(50), nullable=False)
    supplier = Column(VARCHAR(50), nullable=True, unique=True)

    owner = relationship("Admin_permission")


class Admin_permission(Base):
    __tablename__ = "permission"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    permission_status = Column(VARCHAR(50), nullable=False)
    auth = Column(VARCHAR(50), nullable=False)


class Customer_customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(Integer, ForeignKey(
        "user_table.id", ondelete="CASCADE"), nullable=False)
    category_id = Column(Integer, ForeignKey(
        "category.id", ondelete="CASCADE"), nullable=False)
    member_lvl = Column(VARCHAR(50), nullable=True)
    history = Column(VARCHAR(100), nullable=True)
    chatt = Column(VARCHAR, nullable=True)

    owner = relationship("Admin_user")
    owner = relationship("Customer_category")


class Customer_customer_service(Base):
    __tablename__ = "customer_service"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(Integer, ForeignKey(
        "user_table.id", ondelete="CASCADE"), nullable=False)
    customer_id = Column(Integer, ForeignKey(
        "customer.id", ondelete="CASCADE"), nullable=False)
    message = Column(VARCHAR(100), nullable=True)

    owner = relationship("Admin_user")
    owner = relationship("Customer_customer")


class Customer_memberBenefits(Base):
    __tablename__ = "member_benefits"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    event_id = Column(Integer, ForeignKey(
        "event.id", ondelete="CASCADE"), nullable=True)
    customer_id = Column(Integer, ForeignKey(
        "customer.id", ondelete="CASCADE"), nullable=False)
    bonus_ladder = Column(Integer, nullable=True)
    Offer = Column(VARCHAR(100), nullable=True)

    owner = relationship("Customer_event")
    owner = relationship("Customer_customer")


class Customer_event(Base):
    __tablename__ = "event"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    customer_id = Column(Integer, ForeignKey(
        "customer.id", ondelete="CASCADE"), nullable=False)
    category_id = Column(Integer, ForeignKey(
        "category.id", ondelete="CASCADE"), nullable=False)
    name = Column(VARCHAR(50), nullable=False)

    owner = relationship("Customer_customer")
    owner = relationship("Customer_category")


class Customer_community(Base):
    __tablename__ = "community"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(Integer, ForeignKey(
        "user_table.id", ondelete="CASCADE"), nullable=False)
    category_id = Column(Integer, ForeignKey(
        "category.id", ondelete="CASCADE"), nullable=False)
    post = Column(VARCHAR(50), nullable=True)
    chatt = Column(VARCHAR(50), nullable=True)

    owner = relationship("Admin_user")
    owner = relationship("Customer_category")


class Customer_category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    customer_id = Column(Integer, ForeignKey(
        "customer.id", ondelete="CASCADE"), nullable=False)
    prefered_animal = Column(VARCHAR(50), nullable=False)

    owner = relationship("Customer_customer")
