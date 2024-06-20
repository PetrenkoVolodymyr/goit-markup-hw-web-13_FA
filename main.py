from fastapi import FastAPI

import redis.asyncio as redis
from fastapi_limiter import FastAPILimiter

from src.routes import notes
from src.routes import auth
from src.routes import users
from fastapi.middleware.cors import CORSMiddleware

from src.conf.config import config

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix='/api')
app.include_router(users.router, prefix='/api')
app.include_router(notes.router, prefix='/api')


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.on_event("startup")
async def startup():
    r = await redis.Redis(
        host=config.REDIS_DOMAIN,
        port=config.REDIS_PORT,
        db=0,
        password=config.REDIS_PASSWORD,
    )
    await FastAPILimiter.init(r)