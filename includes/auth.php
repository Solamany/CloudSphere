<?php
if(session_status()===PHP_SESSION_NONE) session_start();
function require_login(){if(empty($_SESSION['user'])){header('Location: login.php');exit;}}
?>