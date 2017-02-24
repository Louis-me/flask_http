$(function(){
//   //使用id选择器;例如:tab对象->tr->td对象.
//    $("#moudle tbody tr td").each(function(i){
//         //获取td当前对象的文本,如果长度大于25;
//         if($(this).text().length>25){
//                //给td设置title属性,并且设置td的完整值.给title属性.
//    $(this).attr("title",$(this).text());
//                //获取td的值,进行截取。赋值给text变量保存.
//    var text=$(this).text().substring(0,25)+"...";
//                //重新为td赋值;
//                $(this).text(text);
//         }
//      });
 $(".del").click(function(){
  //var user8ID = $.trim( $('#user8ID').val() );
  var statu = confirm("确定要删除吗?");
  if(!statu){
   return false;
  }
  $.ajax({
    type:'POST',
    url:'/del_api',
    data:'id='+$(this).parents("tr").attr("id"),
    success:function(data){
      if(data["msg"] == 1){
       alert( 'Delete Successful!' );
       location.reload();
      }else{
       alert( 'Delete Failed!' );
      }
      location.reload() ;
    },
    error:function(){
      alert( 'Delete Failed!' );
    }
   });
 })


})