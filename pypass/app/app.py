from fastapi import FastAPI

from pypass.passgen.routes import passgen_router

app = FastAPI(title="PyPass")
app.include_router(passgen_router, prefix="/api")
