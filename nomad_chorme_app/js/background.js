const images = ["01.jpg", "02.jpg", "03.jpg", "04.jpg"];
const chooseImg = images[Math.floor(Math.random() * images.length)];

const bgImage = document.createElement("img");
bgImage.src = `img/${chooseImg}`;

document.body.appendChild(bgImage);
