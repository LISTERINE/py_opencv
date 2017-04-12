dockerbuild:
	docker build --no-cache -t py_opencv:latest .

dockerbuildcache:
	docker build -t py_opencv:latest .

dockerrun:
	make dockerbuildcache && docker-compose up -d

dockerclean:
	docker-compose kill && docker-compose rm

dockerexec:
	docker exec -it $$(docker-compose ps -q |head -n 1) /bin/bash
