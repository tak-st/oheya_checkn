<?php
require_once 'database.php';
?>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>お部屋チェックン</title>
    <link rel="stylesheet" href="css/bootstrap.css">
    <script src="./js/jquery.js"></script>
    <script src="js/bootstrap.js"></script>
    <script src="js/autoreload2.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark p-2">
    <a class="navbar-brand" href="#">
        <img src="icon/oheyacheckn.png" width="32" height="32" alt="">
        お部屋チェックン
    </a>
    <ul class="navbar-nav mr-auto">
        <li class="nav-item">
            <a class="nav-link" href="index.php">ホーム</a>
        </li>
    </ul>
    <?php
    login_or_username();
    ?>

</nav>
<br>
<div class="container-fluid">
    <div class="text-right">
        <button id="reloadbtn" type="button" class="btn btn-outline-dark">更新</button>
        　
        <input id="autoreload" type="checkbox" class="custom-control-input" id="custom-check-1">
        <label class="custom-control-label" for="custom-check-1">自動更新</label>
    </div>
    <?php
    ?>
    <div id="showinfo" class="row">
        <?php
        get_devicedetail($_GET["id"])
        ?>
    </div>
</div>
</body>
</html>