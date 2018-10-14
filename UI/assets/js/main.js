/* toggle to show and hide the dropdown content */
myActions = () => {
    document.getElementById("myDropdown").classList.toggle("show");
}
// Close the dropdown menu
window.onclick = (event) => {
    if (!event.target.matches('.dropdown-btn')) {
        const dropdowns = document.getElementsByClassName("dropdown-content");
        let i;
        for (i = 0; i < dropdowns.length; i++) {
            const openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

/* Search for a product by name or category */
searchProduct = () => {
    let input, filter, table, tr, td, i;
    input = document.getElementById("searchInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("allProducts");
    tr = table.getElementsByTagName("tr");
    // Loop through all table rows and hide the ones not matching the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }    
        }
    }
}

/* Open modal to add a product */
const modal = document.getElementById("addProductModal");
const modalBtnProduct = document.getElementById("addProduct");
const span = document.getElementsByClassName("close")[0];
// Open modal when user clicks modal button
modalBtnProduct.onclick = () => {
    modal.style.display = "block";
}
// Close modal when user clicks "x"
span.onclick = () => {
    modal.style.display = "none";
}
// Close modal if the user clicks outside it
window.onclick = (event) => {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

/* Open modal to add an attendant */
const modalAttendant = document.getElementById("addAttendantModal");
const modalBtnAttendant = document.getElementById("addAttendant");
const spanAttendant = document.getElementsByClassName("cancel")[0];

modalBtnAttendant.onclick = () => {
    modalAttendant.style.display = "block";
}
spanAttendant.onclick = () => {
    modalAttendant.style.display = "none";
}
window.onclick = (e) => {
    if (e.target == modalAttendant) {
        modalAttendant.style.display = "none";
    }
}
