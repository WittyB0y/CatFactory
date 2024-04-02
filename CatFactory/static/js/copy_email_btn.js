document.addEventListener('DOMContentLoaded', () => {
    const btns = document.getElementsByClassName('email-btn');
    const arrBtns = Array.from(btns);

    arrBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const { target } = e;
            const email = String(target?.attributes?.['email']?.nodeValue);
            navigator?.clipboard?.writeText(email) || copyTextToClipboard(email);
        });
    });

    // On Linux can't use property clipboard and use this func
    function copyTextToClipboard(text) {
        let textarea = document.createElement("textarea");
        textarea.value = text;
        document.body.appendChild(textarea);

        textarea.select();
        textarea.setSelectionRange(0, textarea.value.length);

        document.execCommand("copy");

        document.body.removeChild(textarea);
    }
});
