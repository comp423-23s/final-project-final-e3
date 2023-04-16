import { Injectable } from '@angular/core';
import { Room } from './reservations.service';

export interface TimeSlot {
  startTime: string;
  endTime: string;
  timeInterval: string | null | undefined;
}

export interface Schedule {
  Sunday: TimeSlot;
  Monday: TimeSlot;
  Tuesday: TimeSlot ;
  Wednesday: TimeSlot;
  Thursday: TimeSlot;
  Friday: TimeSlot;
  Saturday: TimeSlot;
}

@Injectable({
  providedIn: 'root'
})
export class TimesService {

  constructor() { }
}
