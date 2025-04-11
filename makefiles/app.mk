.PHONY: app.test  		 	\
		app.local 		 	\
		app.add   		 	\
		app.migrate		 	\
		app.static		 	\
		app.install.deps	\
		app.rm.static

app.test: ## Ejecuta las pruebas
	python3 app/manage.py test

app.local: ## Inicia el servidor local
	python3 app/manage.py runserver $(HTTP_PORT)

app.add: ## Crea una nueva aplicación
	@echo "Creando una nueva aplicación..."
	@echo "Nombre de la aplicación: "
	@read app_name; \
	python3 app/manage.py startapp $$app_name; \
	mv $$app_name app/

app.migrate: ## Aplica las migraciones
	python3 app/manage.py makemigrations
	python3 app/manage.py migrate

app.static: ## Recopila los archivos estáticos
	python3 app/manage.py collectstatic

app.install.deps: ## Instala dependencias
	pip install -r app/requirements.txt

app.rm.static: ## Elimina archivos estáticos
	rm -rf app/static
