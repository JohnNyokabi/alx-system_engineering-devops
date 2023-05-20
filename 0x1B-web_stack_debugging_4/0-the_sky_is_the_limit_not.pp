#fix the stack to have 0 bugs
exec {'set limit':
     path     => '/bin',
     command  => 'sed -i "s/15/2000/" /etc/default/nginx'
}
exec {'restart':
     command	 => '/usr/sbin/service nginx restart'
}
