FROM mcr.microsoft.com/playwright/python:v1.49.1-noble

WORKDIR /app

# Install system dependencies & python3.12-venv
RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends python3.12-venv && \
    rm -rf /var/lib/apt/lists/*

# Pre-install browser-use for faster trials; agent install() can upgrade if missing.
RUN pip install --no-cache-dir --break-system-packages "browser-use>=0.5" playwright==1.49.1

# Pre-install OpenHands SDK environment for persona-openhands-sdk agent
RUN python3 -m venv /opt/openhands-sdk-venv && \
    /opt/openhands-sdk-venv/bin/pip install --upgrade pip && \
    /opt/openhands-sdk-venv/bin/pip install --no-cache-dir openhands-sdk openhands-tools fastapi && \
    chmod -R 777 /opt/openhands-sdk-venv

RUN mkdir -p /app/input /app/output

