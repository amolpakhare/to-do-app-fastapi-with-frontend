document.addEventListener("DOMContentLoaded", () => {
    // Handle delete confirmation
    const deleteForms = document.querySelectorAll("form[action^='/delete/']");
    deleteForms.forEach(form => {
        form.addEventListener("submit", (e) => {
            const confirmDelete = confirm("Are you sure you want to delete this task?");
            if (!confirmDelete) {
                e.preventDefault();
            }
        });
    });

    // Optional: auto-focus on first input field
    const firstInput = document.querySelector("input[type='text']");
    if (firstInput) {
        firstInput.focus();
    }
});
