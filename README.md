using_markers package from [rviz/Tutorials](http://wiki.ros.org/rviz/Tutorials)

## Contents

* Original C++ sources from tutorial

* rviz customization files for basic_shapes and points_and_lines examples

* launchers for rviz-only and rviz + package

* Python ports of basic_shapes and points_and_lines

## How to run:

### Launching rviz and node separately:

* C++
 
```
roslaunch using_markers basic_shapes.launch
rosrun using_markers basic_shapes
```
```
roslaunch using_markers points_and_lines.launch
rosrun using_markers points_and_lines
```

* Python

```
roslaunch using_markers basic_shapes.launch
rosrun using_markers basic_shapes.py
```
```
roslaunch using_markers points_and_lines.launch
rosrun using_markers points_and_lines.py
```

### Launch rviz and node simultaneously

* C++

```
roslaunch using_markers basic_shapes_cpp.launch
```
```
roslaunch using_markers points_and_lines_cpp.launch
```

* Python

```
roslaunch using_markers basic_shapes_py.launch
```
```
roslaunch using_markers points_and_lines_py.launch
```
