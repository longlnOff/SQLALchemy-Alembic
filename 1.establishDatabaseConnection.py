from sqlalchemy import create_engine, URL, text
from sqlalchemy.orm import sessionmaker

drivername = "postgresql"
user = "testUser"
password = "testpassword"
host = "localhost"
port = 5432
database = "testDB"

# Create connection string
connectionString = URL.create(
    drivername=drivername,
    username=user,
    password=password,
    host=host,
    port=port,
    database=database
)

engine = create_engine(
    url=connectionString,
    echo=True
)

# Create connection pool
session_pool = sessionmaker(engine)

session = session_pool()

# using context to close session automatically
with session_pool() as session:
    session.execute(text("SELECT 1"))
    # session.commit()