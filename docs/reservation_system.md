# Room and Equipment Reservation System

## Overview
Our feature enables users to add, delete, and manage reservations of the resources available in the XSL lab. This feature will primarily serve students and educators who may benefit from an easy and straightforward way to access these resources. 

Our feature gives provides different functionality based on the roles of each user. The two primary roles are staff and student. The student role allows access to view available rooms and equipment to reserve, create new reservations, and delete or modify existing reservations. The core philosophy of the student role is that the user only has full access to reservations pertaining to itself, and has access to minimal information about other student roles within the system. On the other hand, the staff role allows the user to have full access to the database. Staff roles are able to add, delete, and manage new rooms and equipment available for the student role to reserve. Moreover, it has access to all reservations in the system and can delete or modify existing reservations for any user on the system. 

## Implementation Notes
**Room Model**

| property_name | value_type                               |
|---------------|------------------------------------------|
| name          | str                                      |
| max_capacity  | int                                      |
| availability  | Dict [str : (str, str, str) ]            |
| deviations    | Dict [str: list [ tuple(str, str), … ] ] |

**Availability Example**

template:

"Day of the week": ["start_time", "end_time", "interval"]

example:

availability = {

    "Monday": ["08:00", "17:00", "1"],
    "Tuesday": ["08:00", "17:00", "1"],
    "Wednesday": ["08:00", "16:00", "1"],
    "Thursday": ["08:00", "17:00", "1"],
    "Friday": ["08:00", "18:00", "0.5"],
    "Saturday": ["10:00", "16:00", "1"],
    "Sunday": ["10:00", "16:00", "1"]
}

(Equipment model is similar to room model despite the removal of max_capacity)

**Schdule and Deviations**

Our implementation offers flexibility when dealing with schedule deviations. We accomplish this by separately keeping track of a room's original “default” schedule, as well as any deviations from this original schedule planned by the administrator. 

When creating a room, the availability passed in is considered the default schedule. Time slots will be generated according to this schedule on the fly. Time slots are kept track of through a schedule dictionary, which will have keys from the current Sunday up to and including next Saturday. 

**Creating Deviations**

Override the schedule for specific days by providing a Deviation dictionary. It is formatted the same as a Schedule Dictionary. 

**Deviation Example**

template:

"date": ["new_start_time", "new_end_time", "new_interval"]

example:

deviation = {

    "04/15": ["14:00", "19:00", "1"]
    "04/28": ["13:00", "19:00", "1"]
}

Note: All entries only affect the date they correspond to. Future weeks will not be affected. Expired deviations will be removed automatically. 

| Room Functionality      |
|--------------------|
| List_rooms         |
| List_room_schedule |
| Edit_room_schedule |
| Add_room           |
| Delete_room        |

Only staff could add and delete rooms. User logged in as a staff could see Management page on the side bar, and they can add, delete, and modify rooms there. The user's staff permission will be validated automatically before room operations being executed. 

**Reservation Model**

| property_name | value_type |
|---------------|------------|
| identifier_id | str        |
| pid           | int        |
| subject_name  | str        |
| start         | str        |
| end           | str        |

Identifier_id is a concatenated string of subject_name, user_pid, and date-time of the reservation start time

| Reservation Functionality                            |
|------------------------------------------|
| List_reservation (room or user specific) |
| List_all_reservations                    |
| Add_reservation                          |
| Delete_reservation                       |

Regular user could see their reservations in myReservation page. Only user with a staff role could see all active reservations in Staff page.

## Developer Notes
Developers should first familiarize themselves with the data models and API routes listed above. Having a solid understanding of how the frontend and backend communicate information is essential to working with the codebase. 

To get started, look through the routes in the API module. Then, familiarize yourself with the services model and see what functionalities this feature offer. Finally, move on to data models and entities. 

## Future Work
In the coming days, we will add comprehensive error reporting. A challenge is to balance reliability with speed and simplicity. Moreover, we hope to find ways to scale our system to larger databases. 