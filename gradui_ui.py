import gradio as gr

from utils import handle_input

demo = gr.Interface(
    fn=handle_input,
    inputs=[gr.components.Textbox(label='Write your prompt...'),
            gr.components.Number(label='Number of images'),
            gr.components.Dropdown(choices=['1024x1024', '512x512', '256x256'], label='Image size')],
    outputs=gr.components.Gallery(label='Output'),
    allow_flagging='never'
)

if __name__ == '__main__':
    demo.launch()
