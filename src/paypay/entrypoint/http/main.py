import uvicorn  # type: ignore

from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse
from src.paypay.entrypoint.http.endpoints import user, payment, login  # type: ignore
from src.paypay.entrypoint.http.errors import HTTP_ERRORS  # type: ignore


def build_app() -> FastAPI:
    app = FastAPI()
    app.include_router(user.router, tags=["users"])
    app.include_router(payment.router, tags=["payments"])
    app.include_router(login.router, tags=["login"])

    return app


app = build_app()


@app.exception_handler(ValueError)
async def error_handler(request: Request, error: ValueError):
    status_code = HTTP_ERRORS.get(type(error), status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JSONResponse(
        status_code=status_code,
        content={"message": error.args[0]},
    )


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, host="0.0.0.0", reload=True, access_log=False)
