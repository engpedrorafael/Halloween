#!/bin/bash

CMD_OFF_L1="curl http://192.168.2.152/relay/1?turn=off"
CMD_OFF_L2="curl http://192.168.2.152/relay/0?turn=off"
CMD_OFF_L3="curl http://192.168.2.65/relay/0?turn=off"

pkill -f lux1
pkill -f lux2
pkill -f lux3
sleep 1
${CMD_OFF_L1}
${CMD_OFF_L2}
${CMD_OFF_L3}

