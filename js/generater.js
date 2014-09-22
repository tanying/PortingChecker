var count = 0;
var exist_count = 0;

window.requestFileSystem  = window.requestFileSystem || window.webkitRequestFileSystem;


$(function() {
    $('#addApk').bind('click', addApk);
    displayExistJsonOnDom(json);
});

function displayExistJsonOnDom(data){
    jsonObj = data;
    for(var key in jsonObj){
        addApkInnerHtml(count);

        attrObj = jsonObj[key];
        path = attrObj['path'];
        version = attrObj['versionName'];

        setInnerHtmlValue(count, key, path, version);
        count++;
    }
    exist_count = count;
    $('#addApk').after('<button id="generate">generate json</button>');
    $('#generate').bind('click', generateJson);
}

function changeArrayToJson(array){
    var jsonObj = {};
    var pkg = '';
    var path = '';
    var ver= '';

    $.each(array,function(n,value) {  
        mod = n%3;
        switch(mod){
            case 0: pkg = value;
            case 1: path = value;
            case 2: ver =value;
                    jsonObj[pkg] = {};
                    jsonObj[pkg]['path'] = path;
                    jsonObj[pkg]['versionName'] = ver;
        }
    });
    var data = JSON.stringify(jsonObj)
    displayJsonToDom(data);
}

function displayJsonToDom(data){
    $('body').empty();

    jsonObj = JSON.parse(data);
    var html = '{<br>'
    for(var key in jsonObj){
        html += '&nbsp;&nbsp;"' + key + '":{<br>';
        attrObj = jsonObj[key];
        path = attrObj['path'];
        version = attrObj['versionName'];
        html += '&nbsp;&nbsp;&nbsp;&nbsp;"path":"' + path + '",<br>'
        html += '&nbsp;&nbsp;&nbsp;&nbsp;"versionName":"' + version + '"<br>'
        html += '&nbsp;&nbsp;},<br>'
    }
    html = html.substring(0, html.length-5);
    html += '<br>'
    html += '}'

    $('body').append(html);
    // $('body').append('<button id="save">save</button>')
    // $('#save').bind('click', saveJson(data));

}

function compareString(s1, s2){
    console.log(s1,s2);
    return (s1 != s2) ? true : false;
}

function addApkInnerHtml(i){
    $('#apkInfo').append('<p id="apk'+i+'"></p>');
    $('#apk' + i).append('<div><label>Package name: </label><input id="pkg'+i+'" value="" maxlength="256"></div>');
    $('#apk' + i).append('<div><label>path:</label><input id="path'+i+'" value="" maxlength="256"></div>');
    $('#apk' + i).append('<div><label>version:</label><input id="version'+i+'" value="" maxlength="256"></div>');
}

function setInnerHtmlValue(i, pkg, path, version){
    $('#pkg' + i).attr('value', pkg);
    $('#path' + i).attr('value', path);
    $('#version' + i).attr('value', version);
}

function isEmptyObject(obj){
    for(var n in obj){return false} 
    return true; 
}

function addApk(){
    j = count - 1
    if(j >= 0){
        pkgname = $('#pkg' + j).val();
        path = ($('#path' + j).val());
        version = ($('#version' + j).val());
        if (pkgname && path && version){
            k = j - 1
            if(k >= 0){
                pre_pkgname = $('#pkg' + k).val();
                pre_path = ($('#path' + k).val());
                pre_version = ($('#version' + k).val());
                r1 = compareString(pkgname, pre_pkgname);
                r2 = compareString(path, pre_path);
                r3 = compareString(version, pre_version);
                if (r1 && r2 && r3){
                    setInnerHtmlValue(j, pkgname, path, version);
                    addApkInnerHtml(count);
                    count++;
                }
                else{
                    alert('Please input different content for different Package!');
                }
            }
            else{
                setInnerHtmlValue(j, pkgname, path, version);
                addApkInnerHtml(count);
                count++;
            }
        }
        else{
            alert('Please fill pkgname, path and version!');
        }
    }
    else{
            addApkInnerHtml(count);
            count++;

            $('#addApk').after('<button id="generate">generate json</button>')
            $('#generate').bind('click', generateJson);
    }
}

function generateJson(){
    var array = [];
    var isNormalQuit = true;
    $('input').each(function(){
        //key = $(this).attr('id');
        value = $(this).val();
        if(!value){
            alert('Please fill the value of ' + key);
            isNormalQuit = false;
            return false;
        }
        array.push(value);
    })

    if(isNormalQuit){
        result = confirm('Generate json now?')
        if (result){
            data = changeArrayToJson(array);
            alert ('Generation Successful!\n\nPress CTRL+A CTRL+C to copy the new json!');
        }
        else{
            return;
        }
    }
}