# Smart Box

As a group of 4, we designed and created a box that can move to a destination in the form of 2 different input commands from a website. It also has the ability to detect if the box is still moving and if an object has been caught. My responsibility was to create the front end and the back end using React and Express.js as well as hosting the website on the virtual machine.

## Table of Contents

- (Design and Implementation)[#designAndImplementation]
- (Final Result)[#finalResult]

## Design and Implementation <a name="designAndImplementation"></a>

We used UBC ECE's virtual machine in order to host the website using Nginx. For hardware, we used 1 Motion Detection Sensor (PIR) to detect when the object has been caught in the box, 4 stepper motors to move the box, 2 sonar sensors to help calculate where the box is in the "field" and a Raspberry Pi Pico W to connect to the internet and back end of the project.

The following diagrams show the logic behind both the hardware and software components:

![hardware](https://github.com/HubertTheodore/smart-box/assets/55958230/77980295-62d7-4d00-aedd-7f88f0fd0d74)

Software:

![software](https://github.com/HubertTheodore/smart-box/assets/55958230/b1bf3a7c-6dec-482b-8927-ca5effa1ff95)

Hardware fritzing and pictures of the physical circuit:

![fritzing](https://github.com/HubertTheodore/smart-box/assets/55958230/b0a4c4c5-125f-4724-a8c3-1688c9f05636)
![box1](https://github.com/HubertTheodore/smart-box/assets/55958230/f1bdceb2-7d6d-4fe6-b732-4bcf9f9050b3)
![box2](https://github.com/HubertTheodore/smart-box/assets/55958230/91417b92-e4fa-4b2d-9744-08f014e5148e)

## Final Result <a name="finalResult"></a>

(Smart Box Demo)[https://www.youtube.com/watch?v=lUScERJdyYA]

![boxfinal](https://github.com/HubertTheodore/smart-box/assets/55958230/beaf499c-4f9e-4880-a56d-37cbc13bd5f7)
