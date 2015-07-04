(function($) {
    "use strict";

    function ot_Slider_move(itemid) {
        var thisel = itemid,
            currentb = thisel.parent().parent().children(".ot-slides").children(".ot-slide").eq(thisel.index());
        thisel.addClass("active").siblings("a").removeClass("active");
        currentb.addClass("active").siblings(".ot-slide").removeClass("active");
        thisel.parent().parent().css("height", currentb.attr("rel") + "px");
    }

    var sliderwidth = 0;


    jQuery(document).scroll(function() {
        var position = jQuery(window).scrollTop();

        if (position >= jQuery('.header #main-menu.thisisfixed').attr("rel")) {
            jQuery('.header #main-menu.thisisfixed').addClass("floatingmainmenu");
        } else {
            jQuery('.header #main-menu.thisisfixed').removeClass("floatingmainmenu");
        }
    });

    jQuery(window).resize(function() {
        var difference = (100 / sliderwidth * jQuery(".ot-slider").width()) / 100;
        jQuery(".ot-slider .ot-slides .ot-slide-overlay").css("zoom", difference);


        jQuery(".ot-slider .ot-slide").each(function() {
            var thisel = jQuery(this);

            jQuery(thisel).find("img").one('load', function() {
                thisel.attr("rel", thisel.height());
                jQuery(".ot-slider").each(function() {
                    var thisel = jQuery(this),
                        curel = thisel.find(".ot-slides").children(".ot-slide").eq(0);
                    thisel.find(".ot-slider-thumbs").children("a").eq(0).addClass("active");
                    curel.addClass("active");
                    thisel.css("height", curel.attr("rel") + "px");
                });
            }).each(function() {
                if (this.complete) {
                    jQuery(this).load();
                }
            });
        });
    });

    jQuery(window).ready(function() {
        jQuery('.ajax-popup-link').magnificPopup({
            type: 'ajax'
        });


        // jQuery(".article-double-side .item").mouseenter(function(event) {
        //     var id;
        //     id = jQuery(this).attr("data-id");
        //     console.log(id);
        //     jQuery(".article-double-main").addClass('hidden');
        //     jQuery(".article-double-main[data-id=" + id + "]").removeClass('hidden')
        // });

        jQuery("body").append("<div class='menu-block'></div>");


        jQuery('.header #main-menu.thisisfixed').each(function() {
            var thiselement = jQuery(this);
            jQuery(this).children(".wrapper").wrap("<div class='subset'></div>");
            if (!thiselement.hasClass("thisisfloat")) {
                thiselement.attr("rel", thiselement.offset().top);
            }
        });

        jQuery("#main-menu .wrapper").prepend("<a href='#' class='menu-dropy'><i class='fa fa-align-justify'></i>&nbsp;&nbsp;Toggle menu</a>");

        jQuery(".menu-dropy").click(function() {
            var thisel = jQuery(this).siblings("ul");
            thisel.toggle();
            return false;
        });

        jQuery("#main-menu .wrapper > ul > li.overlay").hover(function() {
            jQuery(".boxed.active .header .header-topmenu").css("z-index", "0");
            jQuery(".menu-overlay").fadeIn(200);
        }).mouseleave(function() {
            jQuery(".menu-overlay").fadeOut(200);
            jQuery(".boxed.active .header .header-topmenu").css("z-index", "1002");
        });




        jQuery("a[href=#open-jumplist]").click(function() {
            jQuery(".ot-jumplist").addClass("active");
            return false;
        });

        jQuery("a[href=#close-jumplist]").click(function() {
            jQuery(".ot-jumplist").removeClass("active");
            return false;
        });

        jQuery(".ot-slider .ot-slide").each(function() {
            var difference = (100 / sliderwidth * jQuery(".ot-slider").width()) / 100,
                thisel = jQuery(this);
            jQuery(".ot-slider .ot-slides .ot-slide-overlay").css("zoom", difference);


            // sliderwidth = thisel.width();
            sliderwidth = 1200;

            jQuery(thisel).find("img").one('load', function() {
                thisel.attr("rel", thisel.height());
                jQuery(".ot-slider").each(function() {
                    var thisel = jQuery(this),
                        curel = thisel.find(".ot-slides").children(".ot-slide").eq(0);
                    thisel.find(".ot-slider-thumbs").children("a").eq(0).addClass("active");
                    curel.addClass("active");
                    thisel.css("height", curel.attr("rel") + "px");
                });
            }).each(function() {
                if (this.complete) {
                    jQuery(this).load();
                }
            });
        });


        jQuery(".ot-slider-thumbs a").click(function() {
            ot_Slider_move(jQuery(this));
            return false;
        });

        jQuery(".ot-slider .page-move.move-left").click(function() {
            var thisel = jQuery(this).parent(),
                nextind = thisel.find(".ot-slider-thumbs").children("a.active");
            if (nextind.prev().index() >= 0) {
                ot_Slider_move(nextind.prev());
            } else {
                ot_Slider_move(nextind.parent().children("a").last());
            }
            return false;
        });

        jQuery(".ot-slider .page-move.move-right").click(function() {
            var thisel = jQuery(this).parent(),
                nextind = thisel.find(".ot-slider-thumbs").children("a.active");
            if (nextind.next().index() >= 0) {
                ot_Slider_move(nextind.next());
            } else {
                ot_Slider_move(nextind.parent().children("a").eq(0));
            }
            return false;
        });


        jQuery("#main-menu .big-drop-2").each(function() {
            jQuery(this).find("ul.sub-menu > li > ul > li").eq(0).addClass("active");
        });

        jQuery("#main-menu .big-drop-2 > ul.sub-menu > li > ul > li > a").click(function() {
            var thisel = jQuery(this).parent(),
                thisindex = thisel.index();
            thisel.addClass("active").siblings("li").removeClass("active");
            jQuery("#main-menu .big-drop-2 > ul.sub-menu > li > ul.sub-menu").each(function() {
                var thisel = jQuery(this);
                thisel.css("height", thisel.find("li.active .menu-content-inner").height());
            });
            return false;
        });


        jQuery("#main-menu .big-drop-2").hover(function() {
            jQuery("#main-menu .big-drop-2 > ul.sub-menu > li > ul.sub-menu").each(function() {
                var thisel = jQuery(this);
                thisel.css("height", thisel.find("li.active .menu-content-inner").height());
            });
        });


        // Alert box close
        jQuery('a[href="#close-alert"]').click(function() {
            jQuery(this).parent().animate({
                opacity: 0,
                padding: "0px 13px",
                margin: "0px",
                height: "0px"
            }, 300, function() {
                // Animation complete.
            });
            return false;
        });

        // Accordion blocks
        jQuery(".accordion > div > a").click(function() {
            var thisel = jQuery(this).parent();
            if (thisel.hasClass("active")) {
                thisel.removeClass("active").children("div").animate({
                    "height": "toggle",
                    "opacity": "toggle",
                    "padding-top": "toggle"
                }, 300);
                return false;
            }
            // thisel.siblings("div").removeClass("active");
            thisel.siblings("div").each(function() {
                var tz = jQuery(this);
                if (tz.hasClass("active")) {
                    tz.removeClass("active").children("div").animate({
                        "height": "toggle",
                        "opacity": "toggle",
                        "padding-top": "toggle"
                    }, 300);
                }
            });
            // thisel.addClass("active");
            thisel.addClass("active").children("div").animate({
                "height": "toggle",
                "opacity": "toggle",
                "padding-top": "toggle"
            }, 300);
            return false;
        });


        // Tabbed blocks
        jQuery(".short-tabs").each(function() {
            var thisel = jQuery(this);
            thisel.children("div").eq(0).addClass("active");
            thisel.children("ul").children("li").eq(0).addClass("active");
        });

        jQuery(".short-tabs > ul > li a").click(function() {
            var thisel = jQuery(this).parent();
            thisel.siblings(".active").removeClass("active");
            thisel.addClass("active");
            thisel.parent().siblings("div.active").removeClass("active");
            thisel.parent().siblings("div").eq(thisel.index()).addClass("active");
            return false;
        });

        jQuery(".lightbox").click(function() {
            jQuery(".lightbox").css('overflow', 'hidden');
            jQuery("body").css('overflow', 'auto');
            jQuery(".lightbox .lightcontent").fadeOut('fast');
            jQuery(".lightbox").fadeOut('slow');
        }).children().click(function(e) {
            return false;
        });



        jQuery("a[href='#font-size-up']").click(function() {
            var cursize = jQuery('.f-size-number').html();
            if (parseInt(cursize) < 24) {
                jQuery('.f-size-number').html(parseInt(cursize) + 2);
                jQuery('.main-article p').css("font-size", (parseInt(cursize) + 2) + "px");
            }
            return false;
        });

        jQuery("a[href='#font-size-down']").click(function() {
            var cursize = jQuery('.f-size-number').html();
            if (parseInt(cursize) > 16) {
                jQuery('.f-size-number').html(parseInt(cursize) - 2);
                jQuery('.main-article p').css("font-size", (parseInt(cursize) - 2) + "px");
            }
            return false;
        });



        jQuery(window).scroll(function() {
            jQuery('.ot-star-rating').each(function(i) {
                var bottom_of_object = jQuery(this).offset().top + jQuery(this).outerHeight(),
                    bottom_of_window = jQuery(window).scrollTop() + jQuery(window).height();

                if (bottom_of_window > bottom_of_object) {
                    var thisel = jQuery(this).children("span.setforanimate");
                    thisel.removeClass("setforanimate").css("display", "block").animate({
                        'width': thisel.attr("rel")
                    }, 500);
                }
            });
        });

    });

})(jQuery);







function lightboxclose() {
    jQuery(".lightbox").css('overflow', 'hidden');
    jQuery(".lightbox .lightcontent").fadeOut('fast');
    jQuery(".lightbox").fadeOut('slow');
    jQuery("body").css('overflow', 'auto');
}


$(document).ready(function() {

    $(".photoCarouselSingle").owlCarousel({

        navigation: false, // Show next and prev buttons
        slideSpeed: 300,
        paginationSpeed: 400,
        singleItem: true

        // "singleItem:true" is a shortcut for:
        // items : 1, 
        // itemsDesktop : false,
        // itemsDesktopSmall : false,
        // itemsTablet: false,
        // itemsMobile : false

    });

});