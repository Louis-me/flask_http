$(function(){
$("#btn_param").click(function(){
    p_param = $("#btn_param").parent().next()
   p_param.append(p_param.clone())
    })

    $("#btn_param_hope").click(function(){
    p_param = $("#btn_param_hope").parent().next()
    p_param.append(p_param.clone())
    })

})
