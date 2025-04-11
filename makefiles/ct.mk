.PHONY: ct.copy				\
		ct.build.image		\
		ct.destroy.image	\
		ct.run				\
		

DEST_DIR ?= local

ct.copy: ## Copiando archivos
	cp $(PROJECT_DIR)/requirements.txt docker/${DEST_DIR}/requirements.txt

ct.build.image: ct.copy ## Build image for development.:
	@cd docker/local && \
		docker build -f Dockerfile -t $(IMAGE) . --no-cache && \
		rm -f db.sqlite3

ct.destroy.image: 
	@echo "Destruyendo imagen de Docker..."
	@docker rmi $(IMAGE) -f

ct.run: ## Run container
	@echo [Application] $(PROJECT_NAME) running on http://localhost:$(HTTP_PORT)
	@export IMAGE="$(IMAGE)" && \
	export WORKDIR="$(WORKDIR)" && \
	export PROJECT_DIR="$(PROJECT_DIR)" && \
	export HTTP_PORT="$(HTTP_PORT)" && \
	export ENV="$(ENV)" && \
	export APP_ENV="$(APP_ENV)" && \
	docker compose up --remove-orphans

ct.test: ## Ejecutar
	@echo "Ejecutando pruebas..."
	@docker exec -it $(PROJECT_NAME) python3 $(PROJECT_DIR)/manage.py test
