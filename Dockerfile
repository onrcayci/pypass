FROM python:slim

WORKDIR /usr/app

COPY requirements.txt .
RUN python -m venv .venv
RUN .venv/bin/pip install -r requirements.txt

COPY pypass ./pypass

# Add PYTHON_PATH environment variable
ENV PYTHON_PATH=/usr/app/pypass:/usr/app/pypass/passgen:/usr/app/pypass/app

ENTRYPOINT [ "/usr/app/.venv/bin/uvicorn", "pypass.app.app:app", "--host", "0.0.0.0" ]