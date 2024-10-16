import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware


rt = APIRouter(prefix='/api')


@rt.get('/hash_code')
async def get_hash_code(
        s: str
):
    return {'answer': hash(s)}


@rt.get('/caesar_cipher')
async def get_caesar_cipher(
        s: str
):
    ciphertext = ""
    for i in s:
        if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
            if i == 'x' or i == 'X' or i == 'y' or i == 'Y' or i == 'z' or i == 'Z':
                ciphertext += chr(ord(i) - 23)
            else:
                ciphertext += chr(ord(i) + 3)
        else:
            ciphertext += i
    return {'answer': ciphertext}



app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin", "Authorization"],
)

app.include_router(rt)


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
