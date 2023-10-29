#!/bin/bash

./luxoff.sh
pkill -f vlc
    
./lux3.sh &
./play.sh Sounds/riso.mp3
sleep 1 
./luxoff.sh

./lux1.sh &
./lux3.sh &
./play.sh Sounds/clock.mp3    
sleep 10
./luxoff.sh
pkill -f vlc 

sleep 10
./lux3.sh &
./play.sh Sounds/trovao.mp3

sleep 5
./lux1.sh &
./play.sh Sounds/porta.mp3



