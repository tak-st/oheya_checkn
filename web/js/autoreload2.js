$(function () {
    $('#reloadbtn').click(function () {
        $.ajax({
            url: "getdata.php",
            type: 'POST',
            data: {mode: 2, device: getParam('id')},
            timeout: 10000,
            dataType: 'text'
        }).done(function (data) {
            $("#showinfo").html(data);
        }).fail(function (data) {

        }).always(function (data) {

        });
    })
});

$(function () {
    setInterval(function () {
        if ($("#autoreload").prop("checked")) {
            $.ajax({
                url: "getdata.php",
                type: 'POST',
                data: {mode: 2, device: getParam('id')},
                timeout: 10000,
                dataType: 'text'
            }).done(function (data) {
                $("#showinfo").html(data);
            }).fail(function (data) {

            }).always(function (data) {

            });
        }
    }, 5000);
});

function getParam(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}