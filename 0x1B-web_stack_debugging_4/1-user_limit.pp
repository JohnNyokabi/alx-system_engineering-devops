# change OS configuration to login with holberton user

exec {'OS configuration':
     command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
     path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
