from fastapi import FastAPI

from passgen.routes import passgen

app = FastAPI(title="PyPass")
app.include_router(passgen, prefix="/api")
