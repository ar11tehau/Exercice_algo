"use strict";

function freq_for(table, objet) {
    let occurence = 0;
    for (let i = 0; i < table.length; i++) {
        if (objet === table[i]) {
            occurence++;
        }
    }
    return occurence
}

function freq_for_of(table, objet) {
    let occurence = 0;
    for (const element of table) {
        if (objet === element) {
            occurence++;
        }
    }
    return occurence
}

function freq_for_in(table, objet) {
    let occurence = 0;
    for (const index in table) {
        if (objet === table[index]) {
            occurence++;
        }
    }
    return occurence
}

function freq_do_while(table, objet) {
    let occurence = 0;
    let i = 0;
    if (table.length < 0) {
        return 0;
    }
    do {
        if (objet === table[i]) {
            occurence++;
        }
        i++;
    } while (i < table.length)
    return occurence
}

function freq_while(table, objet) {
    let occurence = 0;
    let i = 0;
    while (i < table.length) {
        if (objet === table[i]) {
            occurence++;
        }
        i++;
    }
    return occurence
}

let table = ["a", "b", "a", "a", "l"]

console.log(freq_for(table, "a"))
console.log(freq_for_of(table, "a"))
console.log(freq_for_in(table, "b"))
console.log(freq_while(table, "l"))
console.log(freq_do_while(table, "x"))