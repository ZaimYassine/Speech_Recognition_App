import sounddevice as sd

# List all available audio devices
print(sd.query_devices())

# Alternatively, list only input devices
input_devices = [device for device in sd.query_devices() if device['max_input_channels'] > 0]
for i, device in enumerate(input_devices):
    print(f"Device {i}: {device['name']}, ID: {device['index']}")