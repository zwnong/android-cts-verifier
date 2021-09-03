#!/system/bin/sh
read -p 'input device_name:' device
read -p 'please Enter the waiting time after the screen is off:' screenoff
read -p 'please enter Light screen waiting time:' lightscreen
read -p 'Please enter the test times:' count
i=1
while(($i<$count+1))
do
	x=$[RANDOM%700+1]
	y=$[RANDOM%1000+1]
	echo =============================================================================================
	echo device:$device
	echo Total Accesses ：$count
	echo starting:$i
	adb -s $device shell input keyevent 26
	adb -s $device shell input keyevent 82
	adb -s $device shell input swipe 350 1300 350 150
	adb -s $device shell input tap $x $y
	adb -s $device shell input tap $x $y
	adb -s $device shell input keyevent 3
	sleep $lightscreen
	adb -s $device shell input keyevent 26
	sleep $screenoff
	echo "Total Accesses:"$count",""it hava been run:" $i "times" >$device.txt
	i=$(($i+1))
	
done
echo finished
sleep 999999999999