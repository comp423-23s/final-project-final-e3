import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { isAuthenticated } from '../gate/gate.guard';
import { Observable, Subscription } from 'rxjs';
import { Reservations } from '../reservations.service';
import { StaffService } from '../staff.service';
import { ProfileService } from '../profile/profile.service';

@Component({
  selector: 'app-myreservations',
  templateUrl: './myreservations.component.html',
  styleUrls: ['./myreservations.component.css']
})
export class MyreservationsComponent {
  public static Route: Route = {
    path: 'myreservations',
    component: MyreservationsComponent, 
    title: 'My Reservations', 
    canActivate: [isAuthenticated], 
  };

  public reservations$: Observable<Reservations[]>
  public pid: number|undefined;
  public subscription: Subscription | undefined

  constructor(private staffService: StaffService, private profileService: ProfileService){
    this.subscription = this.profileService.getUserId().subscribe(pid => this.pid);
    this.reservations$ = staffService.listUserReservations(this.pid);

  }

  // getPID() {
  //   let pid:string = prompt("Please enter your pid", "0")!;
  //   let pid_num: number | null = parseInt(pid);
  //   this.pid = pid_num;
  //   this.getMyReservations(this.pid);
  // }
  
  getMyReservations() {
    console.log(this.pid)
    this.reservations$ = this.staffService.listUserReservations(this.pid);
  }

  deleteMyReservation(id: String) {
    console.log(id);
    this.staffService.deleteReservation(id).subscribe( {
      next: (reservations) => this.onSuccess(reservations)
    });
  }

  onSuccess(reservation: Reservations) {
    window.location.reload();
  }
}
