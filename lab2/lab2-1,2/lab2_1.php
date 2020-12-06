<?php
    header("Content-Type:text/html; charset=utf-8");

    /* Temperature --> server */
    // ex: curl -d "sensor=1&Temp=28.9" http://IP_addr

    // get data from POST
    $SensorID=$_POST[sensor];
    $Temperature=$_POST[Temp];
    $Humidity=$_POST[Humi];

    // echo response to client
    echo 'Temperature: '.$Temperature."\n".'Humidity: '.$Humidity."\n";

    // data root folder
    $data_root_path = '/home/pi/2020-RPi-course/www-data/';
    
    // create filename according to $SensorID
    $temp_filename = $data_root_path.'temp_'.$SensorID.'.txt';
    $humi_filename = $data_root_path.'humi_'.$SensorID.'.txt';

    // open and write data to file
    $temp_file = fopen($temp_filename, 'w');
    $humi_file = fopen($humi_filename, 'w');

    fwrite($temp_file, $Temperature);
    fwrite($humi_file, $Humidity);

    fclose($temp_file);
    fclose($humi_file);
?>