document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menu-toggle');
    const dots = document.getElementById('dots');
    const dropdown = document.getElementById('dropdown');
    const sidebar = document.getElementById('sidebar');
    const closeBtn = document.getElementById('close-btn');

    menuToggle.addEventListener('click', () => {
        sidebar.classList.toggle('open');
    });

    closeBtn.addEventListener('click', () => {
        sidebar.classList.remove('open');
    });

    dots.addEventListener('click', () => {
        dropdown.classList.toggle('show');
    });

    document.addEventListener('click', (event) => {
        if (!dots.contains(event.target) && !dropdown.contains(event.target)) {
            dropdown.classList.remove('show');
        }
    });
});

// async function token((req,res)){
//     const token = req.headers.authorization.split(' ')[1];
//     return token;
// }