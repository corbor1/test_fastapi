from app.db.db import engine
from app.models.models import Base

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)