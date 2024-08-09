from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with a form to capture user input
html_template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Input Form</title>
  </head>
  <body>
    <h1>Enter a value</h1>
    <form method="POST" action="/">
      <input type="text" name="input_value">
      <input type="submit" value="Submit">
    </form>
    {% if input_value %}
      <h2>You entered: {{ input_value }}</h2>
      {% if input_value == "18" %}
        <p>You are under age!</p>
      {% elif input_value >= '18' %}
        <p>You are above 18!</p>
      {% elif input_value <= '18' %}
        <p>You are below 18!</p>
      {% else %}
        <p>You entered something else!</p>
      {% endif %}
    {% endif %}
  </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    input_value = None
    if request.method == 'POST':
        input_value = request.form['input_value']
    return render_template_string(html_template, input_value=input_value)

if __name__ == "__main__":
    app.run(debug=True)