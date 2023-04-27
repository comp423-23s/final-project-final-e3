import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Reservations } from './reservations.service';

@Injectable({
  providedIn: 'root'
})
export class StaffService {

  constructor(protected http: HttpClient) { }

  listAllReservations() {
    return this.http.get<Reservations[]>("/api/reserve")
  }

  listUserReservations(pid: number|null) {
    return this.http.get<Reservations[]>(`/api/reserve/${pid}`)
  }

  deleteMyReservation(reservation_id: string) {
    return this.http.delete<Reservations>(`/api/reserve/${reservation_id}`)
  }
}
