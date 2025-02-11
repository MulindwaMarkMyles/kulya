var updateButtons = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateButtons.length; i++){
        updateButtons[i].addEventListener('click', function () {
                var productId = this.dataset.product
                var action = this.dataset.action
                console.log(productId, ":", action)
                
                console.log(user.username)
                if (user == "AnonymousUser")
                        addCookieItem(productId, action)
                else
                        updateUserOrder(productId, action)
        })
}

function addCookieItem(productId, action) {
        console.log("Not logged in...")
        if (action == 'add') {
                if (cart[productId] == undefined) {
                        cart[productId] = { "quantity": 1 }
                } else {
                        cart[productId]['quantity'] += 1
                }
        }
        
        if (action == 'remove') {
                cart[productId]['quantity'] -= 1
                if (cart[productId]['quantity'] <= 0) {
                        console.log('Remove item..')
                        delete cart[productId]
                }
        }
        console.log("Console:", cart)
        document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
        location.reload()
}

function updateUserOrder(productId, action) {
        console.log("User logged in sending data....")
    var url = '/update-item/'
    console.log(url);
        
        fetch(url, {
                method: 'POST',
                headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFtoken': csrftoken,
                },
                body: JSON.stringify({ 'productId': productId, 'action': action })
        })
        
        .then((response) => {
                return response.json()
        })
        
                .then((data) => {
                        console.log('data: ', data)
                        location.reload()
        })
}