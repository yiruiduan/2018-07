// 新建input标签
(function (arg) {
        arg.fn.extend({
        "newInput":function (value) {
            var new_input=document.createElement("input");
            new_input.setAttribute("type","text");
            $(new_input).val(value);
            return new_input;
        }
    })
})(jQuery);
// 新建select标签
(function (arg) {
    arg.fn.extend({
        "newSelect" : function (value) {
            var new_select=document.createElement("select");
            var new_option=document.createElement("option");
            var new_option1=document.createElement("option");
            new_option.text="上线";
            new_select.add(new_option);
            if(value=="上线"){
                new_option.setAttribute("selected","selected")
            };
            new_option1.text="下线";
            new_select.add(new_option1);
            if(value=="下线"){
                new_option1.setAttribute("selected","selected")
            };
            return new_select;
        }
    })
})(jQuery)