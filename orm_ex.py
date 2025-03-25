from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
# from sqlalchemy.ext.declarative import declarative_base

Db_url = "postgresql://postgres:abc123456@localhost:5432/postgres"

# now create engine and session that can connect to database
engine = create_engine(Db_url)
session_l = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base for all models(tables)
Base = declarative_base()

## start tables
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

#Create tables
def init_db():
    Base.metadata.create_all(bind=engine)

## now do CRUD operations
def create_user(db, name, email):
    new_user = User(name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user) ## to refresh the table with new data
    return new_user

def get_user(db, user_id):
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db):
    return db.query(User).all()

def delete_user(db, user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

def conn_close(db):
    db.close()

def get_db_conn():
    init_db()
    db = session_l()
    return db

# # Example Usage
# if __name__ == "__main__":
#     init_db()
#     db = session_l()
#     # user = create_user(db, "John Doe", "john@example.com")
#     print(get_all_users(db))
#     data = get_all_users(db)
#     # for users in data:
#     print([{"id": u.id, "name": u.name, "email": u.email} for u in data])
#     db.close()

