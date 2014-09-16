i = 0

$(function() {
    $('#addApk').bind('click', addApk);
});

function addApk(){
    j = i - 1
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
                    addApkInnerHtml(i);
                    i++;
                }
                else{
                    alert('Please input different content for different Package!');
                }
            }
            else{
                setInnerHtmlValue(j, pkgname, path, version);
                addApkInnerHtml(i);
                i++;
            }
        }
        else{
            alert('Please fill pkgname, path and version!');
        }
    }
    else{
            addApkInnerHtml(i);
            i++;

            $('#addApk').after('<button id="generate">generate json</button>')
            $('#generate').bind('click', generateJson);
    }
}

function generateJson(){
    var array = [];
    var isNormalQuit = true;
    $('input').each(function(){
        key = $(this).attr('id');
        value = $(this).val();
        if(!value){
            alert('Please fill the value of ' + key);
            isNormalQuit = false;
            return false;
        }
        array.push([key, value]);
    })

    if(isNormalQuit){
        var filename = prompt('Please input filename:', '3rd.json');
    }
    else{
        window.requestFileSystem(window.TEMPORARY, 1024*1024, onInitFs, errorHandler);
    }
}

function changeArrayToJson(array){

}

function compareString(s1, s2){
    console.log(s1,s2);
    return (s1 != s2) ? true : false;
}

function addApkInnerHtml(i){
    $('#apkInfo').append('<p id="apk'+i+'">Package name: <input id="pkg'+i+'" value="" maxlength="256"></p>');
    $('#pkg' + i).after('<br>path:<input id="path'+i+'" value="" maxlength="256">')
    $('#path' + i).after('<br>version:<input id="version'+i+'" value="" maxlength="256">');
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


function onInitFs(fs) {

  fs.root.getFile('log.txt', {create: true}, function(fileEntry) {

    // Create a FileWriter object for our FileEntry (log.txt).
    fileEntry.createWriter(function(fileWriter) {

      fileWriter.onwriteend = function(e) {
        console.log('Write completed.');
      };

      fileWriter.onerror = function(e) {
        console.log('Write failed: ' + e.toString());
      };

      // Create a new Blob and write it to log.txt.
      var bb = new BlobBuilder(); 
     // Note: window.WebKitBlobBuilder.
      bb.append('Meow');
      
      fileWriter.write(bb.getBlob('text/plain'));

    }, errorHandler);

  }, errorHandler);

}