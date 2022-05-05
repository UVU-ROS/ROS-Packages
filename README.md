# ROS-Packages
Many of the files in catkin_ws are system dependent. That can make sharing files through a github repository tricky. The strategy we chose to employ can be found at https://answers.ros.org/question/257855/git-strategy-for-catkin-and-package-folders/. The file structure should resemble the following

```
workspace_folder/
  src/
    repo_with_pkgs/  <-- git repo
      package_a/
      package_b/
      .
      .
      .
```
The `workspace_folder` is the directory of your specific `catkin_ws`. If you need help creating a catkin_ws see http://wiki.ros.org/catkin/Tutorials/create_a_workspace
# Usage
To utilize the basic packages contained here, you should clone this repository into the `<catkin_ws>/src` directory then call `catkin_make` in the base `catkin_ws directory`
```
cd ~/catkin_ws/src
git clone git@github.com:UVU-ROS/ROS-Packages.git
cd ~/catkin_ws
catkin_make
```
You can then use the packages as you would any other ROS package.


*Note for the clone step you may need to setup ssh keys with your github account. That is left to the reader*
