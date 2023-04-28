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

  constructor(private reservationService: ReservationsService, private timeService: TimesService, private profileService: ProfileService){
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
    this.reservationService.setRoomName(roomName);
  }

}