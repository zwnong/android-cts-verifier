#!/system/bin/sh
read -p 'input device_name:' device
read -p 'please enter Light screen waiting time:' lightscreen
read -p 'Please enter the test times:' count
i=1
while(($i<$count+1))
do
	echo =============================================================================================
	echo device:$device
	echo Total Accesses ：$count
	echo starting:$i
	echo rebooting,please wait-for-device 
	adb -s $device reboot
	adb -s $device wait-for-device
	sleep 25
	adb -s $device shell input keyevent 82
	adb -s $device shell input keyevent 82
	adb -s $device shell am start -n 'com.android.camera2/com.android.camera.CameraActivity'
	sleep 4
	adb -s $device shell input keyevent 27
	sleep 3
	adb -s $device shell input tap 600 1320
	sleep 3
	adb -s $device shell input keyevent 27
	sleep 3
	adb -s $device shell input keyevent KEYCODE_HOME
	sleep $lightscreen
	echo "Total Accesses:"$count",""it hava been run:" $i "times" >$device.txt
	i=$(($i+1))
	
done
echo finished
sleep 999999999999