#fix a container when a GET HTTP method is requested to Apache web server

exec { '/usr/bin/env sed -i "s/phpp/php/g" /var/www/html/wp-settings.php': }