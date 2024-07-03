#!bin/bash

# Start the backend server in a new terminal
gnome-terminal -- bash -c "uvicorn src.main:app --reload; exec bash"

# Start the frontend server in a new terminal
gnome-terminal -- bash -c "cd frontend && bun run dev; exec bash"
