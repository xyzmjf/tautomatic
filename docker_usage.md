
**Docker**

There is now a Docker image of the tautomatic application which may be 
a convenient way to facilitate installation and usage. 

In this documentation we assume the docker command tools are already installed. 

Create and move to a relevant folder for obtaining and testing the Docker image.

Pull Docker image from Docker hub

```
docker pull xyzmjf/tautomatic:latest
```
Check Docker images now present on your machine

```
docker image ls
=> 
REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
xyzmjf/tautomatic   latest    3b650f4d0854   16 minutes ago   3.55GB
ubuntu              latest    99284ca6cea0   2 weeks ago      77.8MB
```

see IMAGE ID above - use this to start image so that we have a running container
```
docker run -td 3b650f4d0854
```
The docker ps command shows the ID of the image and the running container
```
docker ps
=> 
CONTAINER ID   IMAGE          COMMAND       CREATED          STATUS          PORTS     NAMES
4cc5a30fc984   3b650f4d0854   "/bin/bash"   44 seconds ago   Up 43 seconds             zealous_kilby
```

Now obtain a shell (as root) inside container
```
docker exec -it 4cc5a30fc984 bash
```

Once the container is accessed become the 'tautomatic' user
```
su tautomatic
cd /home/tautomatic
```

In the current implementation of the container the xtb and openbabel tools are stored
in a base conda (not mamba) environment.

Activate base environment 
```
~/miniconda/bin/conda init

bash
```

This then gives a new shell with base environment active.
Change directory ready to run the tautomatic scripts.

```
cd ./tautomatic 
```

Now generate tautomers and save to temporary file. 
```
./generate_tautomers.py uracil.smi > temp_uracil.smi
```

Run the code to score the tautomers in a solvent
```
./score_tautomers.py temp_uracil.smi water > uracil_scores.txt

cat uracil_scores.txt
```

Exit the tautomatic user and exit the container by using the exit command multiple times.

Check if the container is still running.
```
docker ps
CONTAINER ID   IMAGE          COMMAND       CREATED          STATUS          PORTS     NAMES
c02832fc3baf   3b650f4d0854   "/bin/bash"   24 minutes ago   Up 24 minutes             confident_nightingale
```

If so then stop if required.
```
docker stop c02832fc3baf
```

