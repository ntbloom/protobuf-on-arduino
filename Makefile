
CPP = g++

CPPFLAGS  = -std=c++17
CPPFLAGS += -Wall
CPPFLAGS += -Wextra
CPPFLAGS += -pedantic
CPPFLAGS += -Werror

VFLAGS	= --quiet
VFLAGS += -v
VFLAGS += --tool=memcheck
VFLAGS += --leak-check=full
VFLAGS += --error-exitcode=1
VFLAGS += --show-reachable=yes
VFLAGS += --show-possibly-lost=yes
VFLAGS += --undef-value-errors=yes
VFLAGS += --track-origins=yes

CLI  = arduino-cli
FQBN = arduino:mbed_nano:nano33ble
PORT = /dev/ttyACM98
INO  = learnprotobuf.ino
WARN = --warnings all
BINDIR = bin

HOMEDIR = /home/ntbloom/docs/programs/learnprotobuf
SCHEMAS = $(HOMEDIR)/schemas
SRC 		= $(HOMEDIR)/src

protobuf:
	protoc -I=$(SCHEMAS) --cpp_out=$(SRC) $(SCHEMAS)/raincounter.proto

build: 
	$(CLI) compile --fqbn $(FQBN) $(INO) $(WARN)

upload:
	$(CLI) upload -p $(PORT) --fqbn $(FQBN) $(INO) 

clean: 
	$(CLI) cache clean
	rm $(BINDIR)/*.out

all: build upload


