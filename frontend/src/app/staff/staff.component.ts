import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { isAuthenticated } from '../gate/gate.guard';

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
}
