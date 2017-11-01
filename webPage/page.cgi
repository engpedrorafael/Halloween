#!/bin/bash
echo "Content-type: text/html"
echo ""

saveIFS=$IFS
IFS='=&'
parm=($QUERY_STRING)
IFS=$saveIFS


echo "command: ${parm[0]}"
echo "</br>"
echo "parameter: ${parm[1]}"
echo "</br>"

if [[ "${parm[0]}" == "action" ]]; then
    /home/gfi/Halloween/${parm[1]}.py 2>&1
elif [[ "${parm[0]}" == "sound" ]]; then
    /home/gfi/Halloween/play.sh /home/gfi/Halloween/Sounds/${parm[1]}.mp3 2>&1
elif [[ "${parm[0]}" == "stop" ]]; then
    if [[ "${parm[1]}" == "sound" ]]; then
        pkill -f vlc
    elif [[ "${parm[1]}" == "action" ]]; then
        pkill -f python
        /home/gfi/Halloween/off.py 2>&1
    fi
else
    echo "Unknwon command/parameter"
fi
