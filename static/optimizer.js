function RemoveAtribute(id) {
    const checkboxes = document.querySelectorAll(`input[type='checkbox'][id='${id}']`);
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener("click", () => {
        if (checkbox.checked) {
            checkboxes.forEach(cb => {
            if (cb !== checkbox) {
                cb.removeAttribute("required");
            }
            });
        } else {
            checkboxes.forEach(cb => {
            if (cb !== checkbox) {
                cb.setAttribute("required", "");
            }
            });
        }
        });
    });
}