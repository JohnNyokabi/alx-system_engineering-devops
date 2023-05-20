# 0x1A. Application Server

## Requirements
	* Ubuntu 20.04LTS
	* Shellcheck (version 0.3.7-5)

## Tasks
   | Task | Description |
   | ---- | ----------- |
   | [0. Set up development with python] | Exercise for setting up the development environment, for testing and debugging code before deploying it to production |
   | [1. Set up production with Gunicone] | Set up the production application server with `Gunicone` on `web-01`, port `5000` |
   | [2-app_server-nginx_config](/2-app_server-nginx_config) | Configure `Nginx` to serve the page from route `/airbnb-onepage/` |
   | [3-app_server-nginx_config](/3-app_server-nginx_config) | Configure `Nginx` to proxy HTTP requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to a Gunicorn instance listening on port 5001 |
   | [4-app_server-nginx_config](/4-app_server-nginx_config) | Serve `AirBnB_v3-RESTful API` on `web-01` |
   | [5-app_server-nginx_config](/5-app_server-nginx_config) | Serve `AirBnB_clone - Web dynamic` on `web-01` |
   | [gunicorn.service](/gunicorn.service) | `systemd` script for starting application server |
   | [4-reload_gunicorn_no_downtime](/4-reload_gunicorn_no_downtime) | Bash script to reload Gunicorn in a graceful way |