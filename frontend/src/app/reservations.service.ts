import { Injectable } from '@angular/core';
import { Profile } from './profile/profile.service';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Room {
  name: string
  // availability: myMap[string: (arg0: string, arg1: string)]
  max_capacity: number
}

let myMap = new Map<string,string> ([
  ["key1", "value1"],
  ["key2", "value2"]
]);

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

