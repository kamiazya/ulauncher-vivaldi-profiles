.PHONY: start stop-service restart-service link-dev-extension unlink-dev-extension remove-published-extension

AUTHOR := kamiazya
EXTENSION_NAME := ulauncher-vivaldi-profiles
EXTENSION_ID := com.github.$(AUTHOR).$(EXTENSION_NAME)
EXTENSIONS_DIR := $(HOME)/.local/share/ulauncher/extensions
DEV_EXTENSION_PATH := $(EXTENSIONS_DIR)/$(EXTENSION_NAME)
PUBLISHED_EXTENSION_PATH := $(EXTENSIONS_DIR)/$(EXTENSION_ID)

start: stop-service remove-published-extension link-dev-extension
	ulauncher --dev -v

stop-service:
	systemctl --user stop ulauncher

restart-service:
	systemctl --user restart ulauncher

link-dev-extension: unlink-dev-extension
	ln -s $(PWD) $(DEV_EXTENSION_PATH)

unlink-dev-extension:
	if [ -e $(DEV_EXTENSION_PATH) ]; then \
		rm $(DEV_EXTENSION_PATH); \
	fi;

remove-published-extension:
	if [ -e $(PUBLISHED_EXTENSION_PATH) ]; then \
		rm -rf $(PUBLISHED_EXTENSION_PATH);  \
	fi;
