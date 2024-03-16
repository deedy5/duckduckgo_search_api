FROM python:3.12.2-slim-bookworm

# Create appuser and switch to it
RUN useradd --create-home appuser
USER appuser

# Include the directory where python packages are installed in the PATH
ENV PATH="/home/appuser/.local/bin:${PATH}"

# Set the working directory to a folder inside appuser's home directory
WORKDIR /home/appuser/app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy the application code
COPY ./duckduckgo_search_api /home/appuser/app/duckduckgo_search_api

# Run the application
CMD ["uvicorn", "duckduckgo_search_api.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "warning"]
