
<?php
function connect(): PDO
{
    require_once 'db_connectinfo.php';
    try {
        $pdo = get_pdo();
    } catch (PDOException $e) {
        echo "500";
        header('Content-Type: text/plain; charset=UTF-8', true, 500);
        exit($e->getMessage());
    }
    return $pdo;
}

function login_or_username()
{
    if (TRUE) {
        ?>
        <ul class="navbar-nav">
        <li class="nav-item">
            <?php
            echo "<span class=\"navbar-expand-lg nav-link\">ようこそ！" . get_username(100) . " さん　</span>"
            ?>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#">ログアウト</a>
        </li>
        <?php
    } else {
        ?>
        <ul class="navbar-nav">
        <li class="nav-item">
            <a class="nav-link" href="#">ログイン</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#">登録</a>
        </li>
        <?php
    }
    ?>
    </ul>
    <?php
}

function get_username($id)
{
    $pdo = connect();
    $stmt = $pdo->query("SELECT user_name FROM user WHERE user_id = $id");
    while ($row = $stmt->fetch()) {
        return $row['user_name'];
    }
}
function get_userdevice($id)
{
    $pdo = connect();
    $stmt = $pdo->query("SELECT * FROM user_device NATURAL JOIN device WHERE user_id = $id");
    while ($row = $stmt->fetch()) {
?>
        <div class="col-sm-6 col-lg-4">
            <div class="card h-100 mt-1">
                <div class="card-header">
                    <?php echo "<h5 class=\"card-title\"> $row[device_name] ($row[device_id])</h5>" ?>
                </div>
                <div class="card-body">
                    <?php echo "<p class=\"card-text\">" . get_devicedisp($row[device_id]) . "<br>最終更新時刻 : ". get_lastUpdated($row[device_id]) . "</p>";
                    get_graph($row[device_id],$row[favorite_sensor],$row[show_num]);
                    ?><br>
                    <a href="detail.php?id=<?php echo $row[device_id]  ?>" class="btn btn-primary">詳細</a>
                </div>
            </div>
        </div>
<?php
    }
}
function get_devicedisp($device_id){
    $pdo = connect();
    $str = "";
    $stmt = $pdo->query("SELECT sensor_id,sensor_type,sensor_unit FROM device NATURAL JOIN sensor WHERE device_id = $device_id  GROUP BY sensor_id");
    while ($row = $stmt->fetch()) {
        $d2 = $pdo->query("SELECT sensor_data,time FROM device_data WHERE device_id = $device_id AND sensor_id = $row[sensor_id] ORDER BY time DESC limit 1");
        while ($row2 = $d2->fetch()){
            if($row[sensor_type] != "Latitude" and $row[sensor_type] != "Longitude" ){}
                $str = $str . Localize($row[sensor_type],"ja-jp") . " " . $row2[sensor_data] . $row[sensor_unit] . "　";
            }
        }
    return $str;
}
function get_lastUpdated($device_id){
    $pdo = connect();
    $stmt = $pdo->query("SELECT time FROM device_data WHERE device_id = $device_id ORDER BY time DESC limit 1");
    while ($row = $stmt->fetch()) {
        return $row[time];
    }
}
function get_lastUpdated_sensor($device_id,$sensor_id){
    $pdo = connect();
    $stmt = $pdo->query("SELECT time FROM device_data WHERE device_id = $device_id AND sensor_id = $sensor_id  ORDER BY time DESC limit 1");
    while ($row = $stmt->fetch()) {
        return $row[time];
    }
}
function get_graph($device_id,$sensor_id,$data_num){
    ?>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
<?php
    $pdo = connect();
    $stmt = $pdo->query("SELECT sensor_data,time,sensor_type FROM device_data NATURAL JOIN sensor WHERE device_id = $device_id AND sensor_id = $sensor_id ORDER BY time DESC limit $data_num");
    $x_data = array();
    $glabel = array();
    $type = "";
    while ($row = $stmt->fetch()) {
        $glabel[] =  "\"" . $row[time] . "\"";
       $x_data[] = $row[sensor_data];
       $type = $row[sensor_type];
    }
    ?>
    <canvas id="myChart<?php echo $device_id . $sensor_id ?>"></canvas>
<script>
    var ctx = document.getElementById("myChart<?php echo $device_id . $sensor_id ?>").getContext("2d");
var chart = new Chart(ctx, {
  type: "line",
  data:{
    labels: [<?php echo implode( ", ", $glabel ) ?>],
    datasets: [{
        label:"<?php echo Localize($type,"ja-jp") ?>",
        data:[<?php echo implode( ", ", $x_data ) ?>],"fill":true,"borderColor":"rgb(75, 192, 192)","lineTension":0.2,pointHitRadius: 60
    }]
  },
  options:{
      scales: {
      xAxes: [
        //y軸
        {
        display: false
        }
      ]},
    legend: {
      //凡例
      display: false,
    },
    animation: {
      duration: 0,
    },
  }
});
</script>
    <?php
}
function get_devicedetail($device_id){
    $pdo = connect();
    $stmt = $pdo->query("SELECT * FROM device WHERE device_id = $device_id");
        while ($row = $stmt->fetch()) {
            echo "<div class=\"page-header\"> <h1>". $row[device_name]  ."　<small class=\"text-muted\">id:". $row[device_id]  ."</small></h1></div>";
        }
        $d1 = $pdo->query("SELECT sensor_id,sensor_type,sensor_unit FROM device NATURAL JOIN sensor WHERE device_id = $device_id  GROUP BY sensor_id");
    while ($row1 = $d1->fetch()) {
        $d2 = $pdo->query("SELECT sensor_data,time FROM device_data WHERE device_id = $device_id AND sensor_id = $row1[sensor_id] ORDER BY time DESC limit 1");
        while ($row2 = $d2->fetch()){
            if($row1[sensor_type] != "Latitude" and $row1[sensor_type] != "Longitude" ){
                ?>
        <div class="col-sm-6 col-lg-4">
            <div class="card h-100 mt-1">
                <div class="card-header">
                    <?php echo "<h5 class=\"card-title\">" . Localize($row1[sensor_type],"ja-jp") . " " . $row2[sensor_data] . $row1[sensor_unit]." </h5>" ?>
                </div>
                <div class="card-body">
                    <?php echo "<p class=\"card-text\">最終更新時刻 : ". get_lastUpdated_sensor($device_id,$row1[sensor_id]) . "</p>";
                    get_graph($device_id,$row1[sensor_id],100);
                    ?>
                </div>
            </div>
        </div>
<?php
            }
        }
}
}
function Localize($str,$language){
    if($language === "ja-jp"){
        if($str === "Temperature") return "温度";
        if($str === "Humid") return "湿度";
        if($str === "Latitude") return "緯度";
        if($str === "Longitude") return "経度";
        if($str === "CO2") return "CO2";
        if($str === "Dust") return "ほこり";
        if($str === "Gas") return "空気汚染";
    }
        return $str;

}