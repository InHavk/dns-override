CC?=gcc

.PHONY: clean test

all: clean dns-override.so test

# FreeBSD does not provide "-ldl", give another try without it
dns-override.so: dns-override.c
	$(CC) -Wall -Werror -fPIC -shared -o dns-override.so dns-override.c -ldl || \
	$(CC) -Wall -Werror -fPIC -shared -o dns-override.so dns-override.c

clean:
	rm -rf *.so

test: dns-override.so
	bats *.bats
