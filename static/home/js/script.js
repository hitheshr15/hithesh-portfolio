const menuToggle =
    document.querySelector(".menu-toggle");

const navMenu =
    document.querySelector(".nav-menu");


if (menuToggle && navMenu) {

    menuToggle.addEventListener(
        "click",
        function () {

            navMenu.classList.toggle("active");

        }
    );

}


const navLinks =
    document.querySelectorAll(".nav-menu a");


navLinks.forEach(function (link) {

    link.addEventListener(
        "click",
        function () {

            navMenu.classList.remove("active");

        }
    );

});



/* ========================= */
/* Scroll Reveal */
/* ========================= */

const revealElements =
    document.querySelectorAll(
        ".section, .project-card, .skill-card, .certification-card"
    );


const observer =
    new IntersectionObserver(
        function (entries) {

            entries.forEach(function (entry) {

                if (entry.isIntersecting) {

                    entry.target.classList.add(
                        "visible"
                    );

                }

            });

        },
        {
            threshold: 0.08
        }
    );


revealElements.forEach(function (element) {

    element.classList.add("reveal");

    observer.observe(element);

});




function copyEmail() {

    const email =
        document.getElementById("email-text").innerText;

    navigator.clipboard.writeText(email)
        .then(function () {

            const button =
                document.querySelector(".copy-email-btn");

            button.innerText = "Copied ✓";

            setTimeout(function () {
                button.innerText = "Copy";
            }, 2000);

        })
        .catch(function () {

            alert("Unable to copy email.");

        });
}