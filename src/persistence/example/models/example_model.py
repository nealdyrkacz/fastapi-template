from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import UUID as saUUID, String

from uuid import UUID, uuid4


Base = declarative_base()

class Example(Base):
    __tablename__ = "example"
    id: Mapped[UUID] = mapped_column(saUUID(as_uuid=True), primary_key=True, insert_default=uuid4)
    name: Mapped[str] = mapped_column(String)