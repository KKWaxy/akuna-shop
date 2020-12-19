$(()=>{
  var akuna_window = $(window);
  $('.owl-carousel').owlCarousel(
    {
      items:1,
      loop:true,
      autoplay:true,
      autoplayHoverPause:true,
      center:true,
    }
  );
    akuna_window.on('scroll', () => {
        if(akuna_window.scrollTop() > 40){
            $('.akunaApp-header').addClass('sticky-top');
            
      }else{
            $('.akunaApp-header').removeClass('sticky-top');
      }
    })
  });