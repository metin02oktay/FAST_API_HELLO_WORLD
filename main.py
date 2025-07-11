from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}   

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=443, ssl_certfile="certs/cert.pem", ssl_keyfile="certs/key.pem")