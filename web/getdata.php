<?php
require_once 'database.php';
if ($_POST["mode"] === "1") {
    get_userdevice($_POST["user"]);
} else {
    get_devicedetail($_POST["device"]);
}
?>