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
}
