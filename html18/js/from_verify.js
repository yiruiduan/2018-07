// 错误信息
function errorMessage(obj,msg){
    var new_span=document.createElement("span");
    $(new_span).css("color","red");
    $(new_span).css("margin-left","15px");
    $(new_span).text(msg);
    $(obj).parent().append(new_span)
}

$(".pg form [value='提交']").click(function () {
    var flag= true;
    $(this).parent().find("span").remove();

    $(this).siblings(".body_right").find("input").each(function () {
        // 验证是否为空
        var require = $(this).attr("require");
        if(require== "true"){
            var value=$(this).val();
            value=value.trim();
            if(value.length==0){
                flag=false;
                errorMessage(this,"*必填项");
                return false;
            };
        };
        // 验证字符串长度在4-40
        var range=$(this).attr("range");
        if(range){
            var value=$(this).val();
            var range_start=range.split('-')[0];
            var range_end=range.split('-')[1];
            value=value.trim();
            if(value.length<range_start||value.length>range_end){
                flag=false;
                errorMessage(this,'*用户名范围是'+range_start+'-'+range_end+'之间');
                return false;
            };
        };
        // 验证用户名由字母数字下划线组成
        var format=$(this).attr("format");
        if(format){
            var value=$(this).val();
            value=value.trim();
            var rep=/^\w*$/;
            if(!rep.test(value)){
                flag=false;
                errorMessage(this,'*用户名由字母数字下划线组成');
                return false;
            };
        };
        // 验证电话号码
        var format_tel=$(this).attr("format_tel");
        if(format_tel){
            var value=$(this).val();
            value=value.trim();
            var rep=/^1[34578]\d{9}$/;
            if(!rep.test(value)){
                flag=false;
                errorMessage(this,'*输入的手机号码有误');
                return false;
            };
        };
        // 验证邮箱
        var format_mail=$(this).attr("format_mail");
        if(format_mail){
            var value=$(this).val();
            value=value.trim();
            var rep=/^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
            if(!rep.test(value)){
                flag=false;
                errorMessage(this,'*输入的邮箱有误');
                return false;
            };
        };
        // 两次密码一致性验证
        var checkpassword_to=$(this).attr("checkpassword_to");
        if(checkpassword_to){
            var value=$(this).val();
            var value_old=$(this).parent().siblings().find("[name='password']").val();
            if(value!=value_old){
                flag=false;
                errorMessage(this,'*您两次输入的密码不一致');
                return false;
            };
        };


    });

    return flag;
});