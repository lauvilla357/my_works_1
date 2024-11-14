<?php
//Conection to dbname:new_db with PDO
$dbname='new_db';
$link_conection='mysql:host=localhost;dbname='.$dbname;
$user_conection='root';
$pass_conection='';
try{
    $conection=new PDO($link_conection,$user_conection,$pass_conection);
    //echo 'Conection to db:'.$dbname.' success!';
}catch(PDOException $e){
    echo "Wrong!".$e->getMessage()."<br/>";
}
?>