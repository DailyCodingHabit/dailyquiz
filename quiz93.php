<?php

$pattern = "/[\s,]+/";
$text = "Daily Coding Habit";
$daily = preg_split($pattern, $text);
$pattern = "/\bi*/im";

foreach($daily as $part){
    echo preg_match_all($pattern, $part); 
}

