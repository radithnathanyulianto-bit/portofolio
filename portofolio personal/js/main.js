
const text = "Adaptasi: 0 → 100 dalam 72 jam";
let i = 0;
const typewriterElement = document.getElementById("typewriter");

if (typewriterElement) {
  function type() {
    if (i < text.length) {
      typewriterElement.innerHTML += text.charAt(i);
      i++;
      setTimeout(type, 60); 
    }
  }
  type();
}


const form = document.getElementById("contact-form");
if (form) {
  form.addEventListener("submit", function(e) {
    e.preventDefault();
    
    const templateParams = {
      from_name: document.getElementById("name").value,
      from_email: document.getElementById("email").value,
      message: document.getElementById("message").value
    };

    emailjs.send("service_e6jwccl", "template_e6wjccl", templateParams)
      .then(() => {
        document.getElementById("status").innerHTML = "Terkirim. Respon < 24 jam.";
        form.reset();
      }, () => {
        document.getElementById("status").innerHTML = "Gagal. Coba lagi.";
      });
  });
}