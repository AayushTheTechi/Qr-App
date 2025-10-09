from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Qr-App</title>
    <style>
        body { font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        input, button { padding: 10px; margin: 5px 0; }
        .result { margin-top: 20px; padding: 10px; background: #f0f0f0; }
    </style>
</head>
<body>
    <h1>Qr App</h1>
    <form method="POST">
        <input type="text" name="data" placeholder="Enter data..." required>
        <button type="submit">Run</button>
    </form>
    {% if result %}
    <div class="result">
        <strong>Result:</strong> { result }
    </div>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        data = request.form.get('data')
        # Placeholder for actual logic integration
        result = f"Processed '{data}' successfully."
    return render_template_string(HTML_TEMPLATE, result=result, repo_name="Qr-App")

if __name__ == '__main__':
    app.run(debug=True)
