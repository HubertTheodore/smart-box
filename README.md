# Smart Box

As a group of 4, we designed and created a box that can move to a destination in the form of 2 different input commands from a website. It also has the ability to detect if the box is still moving and if an object has been caught. 

My responsibility was to create the front end and the back end using React and Express.js as well as hosting the website on the virtual machine.

## Table of Contents

- [Design and Implementation](#designAndImplementation)
- [Final Result](#finalResult)

## Design and Implementation <a name="designAndImplementation"></a>

We used UBC ECE's virtual machine in order to host the website using Nginx. For hardware, we used 1 Motion Detection Sensor (PIR) to detect when the object has been caught in the box, 4 stepper motors to move the box, 2 sonar sensors to help calculate where the box is in the "field" and a Raspberry Pi Pico W to connect to the internet and back end of the project.

The following diagrams show the logic behind both the hardware and software components:

![hardware](https://github.com/HubertTheodore/smart-box/assets/55958230/71057070-299f-478b-b617-326e54e4f5f8)

Software:

![software](https://github.com/HubertTheodore/smart-box/assets/55958230/8118c997-cc76-4d94-a561-a63c0c8c0ff1)

Hardware fritzing:

![fritzing](https://github.com/HubertTheodore/smart-box/assets/55958230/ff9100f9-822a-48ed-88d1-c51225aa251a)

Pictures of the physical circuit:

![box1](https://github.com/HubertTheodore/smart-box/assets/55958230/a6e9227c-09c7-45e4-9a9f-ab80e65c3664)
![box2](https://github.com/HubertTheodore/smart-box/assets/55958230/d3b15c79-42e2-4c49-a477-47e918bce011)

## Final Result <a name="finalResult"></a>

[Smart Box Demo](https://www.youtube.com/watch?v=lUScERJdyYA)

![boxfinal](https://github.com/HubertTheodore/smart-box/assets/55958230/3859d95b-9a75-401e-99d5-457df560ebcd)
