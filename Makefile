include .env
.PHONY: start stop-service restart-service

AUTHOR := kamiazya
EXTENSION_NAME := ulauncher-vivaldi-profiles
EXTENSION_ID := com.github.$(AUTHOR).$(EXTENSION_NAME)

start: stop-service
	ulauncher --no-extensions --dev -v --hide-window

dev:
	VERBOSE=1 ULAUNCHER_WS_API=ws://127.0.0.1:5054/$(EXTENSION_ID) PYTHONPATH=$(PYTHONPATH) $(PYTHON3) $(PWD)/main.py

stop-service:
	systemctl --user stop ulauncher

restart-service:
	systemctl --user restart ulauncher
