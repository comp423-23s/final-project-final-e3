import { Component } from '@angular/core';
import { Route } from '@angular/router';
import { Observable } from 'rxjs';
import { isAuthenticated } from '../gate/gate.guard';
import{ Reservations, ReservationsService, Room } from 'src/app/reservations.service'
import { AvailableTimes, Schedule, TimesService } from '../times.service';
import { Form, FormBuilder, Validators } from '@angular/forms';
import { Deviations } from '../add-room.service';
import { AddRoomService } from '../add-room.service';

@Component({
  selector: 'app-deviations',
  templateUrl: './deviations.component.html',
  styleUrls: ['./deviations.component.css']
})
export class DeviationsComponent {
  public static Route: Route = {
    path: 'deviations',
    component: DeviationsComponent, 
    title: 'Deviations', 
  };

  public room_name: string|undefined;

  public newDeviationsForm;


  constructor(protected formBuilder: FormBuilder, protected reservationService: ReservationsService, protected addRoomService: AddRoomService) {
    this.room_name = this.reservationService.getRoomName();
    this.newDeviationsForm = this.formBuilder.group({
      modified_date: ['', Validators.required],
      new_start_time: ['', Validators.required],
      new_end_time: ['', Validators.required],
      new_time_interval: ['', Validators.required],
    });
  }

  onSubmit(): void {
    
    let form = this.newDeviationsForm.value;


    let modified_date = form.modified_date ?? "";
    let modified_dateNoYear = modified_date.substring(modified_date.length - 5)
    let final_date = modified_dateNoYear.substring(0,2) + '/' + modified_dateNoYear.substring(3);
    let start_time = form.new_start_time ?? "";
    let end_time = form.new_end_time ?? "";
    let time_interval = form.new_time_interval ?? "";

    let new_deviations: Deviations = {[final_date]: [start_time, end_time, time_interval]}

    this.addRoomService.modify_room(this.room_name, new_deviations).subscribe(
      {
        next: () => this.onSuccess(),
        error: (err) => this.onError(err)
      } 
    );
    
  }

  private onSuccess() {
    window.alert(`The time has been changed!`);
    this.newDeviationsForm.reset();
  }

  private onError(err: any) {
    if (err.message) {
      window.alert(err.message);
    } else {
      window.alert("Unknown error: " + JSON.stringify(err));
    }
  }

}
