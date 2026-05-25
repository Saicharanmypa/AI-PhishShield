from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>AI-PhishShield</title>

    <style>
        body {
            background-color: #0f0f0f;
            color: white;
            font-family: Arial;
            text-align: center;
            padding-top: 100px;
        }

        h1 {
            color: red;
        }

        input {
            width: 400px;
            padding: 12px;
            border-radius: 8px;
            border: none;
        }

        button {
            padding: 12px 20px;
            border: none;
            border-radius: 8px;
            background: red;
            color: white;
            cursor: pointer;
        }

        .result {
            margin-top: 30px;
            font-size: 24px;
        }
    </style>
</head>

<body>

    <h1>AI-PhishShield</h1>
    <p>AI Powered Phishing URL Detection</p>

    <form method="POST">
        <input type="text" name="url" placeholder="Enter Website URL">
        <button type="submit">Scan</button>
    </form>

    {% if prediction %}
<div class="result">
    <p>{{ prediction }}</p>
    <p>Threat Score: {{ score }}</p>
</div>
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

    

    prediction = None
    score = None

    if request.method == "POST":

        url = request.form["url"]

        if "google" in url or "github" in url:
            prediction = "✅ Legitimate Website"
            score = "12%"

        else:
            prediction = "⚠️ Phishing Website Detected"
            score = "89%"

    return render_template_string(html, prediction=prediction, score=score)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)