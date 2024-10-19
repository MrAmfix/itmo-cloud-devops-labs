import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def service2():
    return {'Answer': 'This is second service'}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)
