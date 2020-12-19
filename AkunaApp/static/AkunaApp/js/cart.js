//Test pour voir si l'utilisateur est authentifié
userAutenticathed = ()=>{
    if(user === 'AnonymousUser'){
        return 0;
    }else{
        return 1;
    }
}

function AnonymousUserCart(produitId,action){
    let cart = Cookies.getCookie('cart');
    if (cart == undefined || cart == null) {
        cart = {
            products:[],
        };    
        cart = Cookies.createCookie('cart',cart);
    }
    switch(action){
        case "add":
            Cookies.addCookieData('cart',cart,data=produitId);
            break;
        case "delete":
            // Cookies.delCookieData(cart,data=producId);
            break;
        case "deletAll":
            // Cookies.delAllCookieData(cart);
            break;
        default:
            break;
    }
}

//Mise à jour du panier
function updateCart() {
    let updateCartBtns = document.getElementsByClassName('update-cart');
    for (let i = 0; i < updateCartBtns.length; i++) {
        updateCartBtns[i].addEventListener("click",function(){
            let produitId = this.dataset.produit;
            let action = this.dataset.action;
            if (userAutenticathed()) {
                updateUserCart(produitId,action);   
            } else {
                AnonymousUserCart(produitId,action);
            }
        })
    }
}


// Accès aux cookies
function getCookie(name) {
    let cookieArr = document.cookie.split(';');
    for (let i = 0; i < cookieArr.length; i++) {
        const cookiePair = cookieArr[i].split("=");

        if (name == cookiePair[0].trim()) {
            return decodeURIComponent(cookiePair[1]);
        }
    }
    return null;
}


 function updateUserCart(produitId,action){
    let url = '/update_commande/';
    const csrftoken = Cookies.getCookie('csrftoken');
    console.log(csrftoken);
    $.ajax({
        type: "POST",
        url: url,
        headers:{
            'X-CSRFToken': csrftoken,
        },
        data: JSON.stringify({'produitID':produitId,'action':action}),
        success: function (data) {
          console.log(data);
        },

      });
    };


$(()=>{
    // createCartCookie();
    updateCart();
});