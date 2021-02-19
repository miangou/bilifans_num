<?
$uid=$_GET['uid'];
$command="bilifans_num.exe " . $uid ;
exec($command,$list);
?>