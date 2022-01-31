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
