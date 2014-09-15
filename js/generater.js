i = 0

$(function() {

    $('#addApk').bind('click', addApk);
    $('#submit').bind('click', submit);
});

function addApk(){

    console.log($('#pkg' + i).attr('value'))
    $('#apkInfo').append('<p id="apk'+i+'">Package name: <input id="pkg'+i+'" value="" maxlength="256"></p>');
    $('#apk' + i).after('<span>path:<input value="" maxlength="256"></span><br><span>version:<input value="" maxlength="256"></span><br>');
    i++;
}

function submit(){

}
