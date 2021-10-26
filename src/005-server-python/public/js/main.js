const BASE_API = '/public/data/products.json';

const productTemplate = (product) => {
    return (
        `<div class="card">
            <div class="card-content">
            <div class="media">
                <div class="media-left">
                <figure class="image is-48x48">
                    <img src="${product.image_url}" alt="${product.title}">
                </figure>
                </div>
                <div class="media-content">
                <p class="title is-5">${product.title}</p>
                <p class="subtitle is-6">${product.description}</p>
                <p class="subtitle is-6"><a href="#">${product.price}</a></p>
                <div class="control">
                    <button class="button is-primary">Carrito</button>
                </div>
                </div>
            </div>
            </div>
        </div>`
    )
}
function graphProducts(products) {
    if(products){
        const baseDiv = document.getElementById("list-products");
        for(index in products){
            const product = products[index];
            const div = document.createElement('div');
            div.classList.add("is-4", "column");
            div.innerHTML = productTemplate(product);

            baseDiv.appendChild(div);
        }
    }
}
(async function load(){
    const products = await getData(BASE_API);
    graphProducts(products);
})();