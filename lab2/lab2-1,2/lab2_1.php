<?php
    header("Content-Type:text/html; charset=utf-8");
    /* Temp --> server */
    // ex: curl -d "sensor=1&Temp28.9" http://IP_addr
    $SensorID=$_POST[sensor];
    $Temperature=$_POST[Temp];
    $Humidity=$_POST[Humi];


    echo 'Temperature: '.$Temperature."\n".'Humidity: '.$Humidity."\n";

    $data_root_path = '/home/pi/2020-RPi-course/www-data/';
    
    $temp_filename = $data_root_path.'temp_'.$SensorID.'.txt';
    $humi_filename = $data_root_path.'humi_'.$SensorID.'.txt';

    $temp_file = fopen($temp_filename, 'w');
    $humi_file = fopen($humi_filename, 'w');


    fwrite($temp_file, $Temperature);
    fwrite($humi_file, $Humidity);

    fclose($temp_file);
    fclose($humi_file);

?>