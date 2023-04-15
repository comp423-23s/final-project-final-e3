import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { mergeMap, Observable, of, shareReplay } from 'rxjs';
import { Room } from './reservations.service';

@Injectable({
  providedIn: 'root'
})
export class AddRoomService {

  constructor(protected http: HttpClient) { 

  }

  put(room: Room) {
    return this.http.put<Room>("/api/profile", room);
  }
}
