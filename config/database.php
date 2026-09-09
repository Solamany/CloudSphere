<?php
define('DB_HOST','localhost'); define('DB_NAME','cloudsphere_db'); define('DB_USER','root'); define('DB_PASS','');
function db(){ static $pdo=null; if(!$pdo){$pdo=new PDO("mysql:host=".DB_HOST.";dbname=".DB_NAME.";charset=utf8mb4",DB_USER,DB_PASS,[PDO::ATTR_ERRMODE=>PDO::ERRMODE_EXCEPTION]);} return $pdo; }
?>