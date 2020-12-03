From ubuntu:20.04
# Echo a message
RUN echo 'we are building image.'

RUN apt-get update && \
    apt-get install -y wget bash zip rsync python3-venv python3-dev build-essential

Run python3 --version

Run apt update

Run apt install -y git
Run apt install -y vim
Run apt install -y htop

Run apt update
Run apt install -y iproute2

Run apt install -y tree

Run apt install -y python3-pip

# INSTALL gmsh
RUN pip3 install gmsh
ENV PYTHONPATH=/usr/local/lib/python3.8/site-packages/gmsh-4.7.1-Linux64-sdk/lib:$PYTHONPATH

# INSTALL gmsh GUI depended libs
RUN apt install -y libglu1-mesa
RUN apt install -y libxrender1
RUN apt install -y libxcursor1
RUN apt install -y libxft2
RUN apt install -y libxinerama1

Run pip3 install numpy
Run pip3 install scipy
Run pip3 install matplotlib
Run pip3 install pybind11

Run apt-get install -y libhdf4-dev
Run pip3 install h5py

Run apt update
Run apt-get install -y xli

RUN pip3 install pygmsh
RUN pip3 install meshio[all]
RUN pip3 install pyvista

