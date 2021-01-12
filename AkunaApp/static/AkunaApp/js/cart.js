/*Test pour voir si l'utilisateur est authentifié*/
userAuthenticated = ()=>{
    if(user === 'AnonymousUser'){
        return 0;
    }else{
        return 1;
    };
};
 /*La méthode de création de panier en cookie*/

 function create_cart(data){
    return new Promise((resolve)=>{
        let cart = {
            id:data,
            products:[],
        };   
        cart = Cookies.createCookie('cart',cart);
        resolve(cart);
    })
}

/*Cette méthode permet de mettre à jour un nouveau panier qui a été ajouté.*/
async function update_new_cart(cart){
    cart = await create_cart(cart);
    update_cart(cart);
}

/*Mise à jour d'un panier*/
function update_cart(cart){
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
//Mise à jour de la quantité d'un produit dans le panier
manage_item_quantity_handler = ()=>{
    const cart_items_quantities = document.querySelectorAll("#quantity");
    for (let i = 0; i < cart_items_quantities.length; i++) {
        const item_quantity = cart_items_quantities[i];
        item_quantity.addEventListener("change",function(e){
            e.preventDefault();
            const new_quantity = this.value;
            const cart_item_id = this.name;
            const action = "update";
            AnonymousUserCart(cart_item_id,action,value=new_quantity);
        })
    }
}

//Suppression d'un élément du panier
del_item_handler = ()=>{
    let delCartItemBtns = document.getElementsByClassName('delete_item');
    for (let i = 0; i < delCartItemBtns.length; i++) {
        const element = delCartItemBtns[i];
        element.addEventListener('click',function(e){
            e.preventDefault()
            let cartItemID = this.dataset.cart_item;
            let action = this.dataset.action;
            const selct = "#"+cartItemID;
            const item = $(selct);
            console.log(item);
            item.fadeOut("slow",function(){
                console.log("Done");
            });
            console.log(cartItemID + "" + action);
            // AnonymousUserCart(cartItemID,action);
        })
    }
}

//Ajoute de produit au panier
add_item_handler = ()=>{
    let addCartItemBtns = document.getElementsByClassName('update-cart');
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
}

//Mise à jour du panier d'un ustilisateur non connecté.
function AnonymousUserCart(cartItemID,action,value=0){
    let csrftoken = Cookies.getCookie('csrftoken');
    let cart = Cookies.getCookie('cart');
    cart = JSON.parse(cart);
    let products = cart.products;
    switch(action){
        case "add":
            const add_Url =  "/add-Cart-Item/";
            product_in_cart = products.includes(parseInt(cartItemID,10));
            if(!product_in_cart){
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
            const del_URL = "/del_CartItem/"
            $.ajax({
                type:"DELETE",
                url:del_URL,
                headers:{
                    'X-CSRFToken':csrftoken,
                },
                data:{
                    cart:cart.id,
                    action:action,
                    cart_item:cartItemID
                },
                success:function(data){
                    if(data === undefined || null){
                        alert("Notre serveur a rencontré un souci au cours de la suppresion!!\nVeuillez reessayez plus tard !!");
                    }else{
                        const selct = "#"+cartItemID;
                        const item = $(selct);
                        item.hide();
                    }
                }
            })
            // Cookies.delCookieData(cart,data=producId);
            break;
        case "update":
            const update_Url = "/update_cart/";
            $.ajax({
                type:"PUT",
                url:update_Url,
                headers:{
                    'X-CSRFToken':csrftoken,
                },
                data:{
                    cart:cart.id,
                    action:action,
                    cart_item:cartItemID,
                    new_value:value
                },
                success:function(data){
                    console.log(data);
                }
            })
            break;
        case "deletAll":
            // Cookies.delAllCookieData(cart);
            break;
        default:
            break;
    }
}


function updateCart() {
    add_item_handler();
    del_item_handler();
    manage_item_quantity_handler();
    // let addCartItemBtns = document.getElementsByClassName('update-cart');
    // for (let i = 0; i < addCartItemBtns.length; i++) {
    //     addCartItemBtns[i].addEventListener("click",function(){
    //         let produitId = this.dataset.produit;
    //         let action = this.dataset.action;
    //         if (userAuthenticated()) {
    //             updateUserCart(produitId,action);   
    //         } else {
    //             AnonymousUserCart(produitId,action);
    //         }
    //     });
    // };
    
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
    // if(!userAuthenticated){
    //     updateCartBadge();
    // }
    if (userAuthenticated()) {
        
    } else {
        updateCartBadge();
    }
    updateCart();
});