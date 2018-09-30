import docker
from time import sleep

cliente = docker.DockerClient(base_url='unix://var/run/docker.sock')


def remove_container():
    lista = cliente.containers.list(all)
    for c in lista:
        if c.status == 'exited' or c.stats == 'dead' or c.stats == 'removing':
            print("Esee container {} será removido, pois não está mais sendo utilizado.".format(c.short_id))
            c.remove(force=True)

while True:
    remove_container()
    sleep(60)
