from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI"
    }

@app.get("/about")
def about():
    return {
        "course": "FastAPI Training",
        "trainer": "John Doe"
    }

@app.get("/contact")
def contact():
    return {
        "email": "trainer@example.com",
        "phone": "9876543210"
    }

@app.get("/courses")
def courses():
    return [
        "Python",
        "FastAPI",
        "React",
        "SQL"
    ]