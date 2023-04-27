import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { mergeMap, Observable, of, shareReplay } from 'rxjs';
import { Room } from './reservations.service';
import{Schedule} from './times.service'

export interface Deviations {
  [date: string]: string[];
}

@Injectable({
  providedIn: 'root'
})
export class AddRoomService {

  constructor(protected http: HttpClient) { 

  }

  create_room(room_name: string, room_capacity: number, week_schedule: Schedule) : Observable<Room> {
    let room: Room = {name: room_name, max_capacity: room_capacity, availability: week_schedule, deviations: {}}
    return this.http.post<Room>("/api/room", room);
  }
  
  modify_room(room_name: string | undefined, deviations: Deviations){
    return this.http.post<Room>(`/api/room/edit/${room_name}`, deviations)
  }
  
}
