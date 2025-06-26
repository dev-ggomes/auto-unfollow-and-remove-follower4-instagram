// ==UserScript==

// @name            Instagram Quick Unfollow & Remove
// @namespace       http://tampermonkey.net/
// @version         1.0
// @description     Allows you to unfollow someone by clicking "Ctrl + D" and by clicking "Ctrl + F" you can remove someone from your followers list
// @author          dev-ggomes
// @match           https://instagram.com/*/followers/*
// @match           https://instagram.com/*/following/*
// @grant           none
// @license         MIT License

// ==/UserScript==

(function() {
    'use strict';

    let lastHoveredItem = null;

    // Marca o <li> quando o mouse passa por cima
    document.addEventListener('mouseover', e => {
        if (li && li.querySelector('button')) {
            lastHoveredItem = li;
        }
    });

    // Atalhos do teclado
    document.addEventListener('keydown', e => {
        // Unfollow: Ctrl + D
        if (e.ctrlKey && e.key.toLowerCase() === 'd') {
            e.preventDefault();
            triggerAction();
        }
        // Remove follower: Ctrl + F
        if (e.ctrlKey && e.key.toLowerCase() === 'f') {
            e.preventDefault();
            triggerAction();
        }
    });

    function triggerAction() {
        if (!lastHoveredItem) return;
        const btn = lastHoveredItem.querySelector('button');
        if (!btn) return;
        btn.click();

        // Se aparecer modal de confirmação, clica nele automaticamente
        setTimeout(() => {
            // Botões de confirmação constumam ter a classe -Cab_
            const confirmBtn = document.querySelector('button.-Cab_');
            if (confirmBtn) {
                confirmBtn.click();
            }
        }, 500);
    }
})();