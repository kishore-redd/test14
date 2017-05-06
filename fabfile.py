from fabric.api import local


def test10():





	local("cd /home/devops/python/fab14/test14 && touch file11 file12 file13")
	


	local("cd /home/devops/python/fab14/test14 && git add . && git commit -m test")



	local("cd /home/devops/python/fab14/test14 && git push origin master")
