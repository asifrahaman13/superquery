# Use the official Node.js image with Next.js and Bun
FROM node:20

# Set working directory
WORKDIR /app/frontend

# Copy package.json and package-lock.json
COPY . .

# Install Bun
RUN curl -fsSL https://bun.sh/install | bash

# Install dependencies with Bun
RUN bun install

# Copy the rest of the frontend code
COPY . .

# Expose the port on which the Next.js app runs
EXPOSE 3000

# Command to build and start the Next.js application with Bun
CMD ["bun", "run", "dev"]
