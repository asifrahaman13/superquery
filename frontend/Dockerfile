# Use the official Node.js image with Next.js
FROM node:20

# Set working directory
WORKDIR /app/frontend

# Copy package.json and package-lock.json
COPY package.json ./

# Install Bun
RUN curl -fsSL https://bun.sh/install | bash

# Set environment variables for Bun
ENV BUN_INSTALL=/root/.bun
ENV PATH=$BUN_INSTALL/bin:$PATH
ENV BUN_PATH=$BUN_INSTALL/bin/bun

# Install dependencies with Bun
RUN bun install --no-cache

# Copy the rest of the frontend code
COPY . .

# Expose the port on which the Next.js app runs
EXPOSE 3000

# Command to build and start the Next.js application with Bun
CMD ["bun", "run", "dev"]
