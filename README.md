# 🎮 ISIR Movie Game – Live Voting Backend

This is the local server that receives live votes from the public via the ISIR Movie Game web app.

- 🖱️ Visitors scan a QR code and vote between D1, D2, or D3
- 🌐 The frontend is hosted on GitHub Pages: https://kalessia.github.io/ISIR_movie_game/
- 💻 This backend runs locally on your PC, collects votes, and can display live results

---

## 🚀 Step 1 – Install Requirements

Make sure you have Python 3 installed.

Then install Flask by running:

```bash
pip install flask

⚙️ Step 2 – Run the Local Server

In this folder, start the server with:

python server.py

You should see output like:

Running on http://0.0.0.0:5000/

This means your server is running and accessible on your local network.
✅ Step 3 – Test the Server

In your browser, go to:

http://localhost:5000/results

You should see something like:

{
  "D1": 0,
  "D2": 0,
  "D3": 0
}

Votes will appear here in real time as they are received.
🌐 Step 4 – Connect the Frontend (GitHub Pages)

In your static HTML/JS frontend hosted on GitHub Pages, update your fetch() call like this:

fetch("http://192.168.X.Y:5000/vote", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ choice })
});

📌 Replace 192.168.X.Y with the local IP address of your computer running the server.

You can find your IP address by:

    On macOS or Linux:

ip a

On Windows (in Command Prompt):

    ipconfig

Look for your IPv4 address, usually something like 192.168.1.42.

💡 Important: All devices (audience and server PC) must be connected to the same Wi-Fi network.
📡 API Endpoints
Method	Endpoint	Description
POST	/vote	Submit a vote (JSON payload)
GET	/results	View current vote totals
GET	/log	View full vote log with time
📁 Project Structure

Example layout:

your-computer/
├── ISIR_movie_game/       ← GitHub Pages frontend repo
└── backend_server/        ← This repo (local Flask server)
    ├── server.py
    └── README.md

Keep the frontend and backend separate.