#!/bin/bash
while true
do

        if /tmp/tald10/solver /vortex/vortex10 | grep -B 15 -A 30 'Found seed match'; then
                break
        fi
done

































