// ==UserScript==
// @name         occupancyGrapher
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Send occupancy data from browser to server to generate graph
// @author       Andrew Simonson (asimonson1125@gmail.com)
// @match        https://recreation.rit.edu/facilityoccupancy
// @icon         https://www.google.com/s2/favicons?sz=64&domain=rit.edu
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    const server = "http://127.0.0.1:8000";

    const cards = document.querySelectorAll('.d-md-flex .occupancy-count');
    const data = {"lower": cards[0].textContent,
                  "upper": cards[1].textContent,
                  "aquatics": cards[2].textContent}
    const options = {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {'Content-Type': 'application/json'}
    };
    fetch(server + "/submit", options);
})();