# syntax=docker/dockerfile:1
FROM ubuntu:21.10

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
RUN apt-get update -y \
	&& apt-get upgrade -y \
	&& apt-get install -y \
	build-essential\
	clang\
	clang-tidy\
	ninja-build\
	python3\
	librocksdb-dev\
	libfmt-dev\
	protobuf-compiler\
	python3-protobuf\
	libprotoc-dev\
	libprotobuf-dev\
	wget\
	cppcheck

RUN wget -qO- "https://cmake.org/files/v3.21/cmake-3.21.2-linux-x86_64.tar.gz" \
	| tar --strip-components=1 -xz -C /usr/local

COPY ./ /app/
# TODO
