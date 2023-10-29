#!/bin/bash

CMD_ON="curl http://192.168.2.65/relay/0?turn=on"
CMD_OFF="curl http://192.168.2.65/relay/0?turn=off"


for VARIABLE in {1..10}
do
    ${CMD_ON}
    sleep 0.250
    ${CMD_OFF}
    sleep 0.250
done
