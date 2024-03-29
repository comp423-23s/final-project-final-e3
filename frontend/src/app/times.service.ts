import { Injectable } from '@angular/core';
import { Room } from './reservations.service';
import { HttpClient } from '@angular/common/http';



export interface Schedule {
  Sunday: string[];
  Monday: string[];
  Tuesday: string[];
  Wednesday: string[];
  Thursday: string[];
  Friday: string[];
  Saturday: string[];
}

export interface AvailableTimes {
  [date: string]: Array<[startTime: string, endTime: string]>;
}


@Injectable({
  providedIn: 'root'
})
export class TimesService {

  constructor(protected http: HttpClient) { }

  getTimes(roomName: string | null) {
    return this.http.get<AvailableTimes>(`/api/room/${roomName}`);
  }
}


