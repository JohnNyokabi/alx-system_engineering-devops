# 0x10. HTTPS SSL

## Requirements
	* Ubuntu 20.04LTS
	* shellcheck(version 0.3.7)
	* vi, vim or emacs editor

## Tasks
   | Task | Description |
   | ---- | ----------- |
   | 0-world_wide_web | Configure your domain zone so that the subdomain (www) points to the load balancer IP(lb-01) |
   | 1-haproxy_ssl_termination | Haproxy is configured to handle encrypted traffic, the script decrypts it and passes its on to its destination |
   | 100-redirect_http_to_https | Configures HAproxy to automatically redirect HTTP traffic to HTTPS |