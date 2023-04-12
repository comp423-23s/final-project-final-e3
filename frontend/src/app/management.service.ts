import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Room } from './reservations.service';

@Injectable({
  providedIn: 'root'
})
export class ManagementService {

  constructor(protected http: HttpClient) { }

  deleteRoom(roomName: string): Observable<Room>
  {
    return this.http.delete<Room>(`/api/room/${roomName}`)
  }
}