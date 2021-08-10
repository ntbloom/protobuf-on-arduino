
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

HOMEDIR = $(HOME)/docs/programs/learnprotobuf
SCHEMAS = $(HOMEDIR)/schemas
SRC 		= $(HOMEDIR)/src

# arduino-cli
CLIFLAGS  = --libraries $(HOMEDIR)/nanopb
CLIFLAGS += --libraries $(HOMEDIR)/src
#CLIFLAGS += -v

# protobuf
#c++
NANOPB  		 = $(HOMEDIR)/nanopb/generator/nanopb_generator.py 
NANOPROTOC	 =  poetry run python $(NANOPB)
PBFLAGS  		 = -I $(SCHEMAS)
PBFLAGS 		+= --output-dir=$(HOMEDIR)/src
#PBFLAGS 		+= --timestamp
PBFLAGS 		+= --no-strip-path

#python
PROTOC 			 = protoc
PYTHONDIR		 = $(HOMEDIR)/python
PROTOCFLAGS  = --python_out=$(PYTHONDIR)
PROTOCFLAGS += -I $(SCHEMAS)

PYSCRIPT 	   = $(HOMEDIR)/python/counter.py

.PHONY: python

protobuf:
	$(NANOPROTOC) $(PBFLAGS) $(SCHEMAS)/raincounter.proto
	$(PROTOC) $(PROTOCFLAGS) $(SCHEMAS)/raincounter.proto

build: protobuf
	$(CLI) compile $(CLIFLAGS) --fqbn $(FQBN) $(INO) $(WARN)

upload:
	$(CLI) upload -p $(PORT) --fqbn $(FQBN) $(INO) 

clean: 
	$(CLI) cache clean
	rm $(BINDIR)/*.out

all: build upload

listen:
	cat $(PORT)

python:
	poetry run python3 $(PYSCRIPT)
