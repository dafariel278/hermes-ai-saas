from transformers import pipeline

# Load Hermes model
model = pipeline(
    "text-generation",
    model="NousResearch/Hermes-2-Pro-Mistral-7B",
    device_map="auto"
)

def hermes_agent(task):

    system_prompt = f"""
You are Hermes AI Agent.

You must reason step by step and produce professional answers.

Task:
{task}

Response:
"""

    result = model(
        system_prompt,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7
    )

    return result[0]["generated_text"]
