export PHPADMIN_PORT=8001
export OPENCART_PORT=8080
export LOCAL_IP=192.168.1.64

start: stop
	cd $(CURDIR)/Docker && docker-compose pull && docker-compose up

stop:
	cd $(CURDIR)/Docker && docker-compose kill && docker-compose down --volumes
