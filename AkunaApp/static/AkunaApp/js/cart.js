userAuthenticated = ()=>{
    /*Test pour voir si l'utilisateur est authentifié*/
    if(user === 'AnonymousUser'){
        return 0;
    }else{
        return 1;
    };
};

function create_cart(data){
    /*La méthode de création de panier en cookie*/
    return new Promise((resolve)=>{
        let cart = {
            id:data,
            products:[],
        };   
        cart = Cookies.createCookie('cart',cart);
        resolve(cart);
    })
}

async function update_new_cart(cart){
    /*Cette méthode permet de mettre à jour un nouveau panier qui a été ajouté.*/
    cart = await create_cart(cart);
    update_cart(cart);
}

function update_cart(cart){
    /*Mise à jour d'un panier*/
    cart = JSON.parse(cart);
    let products = cart.products;
    let cartLength = document.getElementById('cartLength');
    cartLength.innerText = document.createTextNode(products.length).textContent;  
}
 
function updateCartBadge(){
    let cart = Cookies.getCookie('cart');
    if (cart == undefined || cart == null) {
        const csrftoken = Cookies.getCookie('csrftoken');
        const create_cartURL = "/create_cart/";
        const action = 'create_cart';
        $.ajax({
            type:"GET",
            url:create_cartURL,
            headers:{
                'X-CSRFToken': csrftoken,
            },
            data:{
                action:action,
            },
            
        }).done((data)=>{
            update_new_cart(data);
        });
    }
    else{
        update_cart(cart);
    };
}

//Mise à jour du panier d'un ustilisateur non connecté.
function AnonymousUserCart(cartItemID,action){
    switch(action){
        case "add":
            const add_Url =  "/add-Cart-Item/";
            let csrftoken = Cookies.getCookie('csrftoken');
            let cart = Cookies.getCookie('cart');
            cart = JSON.parse(cart);
            let products = cart.products;
            console.log(products.includes(cartItemID));
            if(!products.includes(cartItemID)){
                $.ajax({
                    type:"POST",
                    url:add_Url,
                    headers:{
                        'X-CSRFToken':csrftoken,
                    },
                    data:{
                        cart : cart.id,
                        action : "add_Item",
                        produit : cartItemID,
                    },
                    success:function(data){
                        cart.products.push(data);
                        Cookies.addCookieData('cart',cart);
                        updateCartBadge();
                    },
                })
            };
            break;
        case "delete":
            console.log('ok');
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
    let addCartItemBtns = document.getElementsByClassName('update-cart');
    let delCartItemBtns = document.getElementsByClassName('delete_item');
    for (let i = 0; i < addCartItemBtns.length; i++) {
        addCartItemBtns[i].addEventListener("click",function(){
            let produitId = this.dataset.produit;
            let action = this.dataset.action;
            if (userAuthenticated()) {
                updateUserCart(produitId,action);   
            } else {
                AnonymousUserCart(produitId,action);
            }
        });
    };
    for (let i = 0; i < delCartItemBtns.length; i++) {
        const element = delCartItemBtns[i];
        element.addEventListener('click',function(){
            preventDefault();
            let cartItemID = this.dataset.cart_item;
            let action = this.dataset.action;
            if(!userAuthenticated()){
                AnonymousUserCart(cartItemID,action);
            }
        })
    }
}

function updateUserCart(produitId,action){
    let url = '/update_commande/';
    const csrftoken = Cookies.getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: url,
        headers:{
            'X-CSRFToken': csrftoken,
        },
        data: {'produitID':produitId,'action':action},
        success: function (data) {console.log(data);},

      });
    };

$(()=>{
    if (userAuthenticated()) {
        
    } else {
        updateCartBadge();
    }
    updateCart();
});