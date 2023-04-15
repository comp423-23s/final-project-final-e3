import { Injectable } from '@angular/core';
import { Profile } from './profile/profile.service';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Room {
  name: string
  max_capacity: string
  monday: string[] | null
  tuesday: string[] | null
  wednesday: string[] | null
  thursday: string[] | null
  friday: string[] | null
  saturday: string[] | null
  sunday: string[] | null
  time_interval: string | null
}


@Injectable({
  providedIn: 'root'
})
export class ReservationsService {

  // public reservations$: Observable<Profile | undefined>;
  constructor(protected http: HttpClient) { }

    list_of_rooms() {
        return this.http.get<Room[]>("/api/room");
    }
  
}

