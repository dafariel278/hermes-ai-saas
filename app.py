import gradio as gr
from agent import hermes_agent

css = """
body{
background:linear-gradient(135deg,#020617,#0f172a);
font-family:Arial;
}

.gradio-container{
max-width:900px !important;
margin:auto;
background:#020617;
border-radius:20px;
padding:40px;
box-shadow:0 20px 60px rgba(0,0,0,0.7);
}

h1{
text-align:center;
color:white;
font-size:40px;
}

"""

def run_agent(prompt):
    return hermes_agent(prompt)

with gr.Blocks(css=css) as demo:

    gr.Markdown("# Hermes AI SaaS")

    gr.Markdown(
    "Autonomous AI Agent powered by Hermes"
    )

    prompt = gr.Textbox(
        label="Enter task for the AI Agent",
        placeholder="Example: Generate a startup idea using AI"
    )

    run_button = gr.Button("Run Agent")

    output = gr.Textbox(label="Agent Output")

    run_button.click(
        fn=run_agent,
        inputs=prompt,
        outputs=output
    )

demo.launch()
