<?
$uid=$_GET['uid'];
$jump="location: ./c.php?uid=".$uid;
header($jump);
?>