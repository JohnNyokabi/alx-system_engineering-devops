# Using puppet to make changes to the config file
file_line { 'Turn of passwd auth':
	ensure  => 'present',
	path    => '/etc/ssh/ssh-config',
	line    => '    PasswordAuthentication no'
	match   => 'PasswordAuthentication yes',
}
file_line { 'Declare identity file':
	ensure  => 'present',
	path    => '/etc/ssh/ssh-config',
	line	=> 'IdentityFile ~/.ssh/school',
}
