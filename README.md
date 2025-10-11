# openpose-docker
A docker build file for CMU openpose with Python API support

### Sources
- https://github.com/CMU-Perceptual-Computing-Lab/openpose
- https://hub.docker.com/r/cwaffles/openpose

## Running multistage Docker (Openpose + api)
- sudo docker build -f Dockerfile.multistage -t sign2text-full .
- sudo docker run --gpus all --rm -it sign2text-full python /test_integration.py
- (testing) sudo docker run --gpus all --rm -it -v $(pwd):/workspace sign2text-full python /workspace/test_integration.py

### Requirements
- Nvidia Docker runtime: https://github.com/NVIDIA/nvidia-docker#quickstart
- CUDA 10.0 or higher on your host, check with `nvidia-smi`
- Download `models` from [this drive link](https://drive.google.com/drive/folders/16Q0DSqVUwp4e7sV7BXrS64S-094m7RNk?usp=drive_link), ensure it is at root path `openpose-docker/models`

### Setup

1. Install Ubuntu 22.04 LTS

2. Install Docker Engine
   - Follow the apt installation instructions from [Docker's official documentation](https://docs.docker.com/engine/install/ubuntu/)

3. Clone the repository
   ```bash
   git clone https://github.com/dboo0012/openpose-docker
   cd ./openpose-docker
   ```

4. ~~Replace Dockerfile (Important)~~
  ~~- Replace the existing Dockerfile with the file from [this Google Drive link](https://drive.google.com/file/d/1cfEdG10LpZe4FPVj3aIzd8i8ZbrFBhHz/view?usp=drive_link)~~

5. Copy models directory (Important)
   - Copy the models file into the directory so it looks like: `openpose-docker/models/`

6. Build the Docker image
   ```bash
   sudo docker build -t openpose .
   ```

7. Install NVIDIA Container Toolkit
   - Follow the installation guide from [NVIDIA's documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

8. Validate GPU detection
   ```bash
   sudo docker run --rm --gpus all nvidia/cuda:11.4.3-devel-ubuntu20.04 nvidia-smi
   ```

9. Run the OpenPose container (This takes a while)
   ```bash
   sudo docker run --gpus all --name openpose -it openpose:latest /bin/bash
   ```

10. Set up Python OpenPose inside the container
    ```bash
    cd /openpose/build/python/openpose
    cp ./pyopenpose.cpython-311-x86_64-linux-gnu.so /usr/local/lib/python3.11/dist-packages
    cd /usr/local/lib/python3.11/dist-packages
    ln -s pyopenpose.cpython-311-x86_64-linux-gnu.so pyopenpose
    export LD_LIBRARY_PATH=/openpose/build/python/openpose
    ```

11. Test Python OpenPose
    ```bash
    python3
    ```
    ```python
    >>> import pyopenpose as op
    >>> 
    ```

### Building Docker image
`sudo docker build -t openpose-docker .`

### Running Docker image
`sudo docker run --rm -it --gpus all openpose-docker bash`

### Useful docker commands

1. sudo docker start -ai openpose (start with shell)

2. sudo docker exec -it openpose /bin/bash (reentering shell)

3. exit (exit shell)

### Example
The Openpose repo is in `/openpose`