class BaseEntity:
    id: int
    email: str
    password: str

    def __init__(self, id:int, email:str, password:str):
        self.id = id
        self.email = email
        self.password = password
    
    def __repr__(self):
        return f"BaseEntity(id={self.id}, email={self.email})"


    
