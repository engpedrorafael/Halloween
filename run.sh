#!/bin/bash
while echo "Start loop..."; do
    
    python flash.py &
    ./play.sh Sounds/lobo.mp3
    sleep 10
    
    python flash.py &
    ./play.sh Sounds/Azghost.mp3
    
    sleep 10
    python flash.py &
    ./play.sh Sounds/riso.mp3
    
    sleep 5
    
    python fill.py
    
    sleep 30

done
