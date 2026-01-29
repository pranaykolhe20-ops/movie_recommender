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
https://huggingface.co/datasets/pranayy2026/movie-rec-data/blob/main/movies_dict.pkl

RUN wget -O Data/processed/similarity.pkl \
https://huggingface.co/datasets/pranayy2026/movie-rec-data/blob/main/similarity.pkl

# render expects this
ENV PORT=10000
EXPOSE 10000

CMD ["python", "app.py"]
