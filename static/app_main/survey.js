let companiesSelect = document.getElementById("company");


function praiseTheUser() {
    let span = document.getElementById("congratulations");
    if (!Object.is(span, null)) {
        span.className = "";
        span.textContent = "Great choice!";
    } else {
        span = document.createElement("span");
        span.id = "congratulations";
        span.textContent = "Great choice!";
    }
    if (this.value == "storylines") {
        this.after(span);
    } else {
        span.className = "return";
        span.textContent = "return you answer!";
    }
};


companiesSelect.addEventListener('change', praiseTheUser);