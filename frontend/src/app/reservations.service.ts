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



@Injectable({
  providedIn: 'root'
})
export class ReservationsService {

  // public reservations$: Observable<Profile | undefined>;
  constructor(protected http: HttpClient) { }

    list_of_rooms() {
      return this.http.get<Room[]>("/api/room");
    }

    addReservation(identifier_id: string, roomName: string, pid: number, start_time: string, end_time: string) : Observable<Reservations>{
      let reserve: Reservations = {identifier_id: identifier_id, pid: pid, subject_name: roomName, start: start_time, end: end_time}
      return this.http.post<Reservations>("/api/reserve", reserve)
    }
}

export interface Reservations {
  identifier_id: string
  pid: number
  subject_name: string
  start: string
  end: string
}

