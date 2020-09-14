$(()=>{
    $('#carousel').carouFredSel(
      {
        items:1,
        infinite:true,
        circular:true,
        align:"center",
        scroll:{
          items:1,
          easing: "elastic",
          duration:1000,
          pauseOnHover:true
        }  
      }
    );
  })