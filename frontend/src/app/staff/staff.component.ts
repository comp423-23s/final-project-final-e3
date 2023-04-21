import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { isAuthenticated } from '../gate/gate.guard';
import { Reservations, ReservationsService } from '../reservations.service';
import { Observable } from 'rxjs';
import { TimesService } from '../times.service';
import { HttpClient } from '@angular/common/http';
import { StaffService } from '../staff.service';

@Component({
  selector: 'app-staff',
  templateUrl: './staff.component.html',
  styleUrls: ['./staff.component.css']
})
export class StaffComponent {
  public static Route: Route = {
    path: 'staff',
    component: StaffComponent, 
    title: 'Staff Page', 
    canActivate: [isAuthenticated], 
  };

  public reservations$: Observable<Reservations[]>

  constructor(private staffService: StaffService){
    this.reservations$ = staffService.listAllReservations();
  }
}
