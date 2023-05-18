#fix the stack to have 0 bugs
exec {'replace':
     provider => shell,
     path     => '/bin',
     command	 => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx'
}
exec {'restart':
     provider => shell,
     command	 => 'sudo service nginx restart',
}
