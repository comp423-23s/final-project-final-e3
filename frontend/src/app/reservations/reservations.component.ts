import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { Observable } from 'rxjs';
import { isAuthenticated } from '../gate/gate.guard';
import{ ReservationsService, Room } from 'src/app/reservations.service'


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

  constructor(private reservationService: ReservationsService){
    this.rooms$ = reservationService.list_of_rooms();
  }

}