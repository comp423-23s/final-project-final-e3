import { Injectable, InjectableType } from '@angular/core';
import { Profile } from './profile/profile.service';
import { HttpClient } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import{ Schedule} from './times.service'
import { JsonPipe } from '@angular/common';

export interface Room {
  name: string
  max_capacity: number
  availability: Schedule;
  deviations: {}
};

export interface Reservations {
  identifier_id: String
  pid: number | undefined
  subject_name: string | null
  start: String
  end: String
}



@Injectable({
  providedIn: 'root'
})
export class ReservationsService {

  public room_name: string | undefined;
  constructor(protected http: HttpClient) { }


    list_of_rooms() {
      return this.http.get<Room[]>("/api/room");
    }

    addReservation(identifier_id: String, roomName: string | null, pid: number | undefined, start_time: String, end_time: String) : Observable<Reservations>{
      let reserve: Reservations = {identifier_id: identifier_id, pid: pid, subject_name: roomName, start: start_time, end: end_time}
      return this.http.post<Reservations>("/api/reserve", reserve)
    }

    setRoomName(roomName: string){
      this.room_name = roomName;
    }

    getRoomName() {
      return this.room_name;
    }
}


