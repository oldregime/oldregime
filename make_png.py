from PIL import Image
import numpy as np

img = Image.open('/mnt/personal file/from w11/github/profile_cropped.jpg').convert('L')
data = np.array(img)
alpha = 255 - data

# Dark mode text color: #c9d1d9 -> RGB(201, 209, 217)
dark_rgb = np.zeros((*data.shape, 3), dtype=np.uint8)
dark_rgb[:, :, 0] = 201
dark_rgb[:, :, 1] = 209
dark_rgb[:, :, 2] = 217

dark_rgba = np.dstack((dark_rgb, alpha))
Image.fromarray(dark_rgba, 'RGBA').save('/mnt/personal file/from w11/github/oldregime_readme/profile_dark.png')

# Light mode text color: #24292f -> RGB(36, 41, 47)
light_rgb = np.zeros((*data.shape, 3), dtype=np.uint8)
light_rgb[:, :, 0] = 36
light_rgb[:, :, 1] = 41
light_rgb[:, :, 2] = 47

light_rgba = np.dstack((light_rgb, alpha))
Image.fromarray(light_rgba, 'RGBA').save('/mnt/personal file/from w11/github/oldregime_readme/profile_light.png')

print("Created transparent PNGs!")
