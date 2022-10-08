default: update up

up:
	docker-compose up --detach --wait --remove-orphans

down:
	docker-compose down --remove-orphans

start: up
stop: down

update: stop
	docker-compose stop
	docker-compose rm -f
	docker-compose pull

update-and-restart: update up

clean: stop
	docker-compose rm -f
