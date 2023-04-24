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
  public times$: Observable<AvailableTimes> | undefined; 
  public profile$: Observable<Profile| undefined>;
  public pid: number|undefined;
  public room_name: string|undefined;

  constructor(private reservationService: ReservationsService, private timeService: TimesService, protected http: HttpClient, private profileService: ProfileService){
    this.rooms$ = reservationService.list_of_rooms();

    this.profile$ = this.profileService.profile$;
    this.profile$.subscribe(profile => {
      if(profile) {
        console.log(profile.pid);
        this.pid = profile.pid
      } else {
        console.error("Profile does not exists")
      }
    })
  }

  setRoomName(roomName: string) {
    this.room_name = roomName;
  }

  getRoomName() {
    return this.room_name;
  }

  displayTimes(roomName: string) {
    this.room_name = roomName;
    this.times$ = this.timeService.getTimes(roomName);
  }

  reserveRoom(start_time: String, end_time: String, date: String) { 

    let new_start = `${start_time}-${date}`
    let new_end = `${end_time}-${date}`
    let identifier_id = `${this.room_name}-${this.pid}-${new_start}`.replace(":", "").replace("/", "")
    console.log(identifier_id);
    this.reservationService.addReservation(identifier_id, this.room_name, this.pid, new_start, new_end).subscribe(
      {
        next: (reservation) => this.onSuccess(reservation),
        error: (err) => this.onError(err)
      } 
    );
  }

  private onSuccess(reservation: Reservations) {
    window.alert("Your reservation has been added.");
    window.location.reload();
  }

  private onError(err: any) {
    if (err.message) {
      window.alert(err.message);
    } else {
      window.alert("Unknown error: " + JSON.stringify(err));
    }
  }
}