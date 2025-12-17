import gradio as gr
import os
from gradio.themes import Base

class WhiteLightGreenTheme(Base):
    def __init__(self):
        super().__init__()
        self.primary_hue = "green"
        self.secondary_hue = "green"
        self.neutral_hue = "gray"

VIDEO_DIR = "assets/video"
VIDEO_PAIRS = {
    "Bottle Scene": {
        "original": os.path.join(VIDEO_DIR, "bottle_orig.mp4"),
        "processed": os.path.join(VIDEO_DIR, "bottle_tom++.mp4"),
        "depth": os.path.join(VIDEO_DIR, "bottle_depth.mp4"),
        "objects": ["bottle", "hand", "box", "table", "paper", "floor", "wristband"]
    },
    "Coda Scene": {
        "original": os.path.join(VIDEO_DIR, "coda_orig.mp4"),
        "processed": os.path.join(VIDEO_DIR, "coda_tom++.mp4"),
        "depth": os.path.join(VIDEO_DIR, "coda_depth.mp4"),
        "objects": ["road", "human", "door", "ellivator", "carpet", "bin", "tree"]
    },
    "ITLP Scene": {
        "original": os.path.join(VIDEO_DIR, "itlp_orig.mp4"),
        "processed": os.path.join(VIDEO_DIR, "itlp_tom++.mp4"),
        "depth": os.path.join(VIDEO_DIR, "itlp_depth.mp4"),
        "objects": ["robot", "road", "tree", "car"]
    }
}

def create_comparison_interface():

    with gr.Blocks(title="Diploma Research Demo - Tom++ Video Processing") as demo:
        gr.Markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
        <h1 style="font-size: 48px; font-weight: bold; color: #DFF2E9; margin: 20px 0;">
        Diploma Research Demo
        </h1>
        </div>
        """)

        gr.Markdown("""
        <div style="text-align: center;">
        <a href="https://github.com/Vadim14032022/steinadler" target="_blank">Demo Repository</a> |
        <a href="https://github.com/Vadim14032022/tom_project" target="_blank">Original Repository with Method</a>
        </div>
        """)

        with gr.Row():
            pdf_download = gr.DownloadButton(
                "Diploma PDF",
                value="assets/diploma.pdf"
            )

        with gr.Row():
            scene_selector = gr.Dropdown(
                choices=list(VIDEO_PAIRS.keys()),
                label="Select Scene",
                value="Bottle Scene",
                interactive=True
            )

        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### Original Video")
                original_video = gr.Video(
                    label="Original",
                    show_label=False,
                    height=400
                )

            with gr.Column(scale=1):
                gr.Markdown("### Tom++ Processed Video")
                processed_video = gr.Video(
                    label="Tom++ Processed",
                    show_label=False,
                    height=400
                )

        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### Depth Video")
                depth_video = gr.Video(
                    label="Depth",
                    show_label=False,
                    height=400
                )

            with gr.Column(scale=1):
                gr.Markdown("### Detected Objects")
                object_list = gr.JSON(
                    label="Objects",
                    show_label=False
                )

        # Function to update videos when scene changes
        def update_videos(scene):
            if scene in VIDEO_PAIRS:
                return (
                    VIDEO_PAIRS[scene]["original"],
                    VIDEO_PAIRS[scene]["processed"],
                    VIDEO_PAIRS[scene]["depth"],
                    VIDEO_PAIRS[scene]["objects"]
                )
            return None, None, None, []

        # Set up the interaction
        scene_selector.change(
            fn=update_videos,
            inputs=scene_selector,
            outputs=[original_video, processed_video, depth_video, object_list]
        )

        # Initialize with first scene
        demo.load(
            fn=lambda: update_videos("Bottle Scene"),
            outputs=[original_video, processed_video, depth_video, object_list]
        )

    return demo

if __name__ == "__main__":
    # Create and launch the demo
    demo = create_comparison_interface()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        show_error=True,
        share=False,
        theme=WhiteLightGreenTheme()
    )
