.PHONY: clean run

build/puzzle: src/puzzle-day$(DAY)-$(IDX).c | build
	@gcc src/puzzle-day$(DAY)-$(IDX).c -o build/puzzle
build:
	@mkdir -p build
run: build/puzzle
	@build/puzzle
clean:
	@rm -rf build
