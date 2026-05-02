from app.auth.utils import hash_password, verify_password, create_access_token

fake_db = {}

def register_user(email: str, password: str):
    if email in fake_db:
        raise Exception("User already exists")

    fake_db[email] = hash_password(password)
    return {"message": "User created"}

def login_user(email: str, password: str):
    user = fake_db.get(email)

    if not user or not verify_password(password, user):
        raise Exception("Invalid credentials")

    token = create_access_token({"sub": email})
    return {"access_token": token}