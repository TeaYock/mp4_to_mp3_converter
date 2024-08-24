FROM python:3.12-rc-slim-bullseye

WORKDIR /src/
COPY requirements.txt /src/

# Installing system packages and ffmpeg
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt


# Application launch command
CMD ["python", "main.py"]