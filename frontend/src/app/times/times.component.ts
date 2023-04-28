import { Component } from '@angular/core';
import { Route, ActivatedRoute } from '@angular/router';
import { TimesService, Schedule, AvailableTimes } from '../times.service';
import { Reservations, ReservationsService, Room } from '../reservations.service';
import { Observable } from 'rxjs';
import { Profile, ProfileService } from '../profile/profile.service';


@Component({
  selector: 'app-times',
  templateUrl: './times.component.html',
  styleUrls: ['./times.component.css']
})
export class TimesComponent {
  public static Route: Route = {
    path: 'times/:roomName',
    component: TimesComponent, 
    title: 'Times', 
  };

  public times$: Observable<AvailableTimes> | undefined; 
  public profile$: Observable<Profile| undefined>;
  public pid: number|undefined;
  public room_name: string | null;

  constructor(private reservationService: ReservationsService, private timeService: TimesService, private profileService: ProfileService, private route: ActivatedRoute){

    this.profile$ = this.profileService.profile$;
    this.profile$.subscribe(profile => {
      if(profile) {
        console.log(profile.pid);
        this.pid = profile.pid
      } else {
        console.error("Profile does not exists")
      }
    })
    this.room_name = this.route.snapshot.paramMap.get('roomName');
    this.times$ = this.timeService.getTimes(this.room_name);
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
