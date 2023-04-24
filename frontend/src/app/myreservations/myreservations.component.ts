import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { isAuthenticated } from '../gate/gate.guard';
import { Observable, Subscription } from 'rxjs';
import { Reservations } from '../reservations.service';
import { StaffService } from '../staff.service';
import { ProfileService, Profile } from '../profile/profile.service';

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
  public profile$: Observable<Profile | undefined>;

  constructor(private staffService: StaffService, private profileService: ProfileService){
    this.profile$ = this.profileService.profile$;
    this.profile$.subscribe(profile => {
      if(profile) {
        console.log(profile.pid);
        this.pid = profile.pid
      } else {
        console.error("Profile does not exists")
      }
    })
    this.reservations$ = staffService.listUserReservations(this.pid);
  }
  
  getMyReservations() {
    this.reservations$ = this.staffService.listUserReservations(this.pid);
  }

  deleteMyReservation(id: String) {
    this.staffService.deleteReservation(id).subscribe( {
      next: (reservations) => this.onSuccess(reservations)
    });
  }

  onSuccess(reservation: Reservations) {
    window.alert("Your reservation has been deleted.")
    // window.location.reload();
  }
}
