var img_srcs = new Array([6])
var img_times =new Array([6])

function transfer(str0){
    var s = str0.split('/');
    var str = '/' + s[3] + '/' + s[4] + '/' +s[5];
    return str;
}

function flushimg(){
    $.ajax({
        url :'/img/get_imgs',
        type:'GET',
        dataType: 'json',
        success:function(data){         
            var obj = document.getElementById(1);
            var objtext = document.getElementById(11);
            var y = data.s1[data.s1.length-1];
            // 如果获取到的最新图片和第一张图不一样，则更新
            var src0 = transfer(String(obj.src));
            if(y.img != src0){      
                // 依次获取保存当前图片
                for(var i = 0;i<6;i++)
                {
                    var m = document.getElementById(String(i+1));
                    img_srcs[i] = transfer(String(m.src));
                    var n = document.getElementById(String(i+11));
                    img_times[i] = n.innerHTML;

                };
                // 重新设置src
                obj.src = y.img;
                objtext.innerHTML = y.time;
                for(var j = 0;j<5;j++)
                {
                    var m = document.getElementById(String(j+2));
                    m.src = img_srcs[j];
                    var n = document.getElementById(String(j+12));
                    n.innerHTML = img_times[j];
                };

                }
            }
    });
    
};

setInterval(flushimg, 1000*2);