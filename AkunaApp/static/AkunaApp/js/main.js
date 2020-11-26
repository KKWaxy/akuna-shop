$(()=>{
  var akuna_window = $(window);

    $("#carousel").carouFredSel(
      {
        items:1,
        infinite:true,
        circular:false,
        align:"center",
        scroll:{
          items:1,
          easing: "raise-in",
          duration:500,
          pauseOnHover:true
        }
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