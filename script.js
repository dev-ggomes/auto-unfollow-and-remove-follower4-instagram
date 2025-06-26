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
    });
})