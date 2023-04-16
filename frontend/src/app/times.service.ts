import { Injectable } from '@angular/core';
import { Room } from './reservations.service';



export interface Schedule {
  Sunday: string[];
  Monday: string[];
  Tuesday: string[];
  Wednesday: string[];
  Thursday: string[];
  Friday: string[];
  Saturday: string[];
}


@Injectable({
  providedIn: 'root'
})
export class TimesService {

  constructor() { }
}
