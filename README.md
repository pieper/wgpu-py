# FORK OF wgpu-py for testing with 3D Slicer - not offical

This version includes a modified qt.py file for testing with [3D Slicer](http://slicer.org).

Works on Windows and Linux.  Currently does not work on Mac, possibly due to Qt version issue.

Steps for testing:
* clone this repository and cd into it
* run /path/to/PythonSlicer download-wgpu-native.py
* run /path/to/PythonSlicer -m pip install .

Then paste this in the Python console to try out some demos:
>>>>>>> 92a5414 (Add readme info for this fork)
```
import glob

demos = qt.QWidget()
layout = qt.QVBoxLayout()
demos.setLayout(layout)
for example in glob.glob("./examples/shadertoy*.py"):
    button = qt.QPushButton(example)
    layout.addWidget(button)
    button.connect("clicked()", lambda e=example: exec(open(e).read()))
demos.show()
```

Of course, seeing ShaderToy demos is not the end goal.  The wgpu interface with PythonQt support in Slicer opens the door to use all kinds of cross-platform GPU-based techniques in Slicer, such as the demos in [SlicerWGPU](https://github.com/pieper/SlicerWGPU) and eventually [pygfx](https://github.com/pygfx/pygfx) together with VTK.

See [https://github.com/pygfx/wgpu-py](https://github.com/pygfx/wgpu-py) for the original readme.
