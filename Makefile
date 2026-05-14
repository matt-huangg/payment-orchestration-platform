dev:
	.venv/bin/uvicorn app.main:app --reload

install: 
	.venv/bin/python -m pip install -r requirements.txt