import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { isAuthenticated } from '../gate/gate.guard';

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
}