<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>LOG IN</title>
</head>
<body>
    <div align="center">
        <h2>Log in</h2>
            <form method="post" action="">
                <p><input type="text" name="usuario" placeholder="Nombre de usuario"></p>
                <p><input type="text" name="contrasena1" placeholder="Contraseña"></p>
                <p><input type="submit" value="Entrar"></p>
            </form>
        <h5><a href="mainfile.php">VOLVER AL INDEX</a></h5>

<?php
if($_POST){
    $usuario_login=$_POST["usuario"];
    $contrasena_login=$_POST["contrasena1"];

    //acceso a la tabla
    include_once "conection.php";
    $query_read='select * from usuarios_contrasenas';
    $sentence_read=$conection->prepare($query_read);
    $sentence_read->execute();
    $table=$sentence_read->fetchall();

    //comprobacion de usuario
    $coincide='no';
    foreach($table as $registro){
        //echo $registro['usuario'];
        if($registro['usuario']==$usuario_login){
            $uc=array($usuario_login,$registro['contrasena']);
    //        print_r($uc);
    //        echo '<br>';
            $coincide='si';
        }
        
    }
    echo "<hr>";
    
    if($coincide=='no'){
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
        //echo "<br>Contraseña correcta";
        session_start();
        $_SESSION['admin']=$usuario_login;
        echo "Bienvenido!";
    }else{
        echo "<br>Contraseña INCORRECTA";
    }
}
?>

    </div>
</body>
</html>
