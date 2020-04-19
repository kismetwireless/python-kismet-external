PYTHON ?= /usr/bin/env python3
PROTOCBIN ?= protoc

PROTOBUF_DEFINITIONS := $(wildcard protobuf_definitions/*.proto)

.PHONY: all install protobuf clean

all:
	$(PYTHON) ./setup.py bdist

install:
	$(PYTHON) ./setup.py install

protobuf: $(PROTOBUF_DEFINITIONS:protobuf_definitions/%.proto=kismetexternal/%_pb2.py)

kismetexternal/%_pb2.py: protobuf_definitions/%.proto
	$(PROTOCBIN) -I protobuf_definitions --python_out=kismetexternal $^
	sed -i -E 's/^import.*_pb2/from . \0/' $@

clean:
	@-$(PYTHON) ./setup.py clean
