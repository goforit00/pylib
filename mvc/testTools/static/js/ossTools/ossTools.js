/**
 * Created by junqingfjq on 16/1/14.
 */
//document.write("<script language='javascript' src='../base.js'></script>");

function donwloadLocation(type) {
    console.log(type)

    var params={};
    params["type"]=type;
    pstr=mapToStr(params);

    ajax_get("/subProject/downloadlocal/?"+pstr,
        function(data){
            console.log(data);
            alert("success")
        },
        function(){
            alert("failed")
        }
    )
}


function uploadOss(env,type){
    console.log(env);
    console.log(type);

    var params={}
    params["env"]=env;
    params["type"]=type;
    pstr=mapToStr(params);

    ajax_get(
            "/subProject/uploadOss/?"+pstr,
        function(data){
            console.log(data)
            alert("success")
//            if(data.msg=="true"){
//                console.log("success")
//            }else{
//                console.log("failed")
//            }
        },
    function(){
        alert("failed")
//        console.log("new error")
    })


    return "aa";
}





function mapToStr(params){
    var str="";
    for( item in params){
        str=str+"&"+item+"="+params[item]
    }
    str=str.substring(1)
    return str;
}