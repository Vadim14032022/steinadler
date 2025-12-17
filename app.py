import gradio as gr
import os

# Define video paths
VIDEO_DIR = "assets/video"
VIDEO_PAIRS = {
    "Bottle Scene": {
        "original": os.path.join(VIDEO_DIR, "bottle_orig.mp4"),
        "processed": os.path.join(VIDEO_DIR, "bottle_tom++.mp4")
    },
    "Coda Scene": {
        "original": os.path.join(VIDEO_DIR, "coda_orig.mp4"),
        "processed": os.path.join(VIDEO_DIR, "coda_tom++.mp4")
    },
    "ITLP Scene": {
        "original": os.path.join(VIDEO_DIR, "itlp_orig.mp4"),
        "processed": os.path.join(VIDEO_DIR, "itlp_tom++.mp4")
    }
}

def create_comparison_interface():

    with gr.Blocks(title="Diploma Research Demo - Tom++ Video Processing") as demo:
        gr.Markdown("""
        # Diploma Research Demo
        """)

        with gr.Row():
            scene_selector = gr.Dropdown(
                choices=list(VIDEO_PAIRS.keys()),
                label="Select Scene",
                value="Bottle Scene",
                interactive=True
            )

        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### 📹 Original Video")
                original_video = gr.Video(
                    label="Original",
                    show_label=False,
                    height=400
                )

            with gr.Column(scale=1):
                gr.Markdown("### ✨ Tom++ Processed Video")
                processed_video = gr.Video(
                    label="Tom++ Processed",
                    show_label=False,
                    height=400
                )

        # Function to update videos when scene changes
        def update_videos(scene):
            if scene in VIDEO_PAIRS:
                return (
                    VIDEO_PAIRS[scene]["original"],
                    VIDEO_PAIRS[scene]["processed"]
                )
            return None, None

        # Set up the interaction
        scene_selector.change(
            fn=update_videos,
            inputs=scene_selector,
            outputs=[original_video, processed_video]
        )

        # Initialize with first scene
        demo.load(
            fn=lambda: update_videos("Bottle Scene"),
            outputs=[original_video, processed_video]
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
        theme=gr.themes.Soft()
    )
