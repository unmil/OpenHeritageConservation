<?php
include 'dbinfo.php';
$headerContent = "Status: 500 Server Error";
function my_error_handler()
{
    $last_error = error_get_last();
    if ($last_error && $last_error['type'] == E_ERROR) {
        header($headerContent);
        echo '...'; //html for 500 page
    }
}
register_shutdown_function('my_error_handler');
if (isset($_POST['data'])) {
    $insert_json = $_POST['data'];

try {
    $mongoClient = new MongoClient($url);
}
catch (Exception $exception) {
    header($headerContent);
    var_dump($excerption->getMessage());
}
$db         = $mongoClient->selectDB($db_name);
$collection = $db->selectCollection($walls_collection);
try {
    
    $queryArray = array(
        'name' => 'A'
    );
    
    $dataRetrieveQuery = $queryArray;
    $retrieveCursor    = $collection->find($dataRetrieveQuery);
    if ($retrieveCursor->count() > 0) {
        $retrieveCursor->next();
        $retrieveCursor = $retrieveCursor->current();
        $r_GeoJson      = $retrieveCursor['geoJSON'];
    } else {
        return false;
    }
}
catch (Exception $exception) {
    header($headerContent);
    var_dump($exception->getMessage());
}
$r_data           = json_decode($r_GeoJson);
$insert           = json_decode($insert_json);
if(!array_key_exists('type', $r_data)){
	$r_data->type='FeatureCollection';
}
$r_data->features = $insert->features;
$w_data_json      = json_encode($r_data);
try {
    $cursor = $collection->update(array(
        'name' => 'A'
    ), array(
        '$set' => array(
            'geoJSON' => $w_data_json
        )
    ));
    //  throw new Exception('error');
}
catch (Exception $exception) {
    header($headerContent);
    var_dump($exception->getMessage());
}
}
?>