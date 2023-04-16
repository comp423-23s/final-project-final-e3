import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { mergeMap, Observable, of, shareReplay } from 'rxjs';
import { Room } from './reservations.service';
import{Schedule, TimeSlot} from './times.service'

@Injectable({
  providedIn: 'root'
})
export class AddRoomService {

  constructor(protected http: HttpClient) { 

  }

  create_room(room_name: string, room_capacity: number, week_schedule: Schedule) : Observable<Room> {
    let room: Room = {name: room_name, max_capacity: room_capacity, schedule: week_schedule}
    return this.http.post<Room>("/api/room", room);
  }
}
