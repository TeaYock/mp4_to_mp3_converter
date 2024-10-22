FROM python:3.12-bullseye

WORKDIR /src/app

COPY ../requirements.txt .

# Installing system packages and ffmpeg
RUN apt update && \
    apt install -y --no-install-recommends \
    coreutils \
    git \
    ffmpeg \
    ca-certificates && \
    pip install --no-cache-dir -r requirements.txt && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* && \
    apt -y autoremove

# Copy application files
COPY ../app /src/app

# Set PYTHONPATH environment variable
ENV PYTHONPATH=/src

# Application launch command
CMD ["python", "main.py"]