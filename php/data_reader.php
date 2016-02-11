<?php
	require 'dbinfo.php';
	require 'mongoDButility.php';
	$queryArrary=Array('name' => 'A');
	$retrieveCursor=selectQuery($url,$db_name,$walls_collection,$queryArrary);
	$selectFields='geoJSON';
	if ($retrieveCursor->count() > 0) {
        $retrieveCursor->next();
        $retrieveCursor = $retrieveCursor->current();
        $r_GeoJson      = $retrieveCursor[$selectFields];
    } else {
        return false;
    }
    

echo $r_GeoJson;
?>