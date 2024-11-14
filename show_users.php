<?php
//conexion a base de datos
include_once "conection.php";
?>

<?php
//session_start();
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>USUARIOS REGISTRADOS</title>
</head>
<body>
    <div>

<?php
    $query='select * from usuarios_contrasenas';
    $sent=$conection->prepare($query);
    $sent->execute();
    $table=$sent->fetchall();
?>
        
    <?php foreach($table as $registro):?>
        <?php foreach($registro as $key=>$value):?>
            <?php if(!is_numeric($key)):?>
                <?php echo $key." : ".$value;?><br>
            <?php endif;?>
        <?php endforeach;?>
        <?php echo "<br>";?>
    <?php endforeach;?>
        
    <h5><a href="mainfile.php">VOLVER AL INDEX</a></h5>
    </div>
</body>
</html>

<?php
//if(isset($_SESSION['admin'])){
//    echo "<p>EFECTIVAMENTE, SESSION VIAJA A TODAS PARTES UNA VEZ CREADO, SI ESTA EL SESSION_START COLOCADO XD.</p>";
//}
?>

