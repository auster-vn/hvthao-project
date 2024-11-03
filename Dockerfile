FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .
COPY recommendation.py .
COPY app.py .
COPY start.sh .
COPY data ./data
COPY .env .env

RUN conda env create -f environment.yml

RUN chmod +x start.sh

CMD ["./start.sh"]

EXPOSE 8501
