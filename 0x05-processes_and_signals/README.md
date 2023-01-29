# 0x05. Processes and signals

---
## Learning Objectives:bulb:
What you should learn from this project:

* What is a PID
* What is a process
* How to find a process’ PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored

---

### [0. What is my PID](./0-what-is-my-pid)
* Write a Bash script that displays its own PID.


### [1. List your processes](./1-list_your_processes)
* Write a Bash script that displays a list of currently running processes.


### [2. Show your Bash PID](./2-show_your_bash_pid)
* Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.


### [3. Show your Bash PID made easy](./3-show_your_bash_pid_made_easy)
* Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.


### [4. To infinity and beyond](./4-to_infinity_and_beyond)
* Write a Bash script that displays To infinity and beyond indefinitely. 


### [5. Don't stop me now](./5-dont_stop_me_now)
* Bash script that stops 4-to_infinity_and_beyond process.


### [6. Stop me if you can](./6-stop_me_if_you_can)
* Another Bash script that stops 4-to_infinity_and_beyond process.


### [7. Highlander](./7-highlander)
* Write a Bash script that displays:
•	To infinity and beyond indefinitely
•	With a sleep 2 in between each iteration
•	I am invincible!!! when receiving a SIGTERM signal


### [8. Beheaded process](./8-beheaded_process)
* Write a Bash script that kills the process 7-highlander.


### [9. Process and PID file](./100-process_and_pid_file)
* Write a Bash script that:
•	Creates the file /var/run/myscript.pid containing its PID
•	Displays To infinity and beyond indefinitely
•	Displays I hate the kill command when receiving a SIGTERM signal
•	Displays Y U no love me?! when receiving a SIGINT signal
•	Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal.


### [10. Manage my process](./101-manage_my_process)
* Bash (init) script 101-manage_my_process that manages manage_my_process.


### [11. Zombie](./102-zombie.c)
* C program that creates 5 zombie processes. For every zombie process created, it displays Zombie process created, PID: ZOMBIE_PID
