#!/system/bin/sh
i=1
count=1000
while(($i<$count))
do
	for((j=1;j<=2;j++))
	do 
		{
		echo power
		input keyevent 26; sleep 1
		}&
	done
	wait
	input keyevent 26
	input keyevent 82
	# sleep 1
	input tap 402 510
	input tap 402 510
	# sleep 1
	input keyevent 3
	# sleep 1
	input keyevent 26
	sleep 0.5
	echo $i > times.txt
	i=$(($i+1))
done