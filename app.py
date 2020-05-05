from paramiko import SSHClient, AutoAddPolicy
from os import environ
import base64 as b64
import time

def start_bench(func: str):
	start_time = time.time()
	hostname = environ.get('SSH_HOST', None)
	username=environ.get('SSH_USR', None)
	password=b64.b64decode(environ.get('SSH_PWD', None))

	try:
		password = password.decode('utf-8')
	except:
		pass

	try:
		ssh = SSHClient() 
		ssh.set_missing_host_key_policy(AutoAddPolicy())
		ssh.connect(
			hostname=hostname,
			port=22,
			username=username,
			password=password,
			compress=True,
			look_for_keys=False,
			allow_agent=False
		)

		# pylint: disable=unbalanced-tuple-unpacking,unused-variable
		stdin, stdout, err = ssh.exec_command(func)

		arr_output = []
		for el in stdout:
			arr_output.append(el)
		
		result = {
			'lines_cnt': len(arr_output),
			'execution_cmd': func,  
			'execution_time': time.time() - start_time
		}
		return result

	except Exception as e:
		print (e)
		return None
	
	ssh.close()


if __name__ == '__main__':
	instructions = ['ls -l']
	benchmark = map(lambda x: start_bench(x), instructions)
	for el in benchmark:
		print (el)