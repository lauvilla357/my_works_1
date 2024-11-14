<?php
session_start();
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>MAINFILE</title>
</head>
<body>
    <?php if(isset($_SESSION['admin'])):?>
    <?php echo "Bienvenido ".$_SESSION['admin'];?>
    <?php endif;?>
    <h2><a href="add_user.php">Registrar usuario</a></h2>
    <h2><a href="login.php">Iniciar sesion</a></h2>
    <?php if($_SESSION):?>
    <h2><a href="protegido.php">IR A CONTENIDO PROTEGIDO</a></h2>
    <?php endif;?>
    <h2><a href="cerrar_sesion.php">Cerrar sesión</a></h2>
    <div align="center"><h5><a href="show_users.php">VER BASE DE DATOS DE USUARIOS</a></h5></div>
</body>
</html>

<?php
//if(isset($_SESSION['admin'])){
//    echo "<p>EFECTIVAMENTE, SESSION VIAJA A TODAS PARTES UNA VEZ CREADO.</p>";
//}
?>