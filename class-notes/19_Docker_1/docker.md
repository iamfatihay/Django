https://docs.docker.com/get-started/docker_cheatsheet.pdf

$ docker --version
$ docker version # Detaylı versiyon bilgisi.

$ docker info

$ docker --help
$ docker help
$ docker command --help

$ docker search <imagename> # dockerhub'da ara.


# Image Build:
$ docker build .
$ docker build . --tag <imagename> # lowercase
$ docker build . -t <imagename> # lowercase
# Image build et ve image'a isim:sürüm ver:
$ docker build . -t <imagename:version>
$ docker build . -t <imagename:version> --no-cache