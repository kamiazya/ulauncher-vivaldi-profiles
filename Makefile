.PHONY: start stop-service restart-service

start: stop-service
	ulauncher --dev -v

stop-service:
	systemctl --user stop ulauncher

restart-service:
	systemctl --user restart ulauncher
