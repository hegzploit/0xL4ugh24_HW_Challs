FROM debian:bookworm AS build
RUN apt-get update && apt-get install -y \
    gcc \
    make \
    libc6-dev

WORKDIR /build
COPY chal.c .
RUN gcc -o chal chal.c

FROM debian:bookworm AS run
RUN apt-get update && apt-get install socat -y
WORKDIR /app
# Copy the compiled binary from build stage
COPY --from=build /build/chal .
RUN chmod +x /app/chal

EXPOSE 11111
ENTRYPOINT ["socat", "tcp-l:11111,fork,reuseaddr", "exec:/app/chal,pty,stderr"]
