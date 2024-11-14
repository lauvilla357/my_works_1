<?php
$usuario_login='lautaro8';
$contrasena_login='villas';

//acceso a la tabla
include_once "conection.php";
$query_read='select * from usuarios_contrasenas';
$sentence_read=$conection->prepare($query_read);
$sentence_read->execute();
$table=$sentence_read->fetchall();

//comprobacion de usuario
$coincide='no';
foreach($table as $registro){
    echo $registro['usuario'];
    if($registro['usuario']==$usuario_login){
        $uc=array($usuario_login,$registro['contrasena']);
//        print_r($uc);
//        echo '<br>';
        $coincide='si';
    }
    echo "<hr>";
}
if($coincide=='si'){
    echo "<br>Hay coincidencia en usuario";
}else{
    echo "<br>No hay coincidencia en usuario";
    exit();
}

//comprobado el usuario, se debe vrificar la contrasena
$contrasena_login_hash=password_hash($contrasena_login,PASSWORD_DEFAULT);
//echo "<br>";
//print_r($uc);
//echo "<br>".$uc[1];

if(password_verify($uc[1],$contrasena_login_hash)){
    //aca va el session_start y la variable $_SESSION
    echo "<br>Contraseña correcta";
}else{
    echo "<br>Contraseña INCORRECTA";
}