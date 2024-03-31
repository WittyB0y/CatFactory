document.addEventListener('DOMContentLoaded', () => {
    const btns = document.getElementsByClassName('email-btn');
    const arrBtns = Array.from(btns);
    arrBtns.forEach(btn => 
        btn.addEventListener('click', (e) => {
            const { target } = e;
            navigator.clipboard.writeText(target.attributes['email'].nodeValue)
        }))
})