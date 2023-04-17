import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { Observable } from 'rxjs';
import { isAuthenticated } from '../gate/gate.guard';
import{ ReservationsService, Room } from 'src/app/reservations.service'
import { AvailableTimes, Schedule, TimesService } from '../times.service';
import { HttpClient } from '@angular/common/http';


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

  constructor(private reservationService: ReservationsService, private timeService: TimesService, protected http: HttpClient){
    this.rooms$ = reservationService.list_of_rooms();
    this.times$ = timeService.getTimes("A7");
  }

  displayTimes(roomName: String) {
    this.times$ = this.timeService.getTimes(roomName);
  }
}