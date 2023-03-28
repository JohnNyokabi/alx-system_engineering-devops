# 0x0C. Web server

## Requirements
   * Ubuntu 20.04 LTS
   * Shellcheck version 0.3.7
   * vi, vim or emacs editors

## Tasks
   | Task | Description |
   | ---- | ----------- |
   | 0-transfer_a_file | Script that transfers a file from our client to a server |
   | 1-install_nginx_web_server | install [nginx] on [web-01] server. Nginx should listen on port 80 |
   | 2-setup_a_domain_name | Provide a domain name only and configure DNS records with an A entry so
   that the root domain points to web-01 IP address |
   | 3-redirection | Configure nginx server so that [/redirect_me] is redirecting to another page |
   | 4-not_found_page_404 | Configure Nginx server to have a custom 404 page that contains string ["Ceci n'est pas une page"] |
   | 7-puppet_install_nginx_web_server.pp | configure nginx using puppet, just as you did,
   install and configure nginx server using Puppet instead of Bash. |