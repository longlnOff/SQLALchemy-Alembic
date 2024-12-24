import sqlalchemy
import sqlalchemy.dialects
import sqlalchemy.dialects.postgresql
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

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

    created_at: Mapped[str] = mapped_column(
        sqlalchemy.dialects.postgresql.TIMESTAMP,
        nullable=False,
        default=sqlalchemy.func.now()
    )

    referrer_id: Mapped[int | None] = mapped_column(
        sqlalchemy.BIGINT,
        sqlalchemy.ForeignKey("users.telegram_id", ondelete="SET NULL"),
        nullable=True
    )