/*VkaZas Scroll List*/

(function($) {
    var defaultOption = {
        initOffset : '40',
        stepOffset : '50'
    };

    var VScrollList = function($list,$container,cb) {
        var self = this;
        this.container = $container.addClass("v-list-container");
        this.list = $($list).addClass("v-scroll-list");
        this.items = [];
        this.curItem = 0;
        this.option = defaultOption;
        this.callback = cb || null;
        var cnt = 0;

        $(this.list).children("li").each(function(){
            $(this).addClass("v-item").attr("item-index", cnt);
            self.items.push($(this));
            cnt++;
        });
        this.list.on("click", "li", function(){
           self.clickToActivate($(this).attr("item-index"));
        });
        document.onmousewheel = function(e) {
            self.scrollListStep(e)
        };

        this.initList();
        this.activateItem(0);
    };
    
    VScrollList.prototype = {
        constructor : VScrollList,
        activateItem : function(id) {
            $(this.items).each(function() {
                $(this).removeClass("active");
            });
            $(this.items[id]).addClass("active");
            if (!!this.callback) (this.callback)(this.curItem);
        },
        initList : function(id) {
            var midPos = $(this.container).height() / 2;
            $(this.list).css("top", midPos - this.option.initOffset);
        },
        scrollListStep : function(e, dir) {  // dir = 1 scroll to top, dir = -1 scroll to bottom
            dir = dir || 0;
            e = e || window.event;

            if (!!e.wheelDelta) {
                if (e.wheelDelta > 0) dir = -1;
                else dir = 1;
            }

            if (dir == -1 && (this.curItem == this.items.length - 1)) {
                return;
            } else if (dir == 1 && (this.curItem == 0)) {
                return;
            }

            var orgPos = $(this.list).offset().top;
            $(this.list).offset({top : orgPos + dir * this.option.stepOffset});
            // $(this.list).animate({
            //     top : "+=" + (dir * this.option.stepOffset)
            // }, 500);
            this.curItem += -dir;
            this.activateItem(this.curItem);
        },
        clickToActivate : function(id) {
            var offset = id - this.curItem;
            for (var i=0; i<Math.abs(offset); i++) {
                this.scrollListStep(null, -(offset / Math.abs(offset)))
            }
        }
    };


    $.fn.vscrolllist = function(cb) {
        return new VScrollList($(this), $(this).parent("div"), cb)
    }
})(jQuery);