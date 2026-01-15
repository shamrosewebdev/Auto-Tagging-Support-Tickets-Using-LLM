# app.py

import gradio as gr
from transformers import pipeline

CATEGORIES = [
    "Billing",
    "Technical Issue",
    "Account Support",
    "Service Request",
    "General Inquiry"
]

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

def auto_tag_ticket(ticket_text):
    if ticket_text.strip() == "":
        return "Please enter a support ticket description."

    result = classifier(ticket_text, CATEGORIES)
    return result["labels"][0]

interface = gr.Interface(
    fn=auto_tag_ticket,
    inputs=gr.Textbox(
        lines=4,
        placeholder="Enter support ticket text..."
    ),
    outputs="text",
    title="Auto-Tagging Support Tickets Using LLM",
    description="Automatically classifies customer support tickets using a pretrained LLM."
)

if __name__ == "__main__":
    interface.launch()
