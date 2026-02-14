# src/carla_interface/sensors.py
import carla
import os

class CameraRecorder:
    def __init__(self, world, vehicle, out_dir="output/frames", fps=20):
        self.world = world
        self.vehicle = vehicle
        self.out_dir = out_dir
        self.fps = fps
        os.makedirs(self.out_dir, exist_ok=True)
        self.frame_idx = 0
        self.camera = None

    def spawn_camera(self):
        bp_lib = self.world.get_blueprint_library()
        cam_bp = bp_lib.find("sensor.camera.rgb")
        cam_bp.set_attribute("image_size_x", "800")
        cam_bp.set_attribute("image_size_y", "600")
        cam_bp.set_attribute("fov", "90")

        transform = carla.Transform(
            carla.Location(x=1.5, z=2.0),  # hood camera
            carla.Rotation(pitch=-10)
        )
        self.camera = self.world.spawn_actor(cam_bp, transform, attach_to=self.vehicle)
        self.camera.listen(self._callback)

    def _callback(self, image):
        filename = os.path.join(self.out_dir, f"frame_{self.frame_idx:06d}.png")
        image.save_to_disk(filename)
        self.frame_idx += 1

    def destroy(self):
        if self.camera is not None:
            self.camera.stop()
            self.camera.destroy()
