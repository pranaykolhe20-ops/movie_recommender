FROM python:3.11-slim

WORKDIR /app

# system deps
RUN apt-get update && apt-get install -y wget

# install python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

# create data folder
RUN mkdir -p Data/processed

# download model files (REPLACE LINKS)
RUN wget -O Data/processed/movies_dict.pkl \
https://drive.google.com/uc?export=download&id=1oXnPvtImlZIyPc2S5xFP8Cscl4rkvVYg

RUN wget -O Data/processed/similarity.pkl \
https://drive.google.com/uc?export=download&id=1v9gYyQaOBsFcFcXVAwCEeIS7tB5tkhxA

# render expects this
ENV PORT=10000
EXPOSE 10000

CMD ["python", "app.py"]
