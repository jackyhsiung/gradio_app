import gradio as gr


def greet(name):
    return "Hello " + name + "!"


demo = gr.Interface(fn=greet, inputs="textbox",
                    outputs="textbox", server_name="0.0.0.0")

if __name__ == "__main__":
    demo.launch()
