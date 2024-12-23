import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import Canvas
import cv2
import os
from PIL import Image, ImageTk

class VideoTrimmerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Trimmer")

        # File selection
        self.file_label = tk.Label(root, text="No file selected")
        self.file_label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Video", command=self.select_video)
        self.select_button.pack(pady=5)

        # Range slider
        self.slider_frame = tk.Frame(root)
        self.slider_frame.pack(pady=10)

        self.start_label = tk.Label(self.slider_frame, text="Start:")
        self.start_label.pack(side=tk.LEFT)

        self.start_slider = tk.Scale(self.slider_frame, from_=0, to=100, orient=tk.HORIZONTAL, length=200, command=lambda x: self.update_preview('start'))
        self.start_slider.pack(side=tk.LEFT)

        self.end_label = tk.Label(self.slider_frame, text="End:")
        self.end_label.pack(side=tk.LEFT)

        self.end_slider = tk.Scale(self.slider_frame, from_=0, to=100, orient=tk.HORIZONTAL, length=200, command=lambda x: self.update_preview('end'))
        self.end_slider.pack(side=tk.LEFT)

        # Video preview
        self.preview_label = tk.Label(root, text="Video Preview:")
        self.preview_label.pack(pady=10)

        self.canvas = Canvas(root, width=320, height=240, bg="black")
        self.canvas.pack()

        # Output button
        self.output_button = tk.Button(root, text="Trim and Save", command=self.trim_video, state=tk.DISABLED)
        self.output_button.pack(pady=20)

        self.video_path = None
        self.video_duration = 0
        self.cap = None

    def select_video(self):
        self.video_path = filedialog.askopenfilename(
            filetypes=[("Video files", "*.mp4;*.avi;*.mov;*.mkv")]
        )
        if self.video_path:
            self.cap = cv2.VideoCapture(self.video_path)
            if not self.cap.isOpened():
                messagebox.showerror("Error", "Unable to open video file.")
                return

            self.video_duration = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT) / self.cap.get(cv2.CAP_PROP_FPS))

            self.file_label.config(text=f"Selected: {os.path.basename(self.video_path)}")
            self.start_slider.config(to=self.video_duration)
            self.end_slider.config(to=self.video_duration)
            self.end_slider.set(self.video_duration)
            self.output_button.config(state=tk.NORMAL)

            self.update_preview('start')
        else:
            self.file_label.config(text="No file selected")

    def update_preview(self, slider):
        if self.cap and self.cap.isOpened():
            if slider == 'start':
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.start_slider.get() * self.cap.get(cv2.CAP_PROP_FPS))
            elif slider == 'end':
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.end_slider.get() * self.cap.get(cv2.CAP_PROP_FPS))

            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (320, 240))
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
                self.canvas.image = imgtk

    def trim_video(self):
        start_time = self.start_slider.get()
        end_time = self.end_slider.get()

        if not self.video_path:
            messagebox.showerror("Error", "No video file selected.")
            return

        if start_time >= end_time or end_time > self.video_duration:
            messagebox.showerror("Error", "Invalid time range selected.")
            return

        try:
            cap = cv2.VideoCapture(self.video_path)
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')

            output_path = filedialog.asksaveasfilename(
                defaultextension=".mp4",
                filetypes=[("MP4 files", "*.mp4")]
            )
            if not output_path:
                cap.release()
                return

            out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
            cap.set(cv2.CAP_PROP_POS_FRAMES, start_time * fps)

            total_frames = int((end_time - start_time) * fps)
            frame_count = 0

            while frame_count < total_frames:
                ret, frame = cap.read()
                if not ret:
                    break
                out.write(frame)
                frame_count += 1

            cap.release()
            out.release()

            messagebox.showinfo("Success", f"Video saved to {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = VideoTrimmerApp(root)
    root.mainloop()
