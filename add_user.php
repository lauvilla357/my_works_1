<?php
//conexion a base de datos
include_once "conection.php";
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>REGISTRO</title>
</head>
<body>
    <div align="center">
    <h2>Registro</h2>
    <form method="post">
        <p><input type="text" name="usuario" placeholder="Nombre de usuario"></p>
        <p><input type="text" name="contrasena1" placeholder="Contraseña"></p>
        <p><input type="text" name="contrasena2" placeholder="Repetir contraseña"></p>
        <p><button type="submit_newuser">Registrar</button></p>
    </form>
    </div>
    <h5><a href="mainfile.php">VOLVER AL INDEX</a></h5>
</body>
</html>

<?php
if($_POST){
    $usuario=$_POST['usuario'];
    $contrasena1=$_POST['contrasena1'];
    $contrasena2=$_POST['contrasena2'];
    //ver que el usuario no exista aun
    $query='select * from usuarios_contrasenas';
    $sent=$conection->prepare($query);
    $sent->execute();
    $table=$sent->fetchall();
    $coincide="no";
    foreach($table as $registro){
        if($registro[1]==$usuario){
            $coincide="si";}}
    if($coincide=="no"){ 
        //verificacion de contraseña
        $contrasena1=password_hash($contrasena1,PASSWORD_DEFAULT);
        if(password_verify($contrasena2,$contrasena1)){
            //adeción a base de datos
            // asi no >>> $query_add_user="insert into usuarios_contrasenas (usuario,contrasena) values (?,?)";
            $query_add_user='insert into usuarios_contrasenas (usuario, contrasena) values ("'.$usuario.'","'.$contrasena2.'")';  // <<<<< ASI SI!
            $sent_add_user=$conection->prepare($query_add_user);
            $sent_add_user->execute();
            echo "<div align='center'>USUARIO REGISTRADO</div>";
            //resetar variables criticas
            $sent=null;
            $sent_add_user=null;
            $conection=null;
        }else{
            echo "<div align='center'>LAS CONTRASEÑAS NO COINCIDEN</div>";
        }
    }else{
        echo "<div align='center'>EL USUARIO YA EXISTE</div>";
    }
}
?>