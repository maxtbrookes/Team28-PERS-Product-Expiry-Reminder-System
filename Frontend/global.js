const BASE_URL = "http://127.0.0.1:5000";

//Function for loading the entries with html output.
/*Updates:
- No longer should need localStorage - added as a database field.
- Changed variable names for code readability.
- Moved to global.js as function in html page bad practice.
- updated UI to work properly with backend endpoints
- removed old localStorage approach and now using backend data
- fixed refresh issues after update and delete
- loads products from backend and renders them on the page
- moved this here because having everything in html was getting messy
*/
// keeps UI state for opened/closed if user changes it on page
// backend already sends opened too, so this only helps the button work for now
let openedState = {};

async function loadProducts(){
    try{
        let res = await fetch(`${BASE_URL}/read_products`);
        let data = await res.json();

        const list = document.getElementById("productList");
        list.innerHTML = "";

        data.forEach(function(entry){
            if(openedState[entry.id] === undefined){
                openedState[entry.id] = String(entry.opened) === "1";
            }

            const isOpened = openedState[entry.id] === true;

            const li = document.createElement("li");
            li.className = "product-card";

            li.innerHTML = `
                <div class="product-head">
                    <div>
                        <div class="product-name">${entry.name}</div>
                        <div class="small-text">
                            Product Id: ${entry.id} |
                            Category: ${entry.category} |
                            Expiry Date: ${entry.expiry_date} |
                            Date Added: ${entry.added_date}
                        </div>
                    </div>

                    <div>
                        ${isOpened
                            ? '<span class="opened-tag">🔓Opened</span>'
                            : '<span class="closed-tag">🔒Closed</span>'}
                    </div>
                </div>

                <div class="btns">
                    <button class="grey-btn" onclick='openOverlay(${JSON.stringify(entry)})'>Update</button>
                    <button class="red-btn" onclick='deleteProduct("${entry.id}")'>Delete</button>
                    <button class="green-btn" onclick='toggleOpened("${entry.id}", "${entry.name}")'>
                        ${isOpened ? "Mark Closed" : "Mark Opened"}
                    </button>
                </div>
            `;

            list.appendChild(li);
        });

    }catch(err){
        console.log("error loading products", err);
        showMsg("Could not load products");
    }
}

function toggleOpened(id, name){ // currently handled on UI side only (backend not fully implemented)
    if(openedState[id] === undefined){
        openedState[id] = false;
    }

    openedState[id] = !openedState[id];

    if(openedState[id]){
        showMsg(name + " has been opened");
    }else{
        showMsg(name + " marked as closed");
    }

    loadProducts();
}