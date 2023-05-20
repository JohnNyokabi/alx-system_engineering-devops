#fix the stack to have 0 bugs
exec {'set limit':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 2000\"/" /etc/default/nginx',
  before   => Exec['restart'],
}
exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart'
}
