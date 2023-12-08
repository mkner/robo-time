
Design
------


This project evolved in the course of designing and implementing an OS for mobile robotics. In particular, small differential drive robots. These robots are both individual mobile robots and interactive robots in a dynamic distributed mobile environment.

Mobile robots exist in the continuous cycle of modes of See, Think and Do. Of necessity, there are ongoing questions a mobile robot needs to answer:

Where am I? What do I see? What am I doing? What am I going to do? Where do I go? How do I get there? When do I get there? Then what? And What next? 

And for every motion oriented task, the starting point always goes back to the fundamentals: perception of the environment and localization in that environment.

Perception is based on continuous measurements and readings from electronic and electro-mechanical and possibly electro-chemical devices. These sensors measure various aspects of the environment, both external and internal. Mobile robotic perception starts at this interface.

The interpretation of incoming measurements and their associated events have one thing in common. They all depend on some primary representation of time, relative time and time synchronization. There are also reference frames in which time occurs: inter-machine, localized intra-machine, and global intra-machine. 

Inter-machine events are measured and recorded with respect to the various representations of a clock counting or quantizing time as discrete units. For electro-mechanical robots and devices this occurs on a microprocessor or microchip level. The robots OS and operational programs usually work on a much higher level. But the common entry reference point is the beginning of the system startup on an electronic level. In other words uptime. And relative offsets to the ongoing forward moving uptime form the first reference point for localized inter-machine time related events.

An **uptime clock** is the primary and primordial clock. This clock provides an interface representing uptime in common units of measurement as seconds, milliseconds, microseconds, and nanoseconds if available. This stream is then available in standard partitions of seconds, minutes, hours, days, years. Even though an uptime clock has no historical or cultural basis for any sense of what a calendar is, it has a fundamental way of partitioning an extended ongoing count of time into a calendar-like system. It uses a symmetric calendar that is logically divided into 360 days for a year; the same number of degrees in a circle. The calendar has 12 months where each month has 30 days. The main idea here is to keep longer spans of uptime in a generic
timezone and  calendar independent form. The output can always be reformatted and reconfigured for specific application
dependent requirements.


The **system clock** provides the same basic features as an uptime clock but also in a localized time and calendar system that is relative to world geography and related zone standards. This localized timezone and format is set in the operating system configuration that the robotic or computer system is running on. 

The **world clock** provides the same basic features as an uptime clock and also represents time in an absolute, but still localized to a particular planet, time reference frame. This clock and its calendar system is synchronized to the global UTC time standard via the NTP protocol.

Each clock type has the *same* common interface for basic date, time and timestamp functions in frequently used
formats and data types. This isomorphic pattern across the clock types is by design in the object oriented structure of 
the clock type classes. Having the same unified interface makes the implementaton of different clock types a lot easier. 





