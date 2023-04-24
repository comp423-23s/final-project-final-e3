import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { Observable } from 'rxjs';
import { isAuthenticated } from '../gate/gate.guard';
import{ Reservations, ReservationsService, Room } from 'src/app/reservations.service'
import { AvailableTimes, Schedule, TimesService } from '../times.service';
import { HttpClient } from '@angular/common/http';

import * as crypto from 'crypto-ts';
import { Profile, ProfileService } from '../profile/profile.service';
const SHA256 = require("crypto-ts").SHA256;

@Component({
  selector: 'app-reservations',
  templateUrl: './reservations.component.html',
  styleUrls: ['./reservations.component.css']
})
export class ReservationsComponent {
  public static Route: Route = {
    path: 'reservations',
    component: ReservationsComponent, 
    title: 'Reservations', 
    canActivate: [isAuthenticated], 
  };

  public rooms$: Observable<Room[]>;
  public times$: Observable<AvailableTimes> | null;
  public room_name: String;
  public profile$: Observable<Profile | undefined>;
  public pid: number;

  constructor(private reservationService: ReservationsService, private timeService: TimesService, protected http: HttpClient, private profileService: ProfileService){
    this.rooms$ = reservationService.list_of_rooms();
    this.times$ = timeService.getTimes("A1");
    this.room_name = "1"
    this.profile$ = this.profileService.profile$;
    this.pid = 0;
    this.profile$.subscribe(profile => {
      if(profile) {
        console.log(profile.pid);
        this.pid = profile.pid
      } else {
        console.error("Profile does not exists")
      }
    })
  }

  displayTimes(roomName: string) {
    this.times$ = this.timeService.getTimes(roomName);
    this.room_name = roomName;
  }

  reserveRoom(roomName: String, start_time: String, end_time: String, date: String) { 
    this.room_name = roomName;

    let new_start = `${start_time}-${date}`
    let new_end = `${end_time}-${date}`
    let identifier_id = `${roomName}-${this.pid}-${new_start}`.replace(":", "").replace("/", "")
    // const identifier_id_hashed = crypto.createHash('sha256').update(identifier_id).digest('hex');
    console.log(identifier_id);
    this.reservationService.addReservation(identifier_id, roomName, this.pid, new_start, new_end).subscribe(
      {
        next: (reservation) => this.onSuccess(reservation),
        error: (err) => this.onError(err)
      } 
    );
  }

  private onSuccess(reservation: Reservations) {
    window.alert("Your reservation has been added.");
  }

  private onError(err: any) {
    if (err.message) {
      window.alert(err.message);
    } else {
      window.alert("Unknown error: " + JSON.stringify(err));
    }
  }
}