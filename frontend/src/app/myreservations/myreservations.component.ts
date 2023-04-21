import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { isAuthenticated } from '../gate/gate.guard';
import { Observable } from 'rxjs';
import { Reservations } from '../reservations.service';
import { StaffService } from '../staff.service';
import { ReservationID } from '../staff.service';

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
  public pid: number;

  constructor(private staffService: StaffService){
    this.pid = 0;
    this.reservations$ = staffService.listUserReservations(this.pid);

  }

  getPID() {
    let pid:string = prompt("Please enter your pid", "0")!;
    let pid_num: number | null = parseInt(pid);
    this.pid = pid_num;
    this.getMyReservations(this.pid);
    console.log(pid);
  }
  
  getMyReservations(pid: number) {
    this.reservations$ = this.staffService.listUserReservations(pid);
  }

  // deleteMyReservation(reservation_id: string) {
  //   this.staffService.deleteMyReservation(reservation_id).subscribe( {
  //     next: (reservation) => this.onSuccess(reservation),
  //       error: (err) => this.onError(err)
  //   });
  // }

  onSuccess(reservation: Reservations) {
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
