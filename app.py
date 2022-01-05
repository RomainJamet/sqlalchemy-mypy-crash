from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, JSONB, CHAR
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import BLOB, Text
from typing import cast, TYPE_CHECKING
from sqlalchemy.orm import Mapped
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
# run "dmypy start"
# run "dmypy run app.py"
test = 'alter this string and save '
# run "dmypy run app.py"
# daemon crashes


class User(Base):
    __tablename__: str = 'Users'

    id: Mapped[str] = Column(UUID, primary_key=True)
    userName = Column(Text)
    password = Column(Text)
    botId: Mapped[str] = Column(UUID, ForeignKey('Bots.id'), nullable=False)

    def toDict(self):
        return {
            'id': self.id,
            'userName': self.userName,
            'botId': self.botId,
        }
