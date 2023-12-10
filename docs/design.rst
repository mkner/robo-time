
Design
------


This project evolved in the course of designing and implementing an OS for mobile robotics. In particular, small differential drive robots. These robots are both individual mobile robots and interactive robots in a dynamic distributed mobile environment.

Mobile robots exist in the continuous cycle of modes of See, Think and Do. Of necessity, there are ongoing questions a mobile robot needs to answer:

Where am I? What do I see? What am I doing? What am I going to do? Where do I go? How do I get there? When do I get there? Then what? And What next? 

And for every motion oriented task, the starting point always goes back to the fundamentals: perception of the environment and localization in that environment.

Perception is based on time-based measurements and readings from various analog and digital electro-sensory devices. These sensors measure various aspects of the environment, both external and internal. Mobile robotic perception starts at this interface.

The interpretation of incoming measurements and their associated events have one thing in common. They all depend on some primary representation of time, relative time and time synchronization. There are also reference frames in which time occurs: inter-machine, localized intra-machine, and global intra-machine. 

Events are measured and recorded with respect to various representations of a clock counting or quantizing time as discrete units. For electro-mechanical robots and devices this first occurs on a microprocessor or microchip level. Even though the robots OS and operational programs usually work on a much higher level, the common entry point of discretized time is the beginning of the system startup on a micro-electronic level.  Uptime is the relative offset to this ongoing forward moving time and forms a reference point for localized time related events.

The **uptime clock** is a primary and primordial clock. This clock provides an interface representing uptime in common units of measurement as seconds, milliseconds, microseconds, and nanoseconds if available. This monotonically increasing count of discrete time units is then available in standard partitions of seconds, minutes, hours, days, years. 

The **system clock** provides the same basic features as an uptime clock but also in a localized time and calendar system that is relative to world geography and related zone standards. This localized timezone and format is set in the operating system configuration that the robotic or computer system is running on. 

The **world clock** provides the same basic features as an uptime clock and also represents time in an absolute, but still localized to a particular planet, time reference frame. This clock and its calendar system is synchronized to the global UTC time standard via the NTP protocol.

Each clock type has the *same* common interface for basic date, time and timestamp functions in frequently used
formats and data types. This isomorphic pattern across the clock types is by design in the object oriented structure of 
the clock type classes. Having the same unified interface makes the implementaton of different clock types a lot easier. 





