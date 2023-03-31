import { Injectable } from '@angular/core';
import { Profile } from './profile/profile.service';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Room {
  id: number
  name: string
  max_capacity: number
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

