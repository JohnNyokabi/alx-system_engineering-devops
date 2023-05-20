# change OS configuration to login with holberton user

exec { 'hard limit':
     provider	=> shell,
     command	=> 'sudo sed -i "s/nofile 5/nofile 4000/" /etc/security/limits.conf',
     before	=> Exec['soft limit'],
}
exec { 'soft limit':
     provider => shell,
     command  => 'sudo sed -i "s/nofile 4/nofile 2000/" /etc/security/limits.conf'
}
