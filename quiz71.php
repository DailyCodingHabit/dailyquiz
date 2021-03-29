<?php


$daily = count("123","2");
$array = [
    'foo' => ['bar1', 'bar2'],
    'john' => ['doe1', 'doe1']
];
$coding = count($array);
$habit = count($array,1);
echo $daily.$coding.$habit;