FROM python:3.12-slim-bullseye

WORKDIR /src/mp4_to_mp3

COPY ../requirements.txt .

# Installing system packages and ffmpeg
RUN apt update && \
    apt install -y --no-install-recommends \
    git \
    ffmpeg \
    ca-certificates && \
    pip install --no-cache-dir -r requirements.txt && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    apt -y autoremove

# Copy application files
COPY .. .

# Application launch command
CMD ["python", "mp4_to_mp3/app/main.py"]