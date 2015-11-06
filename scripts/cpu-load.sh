#!/bin/bash

echo "$(uptime) $(hostname)" | awk '{print $(NF-3), $(NF-2), $(NF-1),$(NF)}' | awk '{printf("BOUNDARY_CPU_LOAD_1_MINUTE %s %s\nBOUNDARY_CPU_LOAD_5_MINUTE %s %s\nBOUNDARY_CPU_LOAD_15_MINUTE %s %s\n",$1,$4,$2,$4,$3,$4)}'
