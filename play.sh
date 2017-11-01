#!/bin/bash

#echo `(pactl list sinks | grep "Volume: 0:")| awk '{print $3}'`


#if [[ $1 =~ .*rapariga.* ]]; then
#  amixer -D pulse sset Master 40%
#else  
#  amixer -D pulse sset Master 100%
#fi

nvlc $1 --intf dummy --play-and-exit 
