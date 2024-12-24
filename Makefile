
.PHONY: start_postgres
start_postgres:
	docker-compose up -d postgresql

.PHONY: stop_postgres
stop_postgres:
	docker-compose stop postgresql