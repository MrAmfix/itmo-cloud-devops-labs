import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def service1():
    return {'Answer': 'This is first service'}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
