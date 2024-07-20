#!/bin/sh

# Function to wait for PostgreSQL to be available
wait_for_postgres() {
  echo "Waiting for postgres..."

  while ! nc -z postgres-db $POSTGRES_CONTAINER_PORT; do
    sleep 0.1
  done

  echo "PostgreSQL started"
}

# Wait for PostgreSQL
wait_for_postgres

# Apply database migrations
echo "Applying database migrations..."
alembic upgrade head

# Start the Flask server
echo "Starting Flask server..."
flask run --host=0.0.0.0
