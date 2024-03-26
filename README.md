# pyformat-webapp

A flask app using docker to reformat python code

### Run locally
```bash
pip install -r requirements.txt
python app.py
```

### Run with docker
```bash
docker build . -t <TAG-NAME>
docker run -p 5100:5100 <TAG-NAME>
```