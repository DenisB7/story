let companiesSelect = document.getElementById("company");


function praiseTheUser() {
    if (this.value == "storylines") {
        span = document.createElement("span");
        span.className = "congratulations";
        span.textContent = "Great choice!";
        this.after(span);
    }
};


companiesSelect.addEventListener('change', praiseTheUser);