const BASE_URL = "http://127.0.0.1:5000";

//Function for loading the entries with html output.
/*Updates:
- No longer should need localStorage - added as a database field.
- Changed variable names for code readability.
- Moved to global.js as function in html page bad practice.
*/
async function loadProducts(){
    try{
        let res = await fetch(BASE_URL+'/read_products');
        let data = await res.json();

        const list = document.getElementById("productList");
        list.innerHTML = "";

        data.forEach(function(entry){
            
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
                        ${entry.opened == 1
                            ? '<span class="opened-tag">Opened</span>'
                            : '<span class="closed-tag">Closed</span>'}
                    </div>
                </div>

                <div class="btns">
                    <button class="grey-btn" onclick='openOverlay(${JSON.stringify(entry)})'>Update</button>
                    <button class="red-btn" onclick='deleteProduct("${entry.id}")'>Delete</button>
                    <button class="green-btn" onclick='toggleOpened("${entry.id}", "${entry.name}")'>
                        ${entry.opened == 1 ? "Mark Closed" : "Mark Opened"}
                    </button>
                </div>
            `;

            list.appendChild(li);
        });

    }catch(err){
        console.log("error loading products", err);
    }
}