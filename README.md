# Wanderlust-HashCode21

traffic light

red 
fgreen

task 
minimize  - time spent in traffic to reach
before deadline

City Plan

One way streets and inse


The city plan consists of one-way streets and intersections. Each street:
● is identi ed by a unique name,
● leads from one intersection to another,
● does not contain any intersections in between (if two streets need to cross
outside an intersection, a bridge or tunnel is used),
● has a  xed amount of time L it takes a car to get from the beginning of the
street to the end. If it takes L seconds to drive through a street and a car enters it at time T it will arrive at the end of the street precisely at T+L, independently of how many cars are on the street.


Traffic Lights

At most one traffic light will be green at each intersection at any given time. While the light is green for an incoming street, only cars from this street will be allowed to enter the intersection (and move to any outcoming street), all other cars have to wait.

When the light is green, one car can cross the intersection every second. 

This means that if a green light for a given street lasts for Ti
2
seconds then only the  rst Ti cars from that street will continue their travel (see Figure 2). Others will need to wait for the following green light.

Schedule
For each intersection we can set a tra c light schedule. The tra c light schedule determines the order and duration of green light for the incoming streets of the intersection and repeats itself until the end of the simulation. The schedule is a list of pairs: incoming street and duration. Each street can appear at most once in
3
the schedule. The schedule can ignore some of the incoming streets – those will never get a green light.

Cars
Each car is described by the path (a sequence of streets) it is going to drive through. No changes in path allowed.single intersection at most once.
all cars start at the end of the  rst street in their path,
If two cars sta  at the end of the same street,the car listed  rst in the input  le goes  rst. 

Cars are queued up at the end of each street. The  rst car in the queue can cross the intersection immediately a er the light turns green.

no delay in intersections

What happens in the last street?
When a car enters the last street of its path, it completes its drive until the end of the street and then is immediately removed from it. This means that the car does not queue up at the end of the last street of its path and does not enter the intersection at the end of it.


