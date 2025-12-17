# 🎲 Animated Dice Roller (Flask + JavaScript)

A web-based polyhedral dice roller built with **Python (Flask)** and **JavaScript**, featuring animated dice rolls and support for standard tabletop dice expressions.

This project was built as a learning exercise to explore:

* backend ↔ frontend communication
* HTTP requests
* JavaScript-driven UI updates
* CSS-based animation and styling

---

## 🧭 Why This Project Exists

My friends and I play **Dungeons & Dragons every weekend**, and we’re constantly rolling dice.
I wanted to use something familiar and fun as a way to teach myself the **basics of full-stack development** — specifically how a backend communicates with a frontend and how UI feedback works.

This project focuses on building a clean, correct dice-rolling system with animated feedback while keeping the logic authoritative on the server.
It’s intentionally simple by design and serves as a foundation for future goals, including experimenting with **3D-rendered dice** and more advanced visual effects

---

## ✨ Features

* Supports dice expressions like:

  * `1d6`
  * `2d6`
  * `3d20`
  * `1d10+2`
  * `4d8-1`
* Animated dice rolling effect
* Correct handling of modifiers
* Clean JSON API endpoint
* Simple, readable UI
* No external JS frameworks

---

## 🛠️ Tech Stack

**Backend**

* Python 3
* Flask

**Frontend**

* HTML
* CSS (custom animations & styling)
* JavaScript (Fetch API)

---

## 📁 Project Structure

```
animated-dice-roller/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv .venv
```

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install flask
```

### 4️⃣ Run the app

```bash
python app.py
```

Then open your browser to:

```
http://127.0.0.1:5000
```

---

## 🔌 API Endpoint

### `GET /api/roll`

**Query Parameters**

* `expr` — dice expression (e.g. `2d6+3`)

**Example**

```
/api/roll?expr=2d6+3
```

**Success Response**

```json
{
  "rolls": [4, 2],
  "modifier": 3,
  "total": 9
}
```

**Error Response**

```json
{
  "error": "Invalid dice expression"
}
```

---

## 🎨 Animation Notes

* Dice animation is implemented entirely with **CSS transforms**
* The animation is purely visual — roll results are calculated server-side
* Final values are always authoritative

---

## 📸 Screenshots
**Main Interface**
<br>
<img src="https://github.com/user-attachments/assets/35cdc1e5-b6ac-4308-a432-fd91f607d1f4" width="900" alt="Main dice roller interface" />

<br><br>

**Roll Result with Modifier**
<br>
<img src="https://github.com/user-attachments/assets/9fe4e3c9-cccb-49c6-8208-ffc865ccab31" width="900" alt="Dice roll result with modifier applied" />


---

## 📚 What I Learned

* How JavaScript communicates with a Flask backend using HTTP
* How JSON APIs are consumed by frontend code
* How CSS animations can create convincing UI feedback
* How to structure a small full-stack project

---

## 🔮 Possible Future Improvements

* Support for more complex dice expressions
* Improved animation easing
* Optional 3D rendering with WebGL


