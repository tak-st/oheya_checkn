$(function () {
    $('#reloadbtn').click(function () {
        $.ajax({
            url: "getdata.php",
            type: 'POST',
            data: {mode: "1", user: "100"},
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
                data: {mode: "1", user: "100"},
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