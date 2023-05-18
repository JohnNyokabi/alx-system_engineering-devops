#fix the stack to have 0 bugs
exec {'replace':
	command	 => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
}
exec {'restart':
	command	 => 'sudo service nginx restart',
}
