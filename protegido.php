<?php
session_start();
?>

<?php if($_SESSION['admin']=='lautaro'):?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>PROTEGIDO</title>
</head>
<body>
    <?php echo "Acá está lo tuyo ".$_SESSION['admin']."<br>"?>
    <h2><a href="http://www.google.com">Google</a></h2>
    <h2><a href="http://www.youtube.com">Youtube</a></h2>
    <h2><a href="http://www.skrill.com">Skrill</a></h2>
    <h2><a href="http://www.paypal.com">Paypal</a></h2>
    <div align="center">
        <h5><a href="mainfile.php">VOLVER AL INDEX</a></h5>
    </div>
</body>
</html>
<?php endif;?>

<?php
//if(isset($_SESSION['admin'])){
//    echo "<br>";
//    //print_r($_SESSION);
//    echo "<br>Hola ".$_SESSION['admin'];
//}
?>