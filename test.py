('DOCTYPE html')
 ("html lang" ="uk")
(head)
    (meta charset="UTF-8")
    (title>Taxi Service</title)
    <link rel="stylesheet" href="style.css">
</head>
<body>

<header>
    <h1>🚕 Taxi Service</h1>
    <p>Швидко • Зручно • Доступно</p>
    <a class="phone" href="tel:+380679440968 ">+380 67 944 09 68</a>

<section class="main">
    <img src="taxi.jpg" alt="Taxi" class="main-img">
    <h2>Замовити таксі онлайн</h2>
    <button onclick="alert('Ваше замовлення прийнято!')">Замовити</button>
</section>

<footer>
    <p>© 2025 Taxi Service — Усі права захищені</p>
</footer>

</body>
</html>
body {
    font-family: Arial, sans-serif;
    margin: 0;
    background: #f3f3f3;
}

header {
    background: #ffd21d;
    text-align: center;
    padding: 20px;}

.phone {
    display: inline-block;
    margin-top: 10px;
    font-size: 20px;
    color: black;
    text-decoration: none;
    font-weight: bold;
}

.main {
    text-align: center;
    padding: 40px;
}

.main-img {
    width: 300px;
    border-radius: 10px;
    margin-bottom: 20px;
}

button {
    padding: 12px 25px;
    background: #000;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 18px;
    cursor: pointer;
}

footer {
    text-align: center;
    padding: 15px;
    background: #222;
    color: #fff;
}
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Admin Panel</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<header>
    <h1>Адмін-панель('h1')
</header>

<section class="main">
    <h2>Додати нове фото</h2>
    <input type="file" id="photoInput">
    <button onclick="savePhoto()">Зберегти</button>

    <h2>Поточне фото:</h2>
    <img id="preview" src="taxi.jpg" width="300">
</section>

<script>
function savePhoto() {
    const fileInput = document.getElementById("photoInput");
    const file = fileInput.files[0];

    if (!file) return alert("Оберіть фото!");

    const reader = new FileReader();
    reader.onload = function(e) {
        localStorage.setItem("mainPhoto", e.target.result);
        document.getElementById("preview").src = e.target.result;
        alert("Фото оновлено!");
    };
    reader.readAsDataURL(file);
}

window.onload = () => {
    const saved = localStorage.getItem("mainPhoto");
    if (saved) document.getElementById("preview").src = saved;
};
</script>

</body>
</html>
