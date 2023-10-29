#!/bin/bash

CMD_ON="curl http://192.168.2.152/relay/0?turn=on"
CMD_OFF="curl http://192.168.2.152/relay/0?turn=off"


for VARIABLE in {1..20}
do
    ${CMD_ON}
    sleep 0.100
    ${CMD_OFF}
    sleep 0.100
    ${CMD_ON}
    sleep 0.100
    ${CMD_OFF}
    sleep 2.000
done
