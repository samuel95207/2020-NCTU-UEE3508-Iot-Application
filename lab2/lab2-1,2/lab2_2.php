<?php
    header("Content-Type:text/html; charset=utf-8");
    /* Temp --> server */
    // ex: curl -d "sensor=1&Temp28.9" http://IP_addr
    $Month=$_POST[Month];
    $Date=$_POST[Date];


    echo 'Month: '.$Month."\n".'Date: '.$Date."\n";

    $data_root_path = '/home/pi/2020-RPi-course/www-data/';
    
    $month_filename = $data_root_path.'Month.txt';
    $date_filename = $data_root_path.'Date.txt';

    $month_file = fopen($month_filename, 'w');
    $date_file = fopen($date_filename, 'w');


    fwrite($month_file, $Month);
    fwrite($date_file, $Date);

    fclose($month_file);
    fclose($date_file);

?>