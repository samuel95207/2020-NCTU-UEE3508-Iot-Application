<?php
    header("Content-Type:text/html; charset=utf-8");

    /* Month & Date --> server */
    // ex: curl -d "Month=12&Date=31" http://IP_addr

    // get data from POST
    $Month=$_POST[Month];
    $Date=$_POST[Date];

    // echo response to client
    echo 'Month: '.$Month."\n".'Date: '.$Date."\n";

    // data root folder
    $data_root_path = '/home/pi/2020-RPi-course/www-data/';
    
    // filenames
    $month_filename = $data_root_path.'Month.txt';
    $date_filename = $data_root_path.'Date.txt';

    // open and write data to file
    $month_file = fopen($month_filename, 'w');
    $date_file = fopen($date_filename, 'w');

    fwrite($month_file, $Month);
    fwrite($date_file, $Date);

    fclose($month_file);
    fclose($date_file);
?>