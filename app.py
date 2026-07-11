from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    hook = script = scenes = cta = ""

    if request.method == 'POST':

        # 🧠 Get user inputs
        product = request.form.get('product')
        description = request.form.get('description')
        audience = request.form.get('audience')
        goal = request.form.get('goal')
        duration = request.form.get('duration')

        if not duration:
            duration = "30"

        # 🔥 HOOK
        hook = f"Stop scrolling! {product} is exactly what {audience} needs right now."

        # 🎬 SCRIPT
        script = f"""
[SCENE 1 - INTRO]
We are introducing {product}.

[SCENE 2 - PROBLEM]
{description}

[SCENE 3 - SOLUTION]
{product} is built for {audience} to achieve {goal} in {duration} seconds.
"""

        # 🎥 SCENES
        scenes = f"""
1. Opening shot of {product}
2. Problem faced by {audience}
3. Solution demonstration of {product}
"""

        # 🚀 CTA
        cta = f"Get {product} now and achieve your {goal} instantly!"

    return render_template("index.html",
                           hook=hook,
                           script=script,
                           scenes=scenes,
                           cta=cta)

if __name__ == "__main__":
    app.run(debug=True)