FROM mcr.microsoft.com/playwright/python:v1.49.1-noble

WORKDIR /app

# Install system dependencies & python3.12-venv
RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends \
        python3.12-venv \
        tmux \
        curl \
        wget \
        git \
        procps \
        ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Pre-install browser-use for system python
RUN pip install --no-cache-dir --break-system-packages "browser-use>=0.5" playwright==1.49.1

# Pre-install /opt/browser-use-venv so agent setup is instantaneous (0s)
RUN python3 -m venv /opt/browser-use-venv && \
    /opt/browser-use-venv/bin/pip install --upgrade pip && \
    /opt/browser-use-venv/bin/pip install --no-cache-dir "browser-use>=0.5" playwright==1.49.1 && \
    chmod -R 777 /opt/browser-use-venv

# Pre-install OpenHands SDK environment for persona-openhands-sdk agent
RUN python3 -m venv /opt/openhands-sdk-venv && \
    /opt/openhands-sdk-venv/bin/pip install --upgrade pip && \
    /opt/openhands-sdk-venv/bin/pip install --no-cache-dir openhands-sdk openhands-tools fastapi && \
    chmod -R 777 /opt/openhands-sdk-venv

ENV BROWSER_USE_EXTRA_ARGS="--use-fake-ui-for-media-stream --use-fake-device-for-media-stream --unsafely-treat-insecure-origin-as-secure=http://192.168.0.109:8888,http://172.17.0.1:5173,http://localhost:8888,http://localhost:3001,http://localhost:5173,http://127.0.0.1:8888,http://127.0.0.1:3001,http://127.0.0.1:5173"

RUN mkdir -p /app/input /app/output /installed-agent
