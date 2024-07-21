# Insight.io Task

This project implements a simple Flask application with a REST API endpoint to interact with the OpenAI API and store questions and answers in a database.

## Features

- **Ask a Question**: Send a POST request to the `/ask` endpoint with a question, and receive an answer from the OpenAI API.
- **Database Storage**: Questions and answers are stored in a PostgreSQL database.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

### Clone the repository

```sh
git clone https://github.com/your-username/insight-io-task.git
cd insight-io-task
```

### Set up environment variables

Create a `.env` file in the root directory of the project and add the following variables:
```env
APP_HOST_PORT=5000
APP_CONTAINER_PORT=5000
POSTGRES_HOST_PORT=5432
POSTGRES_CONTAINER_PORT=5432

POSTGRES_USER=<your_postgres_user>
POSTGRES_PASSWORD=<your_postgres_password>
POSTGRES_DB=questions_db

DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres-db:${POSTGRES_CONTAINER_PORT}/${POSTGRES_DB}

OPENAI_API_KEY=<your_openai_api_key>
```

### Build and run the application

```sh
docker-compose up --build
```

The app will be available at `http://localhost:<APP_HOST_PORT>`.

### Run tests

Tests are executed using pytest. They are configured to run in a GitHub Actions CI workflow.

To run tests locally:

```sh
pytest tests/
```
### GitHub Actions CI/CD
A GitHub Actions workflow is configured to run tests on each push to the main branch.
The workflow file is located at .github/workflows/ci.yml.

## Usage

### Endpoints

#### `/ask`

**Method:** POST

**Description:** This endpoint receives a JSON payload with a 'question' key, sends the question to the OpenAI API, stores the question and answer in the database, and returns the question and answer in a JSON response.

**Request Body:**
```json
{
  "question": "Who won the most Wimbledon titles in the open era?"
}
```

**Response Body:**
```json
{
  "question": "Who won the most Wimbledon titles in the open era?",
  "answer": "Roger Federer"
}
```

