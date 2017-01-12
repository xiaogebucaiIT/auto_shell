#!/bin/bash

function FreeDisk()
{
	find /data/permdata/file/ftp/ -mtime +3 -type f -name "*" -exec rm -rf {} \;
	find /data/permdata/file/httpdown/ -mtime +3 -type f -name "*" -exec rm -rf {} \;
	find /data/permdata/file/webmail/ -mtime +3 -type f -name "*" -exec rm -rf {} \;
}


while((1))
do
	echo date
	FreeDisk
	sleep 1h
	echo date

done
