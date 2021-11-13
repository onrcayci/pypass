FROM python:slim

WORKDIR /usr/app

COPY requirements.txt .
RUN python -m venv .venv
RUN .venv/bin/pip install -r requirements.txt

COPY pypass ./pypass

ENTRYPOINT [ "/usr/app/.venv/bin/uvicorn", "pypass.app.app:app", "--host", "0.0.0.0" ]