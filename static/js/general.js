$(function(){

$(".hasubmenu").click(function(){
                $(this).find("ul").toggle();
                $(this).toggleClass('spsubmenuon');
                e.preventDefault();
                
            });

// MENU RESPONSIVE
var $btn = $('#js-iconMenu'),
    $menu = $('.js-toggleEffect');
function menuToggle(e) {

    $menu.fadeToggle();
    $(this).toggleClass('on');
    e.preventDefault();
}
$btn.on('click', menuToggle);
$('.menu_close').on('click', function(){
    $('#js-iconMenu').click();
    /*$('html, body').animate({
        scrollTop: 0
    }, 300);*/
    return false;
});

$('.spclose').on('click', function(){
    $('#js-iconMenu').click();
    /*$('html, body').animate({
        scrollTop: 0
    }, 300);*/
    return false;
});
});




$.fn.textlimit = function(limit)
{
    return this.each(function(index,val)                       
    {
        var $elem = $(this);
        var $limit = limit;
        var $strLngth = $(val).text().length; 
        if($strLngth > $limit)
        {
          $($elem).text($($elem).text().substr( 0, $limit )+ "...");
        }
    })
};
$(window).on('load', function() {
        $(".slider_wrapspimg").hide();
        $('#slider_sp').addClass('showslide');

    });
$(document).ready(function() {
    $(window).resize(function() {
       var windowWidth = $( window ).width();
    if(windowWidth < 768){
     $(".column_txt_dec").textlimit(20);
     $(".workstyle").textlimit(10);
     $(".jobnum").textlimit(5);
     $(".card01_table table th").textlimit(4);
     $(".card01_table table td").textlimit(7);
     $(".card02_table table th").textlimit(5);
  }else {
   $(".column_txt_dec").textlimit(50);
   $(".workstyle").textlimit(50);
   $(".jobnum").textlimit(20);
   $(".card01_table table th").textlimit(20);
   $(".card01_table table td").textlimit(20);
   $(".card02_table table th").textlimit(10);
  }
    }).resize();
});

$(document).on('ready', function() {
$(".logo img ").on('load', function() {
            $('.slider_wrap').css('background', 'none');
            $('.slider_wrap').css('height', 'auto');
            $('#slider').show();
              $('.flexslider').flexslider({
    animation : "fade", // slide or fade
    slideshowSpeed : 4000, //Integer: Set the speed of the slideshow cycling, in milliseconds
    animationSpeed : 1000,
    directionNav: false,
    controlNav: true
    });


        }).each(function() {
            if (this.complete) $(this).load();
        });
    $(".variable_sp").slick({
        dots: true,
    infinite: true,
    speed: 1000,
    fade: true,
    prevArrow: false,
    infinite: true,
    autoplay: true,
    nextArrow: false,
    pauseOnHover: false,
    cssEase: 'linear'
    });
    $(".list_job_sp").slick({
        dots: false,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1
    });
    $(" .detailfcol_sp").slick({
        dots: false,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1
    });

});

$( ".variable" ).hover(
  function() {
    $( ".slide_pager_warap" ).addClass( "slickhover" );
  }, function() {
    $( ".slide_pager_warap" ).removeClass( "slickhover" );
  }
);
$( ".slide_pager_warap" ).hover(
  function() {
    $( ".slide_pager_warap" ).addClass( "slickhover" );
  }, function() {
    $( ".slide_pager_warap" ).removeClass( "slickhover" );
  }
);

$('.slick-next').click(function(){
    $('.variable').slick("slickNext");
});

$('.slick-prev').click(function(){
    $('.variable').slick("slickPrev");
 });
// PAGE TOP
$(function(){
  $('.back-to-top').click(function() {
  $('html, body').animate({
    scrollTop: 0
  }, 700);
  return false;
});
})

$.fn.textlimit = function(limit)
{
    return this.each(function(index,val)                       
    {
        var $elem = $(this);
        var $limit = limit;
        var $strLngth = $(val).text().length; 
        if($strLngth > $limit)
        {
          $($elem).text($($elem).text().substr( 0, $limit )+ "...");
        }
    })
};

$(document).ready(function() {
    $(window).resize(function() {
       var windowWidth = $( window ).width();
      if(windowWidth < 768){
     $(".card_title").textlimit(25);
  }else {
   $(".card_title").textlimit(45);
  }
    }).resize();
});

//show more text
$(document).ready(function() {
  var showChar = 40;
  var ellipsestext = "...";
  var moretext = "続きを読む▼";
  var lesstext = "▲閉じる";
  $('.seomore').each(function() {
    var content = $(this).html();

    if(content.length > showChar) {

      var c = content.substr(0, showChar);
      var h = content.substr(showChar-1, content.length - showChar);

      var html = c + '<span class="moreellipses">' + ellipsestext+ '&nbsp;</span><span class="morecontent"><span>' + h ;

      $(this).html(html);
    }

  });

  $(".semorelink").click(function(){
    if($(this).hasClass("less")) {
      $(this).removeClass("less");
      $(this).html(moretext);
      
    } else {
      $(this).addClass("less");
      $(this).html(lesstext);
      
    }
    $(this).parent().prev().toggle();
    $(this).prev().toggle();
    return false;
  });
});
