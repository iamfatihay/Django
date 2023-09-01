// let element = document.querySelector(".messages")

// setTimeout(function() {
//     element.style.display = "none";
// }, 2000);



// Sayfa tamamen yüklendiğinde çalışacak bir fonksiyon
document.addEventListener("DOMContentLoaded", function() {
    let element = document.querySelector(".messages");

    // setTimeout kullanımı
    setTimeout(function() {
        if (element) {
            element.style.display = "none";
        }
    }, 2000);
});
