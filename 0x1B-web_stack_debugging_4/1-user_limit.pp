# change OS configuration to login with holberton user

exec {'replace-1':
	provider => shell,
	command	 => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
	before	 => Exec['replace-2'],
}

exec {'replace-2':
	provider => shell,
	comand	 => 'sudo sed -i "s/noile 4/nofile 40000/" /security/limits.config',
}
