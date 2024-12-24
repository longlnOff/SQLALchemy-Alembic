import sqlalchemy
import sqlalchemy.dialects
import sqlalchemy.dialects.postgresql
from sqlalchemy.orm import (
                            DeclarativeBase, 
                            Mapped, 
                            mapped_column,
                            declared_attr
                        )
from typing_extensions import Annotated


class TimestampMixin:
    created_at: Mapped[str] = mapped_column(
        sqlalchemy.dialects.postgresql.TIMESTAMP,
        nullable=False,
        default=sqlalchemy.func.now()
    )

    updated_at: Mapped[str] = mapped_column(
        sqlalchemy.dialects.postgresql.TIMESTAMP,
        nullable=False,
        default=sqlalchemy.func.now(),
        onupdate=sqlalchemy.func.now()
    )

class TablenameMixin:
    @declared_attr.diretive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"


class Base(DeclarativeBase):
    pass


class User(Base, TimestampMixin, TablenameMixin):

    telegram_id: Mapped[int] = mapped_column(
        sqlalchemy.BIGINT,
        primary_key=True
    )

    full_name: Mapped[str] = mapped_column(
        sqlalchemy.VARCHAR(255),
    )

    username: Mapped[str | None] = mapped_column(
        sqlalchemy.VARCHAR(255),
        nullable=True
    )

    language_code: Mapped[str] = mapped_column(
        sqlalchemy.VARCHAR(10),
        nullable=False
    )

    referrer_id: Mapped[int | None] = mapped_column(
        sqlalchemy.BIGINT,
        sqlalchemy.ForeignKey("users.telegram_id", ondelete="SET NULL"),
        nullable=True
    )


int_pk = Annotated[int, mapped_column(sqlalchemy.Integer, primary_key=True)]

user_fk = Annotated[
    int, 
    mapped_column(sqlalchemy.Integer, 
                  sqlalchemy.ForeignKey("users.telegram_id", ondelete="SET NULL"),)
]

str_255 = Annotated[str, mapped_column(sqlalchemy.VARCHAR(255))]


class User2(Base, TimestampMixin, TablenameMixin):
    telegram_id: Mapped[int] = mapped_column(
        sqlalchemy.BIGINT,
        primary_key=True
    )

    full_name: Mapped[str_255]
    username: Mapped[str_255 | None]
    language_code: Mapped[str_255]
    referrer_id: Mapped[user_fk | None]


class Product(Base, TimestampMixin, TablenameMixin):
    product_id: Mapped[int_pk]
    title: Mapped[str_255]
    desceiption: Mapped[str_255 | None]


class Order(Base, TimestampMixin, TablenameMixin):
    order_id: Mapped[int_pk]
    user_id: Mapped[user_fk]


class OrderProduct(Base, TablenameMixin):
    order_id: Mapped[int] = mapped_column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("orders.order_id", ondelete="CASCADE"),
        primary_key=True
    )

    product_id: Mapped[int] = mapped_column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("products.product_id", ondelete="CASCADE"),
        primary_key=True
    )

    quantity: Mapped[int]