FROM registry.fedoraproject.org/fedora:rawhide
RUN echo "fastestmirror=1" >> /etc/dnf/dnf.conf
RUN dnf -y upgrade
RUN dnf -y install dnf-plugins-core
RUN dnf -y copr enable mhayden/azure-cli
ARG CACHEBUST=1
RUN dnf --exclude python3-azure-sdk -y install azure-cli
CMD /usr/bin/az
