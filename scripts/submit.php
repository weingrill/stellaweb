<!DOCTYPE html>
/*
JSON ingestor for wifsippressure
2016 (c) Joerg Weingrill <jweingrill@aip.de>
 */
<HTML>
<HEAD>
<TITLE>WiFSIP JSON ingestor</TITLE>
<META NAME="author" CONTENT="Joerg Weingrill">
<META HTTP-EQUIV="Reply-to" CONTENT="jweingrill@aip.de">
</HEAD>

<BODY bgcolor=white link=black vlink=black text=black>
<center>
<h1>WiFSIP JSON ingestor</h1>

<?php

include("config.php");

/* create a connection */
$dbconn = pg_connect("$host $port $dbname $credentials")
  or die("Error: Unable to open database");
echo "database connected";

/* let's say we're grabbing this from an HTTP GET or HTTP POST variable called jsonData... */
/* $jsonString = $_REQUEST['jsonData']; */
$jsonString = file_get_contents('php://input');

/* but for the sake of an example let's just set the string here

$jsonString = '{"timestamp":"20160812 07:10:22","counts":"483","volts":"2.358398","mbar":"1.189037e-05"}';

/* use json_decode to create an array from json */
$jsonArray = json_decode($jsonString, true);

/* insert data */
$res = pg_insert($dbconn, 'wifsippressure', $jsonArray)
  or die("wrong input parameters");
echo "data inserted";

/* close connection */
pg_close($dbconn);
echo "database closed";

?>

<font size='-1'>
2016 (c) jweingrill AIP
</font>
</center></BODY></HTML>
