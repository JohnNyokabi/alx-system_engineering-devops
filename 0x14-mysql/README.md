# 0x14. MySQL

## Requirements
	* Ubuntu 20.04LTS
	* vi, vim, emacs editors
	*shellcheck(version 0.3.7)

## Tasks
   | Task | Description |
   | ---- | ----------- |
   | 0. Install MySQL | Installing MySQL(version 5.7.x) on both web-01 and web-02 |
   | 1. Let us in | Create a user and password for both MySQL databases which will allow the checker to access them |
   | 2. If only you could see what I've seen with your eyes | In order to set up replication, there's need to have a database with at least one table and one row in the primary MySQL server(web-01) to replicate from |
   | 3. Quite an experience to live in fear, isn't it? | Create a new user for the replica server in the primary MySQL server(web-01) |
   | [4-mysql_configuration_primary][4-mysql_configuration_replica] | Setup a primary-replica infrastructure using MySQL |
   | [5-mysql_backup] | Bash script that generates a MySQL dump and creates a compressed archive out of it |