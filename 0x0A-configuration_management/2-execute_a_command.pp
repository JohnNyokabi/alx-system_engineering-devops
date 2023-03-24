# Manifest that kills a process by calling pkill
exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow'
}