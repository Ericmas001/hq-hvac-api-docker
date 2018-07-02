#!/bin/sh

echo ""
echo ">>> VERSION"
uname -a

echo ""
echo ">>> USER GROUPS"
groups

echo "" > /exec/const.py && \
	echo "KEY = \"$KEY\"" >> /exec/const.py && \
	echo "PIN = $PIN" >> /exec/const.py

cp -n /default_config.json /config/last_config.json

echo ""
echo ">>> CONST"
cat /exec/const.py

echo ""
echo ">>> CONFIG"
cat /config/last_config.json

echo ""
echo ">>> LET'S RUN"
python /exec/hvacws.py