# Load .env variables
include .env

# Start network and services
start: network services
	@echo "Network and all services started successfully."

# Create Docker network if it doesnt exist (in "start")
network:
	@echo "Checking if network exists..."
	@if ! docker network ls | grep -q $(NETWORK_NAME); then \
		echo "Network $(NETWORK_NAME) does not exist. Creating it..."; \
		docker network create $(NETWORK_NAME); \
	else \
		echo "Network $(NETWORK_NAME) already exists."; \
	fi

# Start all services (in "start")
services:
	@echo "Starting PostgreSQL Compose project..."
	@cd $(POSTGRES_DIR) && docker-compose up -d || { echo "Failed to start PostgreSQL"; exit 1; }
	@echo "Starting Grafana Compose project..."
	@cd $(GRAFANA_DIR) && docker-compose up -d || { echo "Failed to start Grafana"; exit 1; }

# Stop services
stop:
	@echo "Stopping services..."
	@cd $(GRAFANA_DIR) && docker-compose down || { echo "Failed to stop Grafana"; exit 1; }
	@cd $(POSTGRES_DIR) && docker-compose down || { echo "Failed to stop PostgreSQL"; exit 1; }
	@echo "All services stopped."

# Check services status
status:
	@echo "Checking the status of services..."
	@docker ps --filter "name=postgres" --filter "name=grafana"

# Show logs for both PostgreSQL and Grafana services
logs:
	@echo "Fetching logs for PostgreSQL and Grafana..."
	@cd $(GRAFANA_DIR) && docker-compose logs --tail=200 -f postgres &
	@cd $(POSTGRES_DIR) && docker-compose logs --tail=200 -f grafana &
	@wait

# Clean all resources: containers, networks, and volumes
clean: stop
	echo "Removing containers, networks, and volumes..."
	@docker network rm $(NETWORK_NAME) || { echo "Network $(NETWORK_NAME) not found."; }
	@docker volume prune -f
	@echo "Clean up complete."
