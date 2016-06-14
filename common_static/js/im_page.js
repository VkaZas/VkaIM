/*vertical centering im-content-blk*/
$(function(){
    var $obj = $(".im-content-blk"), $obj_bg = $(".im-content-blk-bg");
    var clientHeight = $(document.body).height();
    var clientWidth = $(document.body).width();
    var selfHeight = $obj.height();
    var selfWidth = $obj.width();
    $obj.css({
        "top" : (clientHeight - selfHeight) / 2,
        "left" : (clientWidth - selfWidth) / 2
    });
    $obj_bg.css({
        "top" : (clientHeight - selfHeight) / 2,
        "left" : (clientWidth - selfWidth) / 2
    });
});