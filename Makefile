PYTHON ?= /usr/bin/env python3
PROTOCBIN ?= protoc

.PHONY: all install protobuf clean

all:
	$(PYTHON) ./setup.py bdist

install:
	$(PYTHON) ./setup.py install

protobuf:
	( cd KismetExternal; \
	  $(PROTOCBIN) -I ../protobuf_definitions --python_out=. ../protobuf_definitions/*.proto; \
	  sed -i -E 's/^import.*_pb2/from . \0/' *_pb2.py ; \
	)

clean:
	@-$(PYTHON) ./setup.py clean
