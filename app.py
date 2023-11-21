from transformers import pipeline
import gradio as gr


class summarizer:
    model = pipeline("summarization")

    def predict(self, prompt):
        summary = self.model(prompt)[0]["summary_text"]
        return summary


def hello():
    print("Hello, dude!")


s = summarizer()
with gr.Blocks() as demo:
    textbox = gr.Textbox(placeholder="Enter text to summarize", lines=4)
    gr.Interface(fn=s.predict, inputs=textbox, outputs="text")
demo.launch()
