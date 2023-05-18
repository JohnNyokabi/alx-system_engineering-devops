# change OS configuration to login with holberton user

exec {'replace-1':
	command	 => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
	path	 => '/usr/local/bin/:/bin/'
}

exec {'replace-2':
	comand	 => 'sudo sed -i "s/nofile 4/nofile 50000/" /security/limits.config',
	path 	 => '/usr/local/bin/:/bin/'
}
