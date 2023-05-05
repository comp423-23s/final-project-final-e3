# Resource Reservation System

Team Members: 
[Evan Liu](https://github.com/evanliu0062),
[Yinuo Liu](https://github.com/YinuoLiu0708),
[Tianyi Niu](https://github.com/tianyiniu),
[Alexander Zheng](https://github.com/alexz957unc)

## Overview
Our feature enables users to add, delete, and manage reservations of resources available in the XSL lab. This feature will primarily serve students and educators who may benefit from an easy and straightforward way to access these resources. 

Our project gives provides different functionality based on the roles of each user. The two primary roles are staff and student. The student role allows access to view available rooms and equipment to reserve, create new reservations, and delete or modify existing reservations. The core philosophy of the student role is that the user only has full access to reservations pertaining to itself, and has access to minimal information about other student roles within the system. On the other hand, the staff role allows the user to have full access to the database. Staff roles are able to add, delete, and manage new rooms and equipment available for the student role to reserve. Moreover, it has access to all reservations in the system. 

### **Usage Examples**

**User Functionality**

View all available resources including room and equipment:
![list_rooms](/docs/images/available_rooms.png)

View all reservable times for a resource and make reservation by clicking a time slot:
![list_reservations](/docs/images/make_reservation.png)

View all active reservations made by the logged-in user:
![student_all_reservations](/docs/images/student_all_reservations.png)

**Staff Functionality**

Staff functionality is a superset of user functionality.

View all active reservations as staff:
![staff_all_reservations](/docs/images/staff_all_reservations.png)

Manage Existing Resources:
![manage_resources](/docs/images/add_delete_rooms.png)

Add a new resource as staff:
![new_room](/docs/images/add_room.png)

Modify Schedule for a resource:
![deviation](/docs/images/modify_resource_schedule.png)

## Implementation Notes

### **Resource Model**

| Field | Type                                             |
|---------------|------------------------------------------|
| name          | str                                      |
| max_capacity  | int                                      |
| availability  | Dict [str : (str, str, str) ]            |
| deviations    | Dict [str: list [ tuple(str, str), … ] ] |

For rooms, name should be formatted as "Room-R{Room No.}", and for equipment, "{Equipment_Name}-{Name 1st letter}{Equipment No.}"
This naming format is not enforced. 
etc. "Room-R1" and "Monitor-M1"

Note that this formatting standard is not enforced. 

**Availability**

Template:

```
"Day of the week": ["start_time", "end_time", "interval"]
```

Example:

```
availability = { 
    "Monday": ["08:00", "17:00", "1"],
    "Tuesday": ["08:00", "17:00", "1"],
    "Wednesday": ["08:00", "16:00", "1"],
    "Thursday": ["08:00", "17:00", "1"],
    "Friday": ["08:00", "18:00", "0.5"],
    "Saturday": ["10:00", "16:00", "1"],
    "Sunday": ["10:00", "16:00", "1"]
}
```

**Schdule and Deviations**

Our implementation offers flexibility when dealing with schedule deviations. We accomplish this by separately keeping track of a room's original “default” schedule, as well as any deviations from this original schedule planned by the administrator. 

When creating a room, the availability passed in is considered the default schedule. Time slots will be generated according to this schedule on the fly. Time slots are kept track of through a schedule dictionary, which will have keys from **the current Sunday up to and including next Saturday**. 

**Creating Deviations**

Override the schedule for specific days by providing a Deviation dictionary. It is formatted the same as a Schedule Dictionary. 

Template:

```
"MM/DD": ["new_start_time", "new_end_time", "new_interval"]
```

Example:

```
deviation = {
    "04/15": ["14:00", "19:00", "1"]
    "04/28": ["13:00", "19:00", "1"]
}
```

Note: All entries only affect the date they correspond to. Future weeks will not be affected. Expired deviations will be removed automatically. 

| Room Functionality | Route | Parameters: type |
|--------------------|-------|------------|
| List_rooms         | GET("/api/room/") | N/A |
| List_room_schedule | GET("/api/room/{room_name}") | room_name:str|
| Edit_room_schedule | POST("/api/room/edit/{room_name}") | user_pid: int, room_name: str, deviation: Deviation Dict | 
| Add_room           | POST("/api/room/") | user_pid: int, room: Room |
| Delete_room        | DELETE("/api/room/{room_name}") | user_pid: int, room_name: str | 

Only staff could add and delete rooms. User logged in as a staff could see Management page on the side bar, and they can add, delete, and modify rooms there. The user's staff permission will be validated automatically before room operations being executed. 


### **Reservation Model**

| Field | Type       |
|---------------|------------|
| identifier_id | str        |
| pid           | int        |
| subject_name  | str        |
| start         | str        |
| end           | str        |

Identifier_id is a concatenated string of subject_name, user_pid, and date-time of the reservation start time

Example Reservation Object

```
reservation = {
    identifier_id = "Room-R1-123456789-1300-0310",
    pid = 123456789, 
    subject_name = "Room-R1", 
    start = "13:00-03/10", 
    end = "14:00-03/10"
}
```

| Reservation Functionality                | Route | Parameters: type |
|------------------------------------------|-------|------------|
| List_all_reservations | GET("/api/reserve") | N/A | 
| List_reservation (room or user specific)                  | GET("/api/reserve/{subject_name_or_pid}) | subject_name_or_pid: str/int |  
| Add_reservation                          | POST("/api/reserve") | reservation: Reservation | 
| Delete_reservation                       | DELETE("api/reserve/{reservation_id}") | reservation_id: str |

Regular user could see their reservations in myReservation page. Only user with a staff role could see all active reservations in Staff page.

## Developer and Design Notes
Our primary philosophy when designing the backend is simplicity. We aim to represent all our information in the most efficient and simplest way possible. A reservation is defined by three pieces of information: start time, end time, user, and subject. Originally, we hoped to represent the reservation using complex objects: 

```
reservation = {
    subject: Resource_object,
    User: User_object,
    Start: Time_object,
    End: Time_object
}
```

However, this design quickly ran into issues. The usage of complex objects means that this object is not inhrent JSON-encodable. To send information to the frontend, this Reservation object will have to undergo preprocessing, adding significant overhead. Moreover, the lower database also does not accept such objects. Writing to database thus also requires extra processing. 

The solution is to encode everything as String. Since the user's PID is unique, the room's name is unique, and each time slot's start/end time is unique, it is much simpler to represent these four fields as simple strings. While this approach does reduce processing time translating between data models and entities, it does create overhead when reading from the database. Future developers can balance these two approaches to find middle ground between simplicity and speed. 


## Future Work
A challenge is to balance reliability with speed and simplicity. Moreover, we hope to find ways to scale our system to larger databases. 

Moreover, we hope to add a notification component to our feature. A user should be able to be notified upon any changes to their reservation, either through email or text.

Finally, a manager should also be able to change (lengthen or shorten) the window of active reservations. Currently, the window is fixed at two weeks, from last Sunday to next Saturday. Just as with deviations and schedules, a manager will find flexile window sizes helpful in adapting to sudden increases in demand. 