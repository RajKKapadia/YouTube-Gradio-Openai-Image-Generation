import gradio as gr

from utils import handle_input

demo = gr.Interface(
    fn=handle_input,
    inputs=gr.components.Textbox(label='Write your prompt...'),
    outputs=gr.components.Image(label='Output', type='pil', height=512, width=512),
    allow_flagging='never'
)

if __name__ == '__main__':
    demo.launch()
