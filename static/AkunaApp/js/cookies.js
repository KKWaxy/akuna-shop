Cookies = {}

Cookies.createCookie = function(name,data){
    document.cookie = name + '=' + JSON.stringify(data) + ';domain=;path=/';
    return(Cookies.getCookie(name));
};

Cookies.getCookie = (name)=>{
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  };

Cookies.addCookieData = (name,cookie,data) =>{
    if(cookie == null){
        return 0;
    }else{
        console.log(cookie.products);
        // cookie.products.push(data);
        console.log(cookie.products);
        document.cookie = name + '=' + JSON.stringify(cookie) + ';domain=;path=/';
        return 1;
    }
  }
