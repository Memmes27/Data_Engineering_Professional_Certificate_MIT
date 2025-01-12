import os
import sys

def delete_container(container_name):
    os.system(f"docker stop {container_name}")
    os.system(f"docker rm {container_name}")
    print(f"Container {container_name} deleted")

#Read input arguments
if len(sys.argv) > 2:
    command = sys.argv[1]
    container_name = sys.argv[2]

    if command == '-delete':
        delete_container(container_name)
else:
    print("Usage: python delete_container.py -delete [container_name]")