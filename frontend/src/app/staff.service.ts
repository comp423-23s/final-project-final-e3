import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Reservations } from './reservations.service';
import { Observable } from 'rxjs';

export interface ReservationID{
  reservation_id: string;
}

@Injectable({
  providedIn: 'root'
})
export class StaffService {

  constructor(protected http: HttpClient) { }

  listAllReservations() {
    return this.http.get<Reservations[]>("/api/reserve")
  }

  listUserReservations(pid: number) {
    return this.http.get<Reservations[]>(`/api/reserve/${pid}`)
  }

//   deleteMyReservatoin(reservation_id: string): Observable<Reservations>
//   {
//     return this.http.delete<Reservations>(`/api/reserve/${reservation_id}`)
//   }
}


