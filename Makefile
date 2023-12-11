.PHONY: all build run

all:
	$(MAKE) build && $(MAKE) run

build:
	pyinstaller ytgui.py

run:
	./dist/ytgui/ytgui
