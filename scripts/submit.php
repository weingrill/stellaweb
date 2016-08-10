/* source http://stackoverflow.com/questions/11320796/saving-json-string-to-mysql-database */

include("config.php");

/* create a connection */
$dbconn = pg_connect($connect_string)
  or die("Error: Unable to open database");


/* let's say we're grabbing this from an HTTP GET or HTTP POST variable called jsonGiven... */
$jsonString = $_REQUEST['jsonGiven'];

/* but for the sake of an example let's just set the string here */
$jsonString = '{"name":"jack","school":"colorado state","city":"NJ","id":null}';

/* use json_decode to create an array from json */
$jsonArray = json_decode($jsonString, true);

/* create a prepared statement */
$sql = "INSERT INTO aa (field1, field2) VALUES (1, '$jsonArray')";
if ($stmt = $mysqli->prepare('INSERT INTO test131 (name, school, city, id) VALUES (?,?,?,?)')) {

    /* bind parameters for markers */
    $stmt->bind_param("ssss", $jsonArray['name'], $jsonArray['school'], $jsonArray['city'], $jsonArray['id']);

    /* execute query */
    $stmt->execute();

    /* close statement */
    $stmt->close();
}

/* close connection */
pg_close($dbconn);
