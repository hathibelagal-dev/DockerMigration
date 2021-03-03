import docker
import os
import time
import sys

my_client = docker.APIClient(base_url='unix://var/run/docker.sock')

def export_filesystem():
	start = time.perf_counter()
	f = open("container.tar", "wb")
	for data in my_client.export(sys.argv[1]):
		f.write(data)
	f.close()
	end = time.perf_counter()
	os.system("cp container.tar /tmp")
	print("Time to export filesystem: %f s"%(end - start))

def import_filesystem():
	if os.path.isfile("container.tar"):
		start = time.perf_counter()
		my_client.import_image_from_file("container.tar", 
			repository="%s_im"%sys.argv[1], tag="latest")
		end = time.perf_counter()
		print("Time to import filesystem: %f s"%(end - start))
		os.remove("container.tar")
		my_client.remove_image("%s_im:latest"%sys.argv[1])

export_filesystem()
import_filesystem()
