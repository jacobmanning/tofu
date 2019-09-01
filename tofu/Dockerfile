FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
  software-properties-common

RUN apt-get install -y \
  build-essential \
  curl \
  wget

# Bazel
RUN apt-get install -y \
  pkg-config \
  zip \
  zlib1g-dev \
  unzip \
  python3

RUN apt-get -y install openjdk-8-jdk && \
  echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list && \
  curl https://bazel.build/bazel-release.pub.gpg | apt-key add - && \
  apt-get update && \
  apt-get -y install bazel && \
  apt-get -y upgrade bazel

RUN bazel version
