.PHONY: test, valgrind

test: arrays
	./arrays

valgrind: arrays
	valgrind --leak-check=full ./arrays

arrays: arrays.c
	gcc -g -Wall -std=gnu99 -o arrays arrays.c
