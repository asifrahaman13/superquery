#!bin/bash

# Start the backend server in a new terminal
gnome-terminal -- bash -c "uv run uvicorn src.main:app --reload; exec bash"

# Start the web server in a new terminal
gnome-terminal -- bash -c "cd web && bun run dev; exec bash"
