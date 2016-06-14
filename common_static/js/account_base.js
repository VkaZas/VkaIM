/* vertical centering content-blk*/
$(function(){
    var $obj = $(".content-blk"), $obj_bg = $(".content-blk-bg");
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

$(function(){

});