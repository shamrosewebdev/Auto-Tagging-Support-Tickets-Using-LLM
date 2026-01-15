<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Auto-Tagging Support Tickets Using LLM</title>
</head>
<body>

<h1>Task 5: Auto-Tagging Support Tickets Using Large Language Models (LLMs)</h1>

<h2>Objective</h2>
<p>
The objective of this task is to build an intelligent auto-tagging system that automatically
classifies customer support tickets into predefined categories using a pretrained Large Language Model (LLM).
The solution focuses on prompt-based and zero-shot classification without requiring model training.
</p>

<hr>

<h2>Problem Description</h2>
<p>
Customer support teams receive a large volume of text-based tickets every day.
Manually assigning categories to these tickets is time-consuming and error-prone.
This project automates the ticket classification process using LLMs to improve efficiency
and response time.
</p>

<hr>

<h2>Dataset</h2>
<p>
This task uses a flexible dataset approach:
</p>
<ul>
    <li>Sample or custom-generated support ticket texts</li>
    <li>No fixed dataset size required</li>
    <li>Focus is on LLM inference rather than training</li>
</ul>

<p>
Example ticket categories include:
</p>
<ul>
    <li>Billing</li>
    <li>Technical Issue</li>
    <li>Account Support</li>
    <li>Service Request</li>
    <li>General Inquiry</li>
</ul>

<hr>

<h2>Approach &amp; Methodology</h2>

<h3>1. Category Definition</h3>
<p>
A predefined list of realistic support ticket categories was created to guide the classification process.
</p>

<h3>2. Zero-Shot Classification</h3>
<p>
A pretrained transformer-based Large Language Model was used in zero-shot mode.
This allows the model to classify text into categories without any additional training.
</p>

<h3>3. LLM Inference</h3>
<ul>
    <li>Ticket text is passed as input to the LLM</li>
    <li>The model evaluates semantic similarity between the text and category labels</li>
    <li>The most relevant category is selected automatically</li>
</ul>

<h3>4. Confidence Scoring</h3>
<p>
The model also provides confidence scores, helping assess prediction reliability.
</p>

<h3>5. Deployment</h3>
<p>
A lightweight interactive interface was created using Gradio to allow users
to input support tickets and receive real-time category predictions.
</p>

<hr>

<h2>Model Used</h2>
<ul>
    <li>facebook/bart-large-mnli (Zero-Shot Classification)</li>
</ul>

<hr>

<h2>Key Results</h2>
<ul>
    <li>Successfully automated support ticket categorization</li>
    <li>No model training required</li>
    <li>Accurate and fast predictions using pretrained LLMs</li>
    <li>Demonstrated practical use of prompt-based AI systems</li>
</ul>

<hr>

<h2>Tools &amp; Libraries</h2>
<ul>
    <li>Python</li>
    <li>Hugging Face Transformers</li>
    <li>Gradio</li>
</ul>

<hr>

<h2>Example Usage</h2>
<pre><code>
Ticket: "I was charged twice for my monthly subscription"
Output: Billing
</code></pre>

<hr>

<h2>Skills Demonstrated</h2>
<ul>
    <li>Large Language Model (LLM) inference</li>
    <li>Zero-shot text classification</li>
    <li>Prompt-based NLP solutions</li>
    <li>Lightweight AI deployment</li>
    <li>Real-world customer support automation</li>
</ul>

<hr>

<h2>Notes</h2>
<p>
This project emphasizes practical usage of pretrained LLMs for real-world business problems.
It demonstrates how modern AI systems can be leveraged without heavy training or infrastructure requirements.
</p>

<hr>

<h2>Shamrose Khan</h2>
<p>
Internship Project – AI / Machine Learning
</p>

</body>
</html>

