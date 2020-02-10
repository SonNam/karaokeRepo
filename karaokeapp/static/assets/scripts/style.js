$(document).ready(function(){
        // $('#datetime-picker').datetimepicker({
        //    format: 'DD/MM/YYYY',
        // });
        // $(function () {
        if($(this).width() < 768){
            $('.form-content .frm label .tool-tip').addClass('md');            
        }
        else if($(this).width() >= 768){
            $('.form-content .frm label .tool-tip').removeClass('md');            
        };
    $('.form-content .frm input.form-control').focus(function(){
        $(this).siblings('span.required').hide();
    });
    $('.form-content .frm .popup p span.close').click(function(){
        $(this).parent('p').slideUp();
    });
    $('.product .side-bar>ul>li>span').click(function(){
        if($(this).parent('li').hasClass('active')){
            $('.product .side-bar>ul>li').removeClass('active');
            $('.product .side-bar>ul>li>ul').slideUp();
        }
        else{
            $('.product .side-bar>ul>li>ul').slideUp();
            $('.product .side-bar>ul>li').removeClass('active');            
            $(this).parent('li').addClass('active');
            $(this).siblings('ul').slideDown();
        }
    });
    $('header .right .right-bar .control-bar span.ct-bar').click(function(){
        $('header .right .right-bar .control-bar .ct-down').toggleClass('active');
    });
    $('.lab-cmt').click(function(){
        $('.inp-cmt').show();
        $('.so-hd').hide();
    });
    $('.lab-shd').click(function(){
        $('.so-hd').show();
        $('.inp-cmt').hide();
    });
    $('.lab-phone').click(function(){
        $('.inp-phone').show();
        $('.inp-mail').hide();
    });
    $('.lab-mail').click(function(){
        $('.inp-mail').show();
        $('.inp-phone').hide();
    });
    
    $( ".form-content .frm label .tool-tip" ).hover(
        function() {
          $( this ).siblings('.text-tool').addClass( "hover" );
        }, function() {
          $( this ).siblings('.text-tool').removeClass( "hover" );
        }
      );
    $(".menu_mb").click(function(){
        $('header .right').addClass('active');
        $(this).addClass('active');
    });
    $(".btn-out , header .right .overlay").click(function(){
        $('header .right').removeClass('active');
        $('.menu_mb').removeClass('active');
    });
});
$(document).ready(function(){
    $('.content_v1 .item .right .check-i').click(function(){
        if($(window).width()>1199){
            $('.content_v1 .item .right .desc-check-i').toggleClass('active');
        }
        else if($(window).width() < 1200){
                $('.content_v1 .item .right .desc-check-i').slideToggle();
        }
    });
    $('.form-ct form label textarea').click(function(){
        $('.dl-mau').hide();
    });
    var scH  =   $(window).height();
    var PgH = $('body').height();
        if($(window).width() > 991){
            if(PgH < scH ){
                $('footer').addClass('fixed-bottom');
            }
            else{
                $('footer').removeClass('fixed-bottom');        
            }
        }
});
