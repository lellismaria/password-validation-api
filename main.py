from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Password(BaseModel):
    password: str

@app.post("/validate_password")
async def validate_password(password: Password = Body(...)):
    error_messages = {
        "length": "A senha deve conter ao menos nove caracteres.",
        "lowercase": "A senha deve conter ao menos uma letra minúscula.",
        "uppercase": "A senha deve conter ao menos uma letra maiúscula.",
        "digit": "A senha deve conter ao menos um número.",
        "special_char": "A senha deve conter ao menos um caractere especial.",
        "repeated_char": "A senha não deve conter caracteres repetidos."
    }

    if len(password.password) < 9:
        raise HTTPException(status_code=400, detail={"status": 400, "message": error_messages["length"], "isValid": False})

    if not any(char.islower() for char in password.password):
        raise HTTPException(status_code=400, detail={"status": 400, "message": error_messages["lowercase"], "isValid": False})

    if not any(char.isupper() for char in password.password):
        raise HTTPException(status_code=400, detail={"status": 400, "message": error_messages["uppercase"], "isValid": False})

    if not any(char.isdigit() for char in password.password):
        raise HTTPException(status_code=400, detail={"status": 400, "message": error_messages["digit"], "isValid": False})

    if not any(char in "!@#$%^&*()-+" for char in password.password):
        raise HTTPException(status_code=400, detail={"status": 400, "message": error_messages["special_char"], "isValid": False})

    if len(set(password.password)) != len(password.password):
        raise HTTPException(status_code=400, detail={"status": 400, "message": error_messages["repeated_char"], "isValid": False})

    return {"status": 200, "message": "A senha é válida.", "isValid": True}