from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head>
        <title>Girish DevOps Dashboard</title>
        <style>
          body {
            background: #0b1120;
            color: #f1f5f9;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 100px 20px;
          }
          .card {
            max-width: 650px;
            margin: auto;
            padding: 40px;
            background: #172033;
            border-radius: 16px;
            border: 1px solid #334155;
          }
          h1 { color: #38bdf8; }
          .status { color: #4ade80; }
        </style>
      </head>
      <body>
        <div class="card">
          <h1>Girish's DevOps Dashboard</h1>
          <h2>Python + Flask + Docker</h2>
          <p class="status">Application is running!</p>
          <p>My second Dockerfile project.</p>
        </div>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
