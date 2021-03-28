import uvicorn

from typing import Optional

from fastapi import FastAPI
from paypay.entrypoint.http.endpoints import user


def build_app() -> FastAPI:
    app = FastAPI()
    app.include_router(user.router, tags=["users"])

    return app


app = build_app()


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        port=5000,
        host='0.0.0.0',
        reload=True,
        access_log=False
    )
