from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Asegurate de tener instalado el driver pymysql
# pip install pymysql

# URL de conexión MySQL (modificá usuario, password, host, puerto y DB)
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/tvbox_db"

# Crear engine con opciones para pool y ping automático
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
    echo=True  # Opcional: para ver logs SQL
)

# Crear SessionLocal para instanciar sesiones de DB
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Función para usar en FastAPI (dependency)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
