/**
 * Created by junqingfjq on 16/1/6.
 */


document.write("<script language='javascript' src='http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js'></script>");
document.write("<script language='javascript' src='http://apps.bdimg.com/libs/bootstrap/3.3.0/js/bootstrap.min.js'></script>");

function goto(url){
    window.location=url;
}



function ajax_get(url,sucFun,errFun){

     $.ajax({
        url:url,
        type:'get',
        success:sucFun,
        error:errFun
    })
}