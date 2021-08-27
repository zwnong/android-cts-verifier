#!/system/bin/sh
i=1
count=1000
while(($i<$count))
do
	input keyevent 26
	input keyevent 82
	input tap 402 510
	input tap 402 510
	input keyevent 3
	input keyevent 26
	cat $i > times.txt
	i=$(($i+1))
done