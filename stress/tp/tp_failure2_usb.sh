#!/system/bin/sh
read -p 'input device_name:' device
read -p 'please Enter the waiting time after the screen is off:' screenoff
read -p 'please enter Light screen waiting time:' lightscreen
read -p 'Please enter the test times:' count
i=1
while(($i<$count+1))
do
	echo ----------------------------------------------
	echo $device starting:$i
	for((j=1;j<=2;j++))
	do 
		{
		echo power
		adb -s $device shell input keyevent 26; sleep 1
		}&
	done
	wait
	adb -s $device shell input keyevent 26
	adb -s $device shell input keyevent 82
	# sleep 1
	adb -s $device shell input tap 402 510
	adb -s $device shell input tap 402 510
	# sleep 1
	adb -s $device shell input keyevent 3
	sleep $lightscreen
	adb -s $device shell input keyevent 26
	sleep $screenoff
	echo "it hava been run:" $i "times" >$device.txt
	i=$(($i+1))
done
echo finished
sleep 99999999999999