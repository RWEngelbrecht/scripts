#!/bin/bash

# $1 must be message; $2 must be ~num deciseconds to run
print_spinner () {
	spin='-\|/'
	i=0
	j=0

	while (( $j < $2 )) 
	do
		i=$(( (i+1) %4 ))
		printf "\r$1 ${spin:$i:1}"
		j+=1
		sleep .1
	done
}

spinny_time=20000
tmux new -d -s auto24 'ssh dev-auto24 "source /srv/auto24-rigardt/setenv; /srv/auto24-rigardt/manage.py runserver 0.0.0.0:8103"; exec $SHELL'
print_spinner "Starting auto24 django server..." $spinny_time
printf "Django server running in tmux session auto24...\n\tto access, run:\t\ttmux attach -t auto24\n"

tmux new -d -s portal_tunnel 'ssh -v -N -L 8103:10.202.36.6:8103 msp-jmppl99;exec $SHELL'
print_spinner "Creating tunnel to cloudlink server..." $spinny_time
printf "Tunnel running in tmux session portal_tunnel...\n\tto access, run:\t\ttmux attach -t portal_tunnel\n"
