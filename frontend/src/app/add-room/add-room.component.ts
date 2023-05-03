import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Route } from '@angular/router';
import { Observable } from 'rxjs';
import { isAuthenticated } from '../gate/gate.guard';
import { ReservationsService, Room } from '../reservations.service';
import { FormBuilder, Validators } from '@angular/forms';
import { AddRoomService } from '../add-room.service';
import { Schedule } from '../times.service';

@Component({
  selector: 'app-add-room',
  templateUrl: './add-room.component.html',
  styleUrls: ['./add-room.component.css']
})
export class AddRoomComponent{
  public static Route: Route = {
    path: 'add-room',
    component: AddRoomComponent, 
    title: 'Add Resources',  

  };

  public newRoomForm;

  constructor(protected formBuilder: FormBuilder, protected addRoomService: AddRoomService) {
    this.newRoomForm = this.formBuilder.group({
      room_name: ['', Validators.required],
      room_capacity: ['', Validators.required],
      monday_start: ['', Validators.required],
      monday_end: ['', Validators.required],
      tuesday_start: ['', Validators.required],
      tuesday_end: ['', Validators.required],
      wednesday_start: ['', Validators.required],
      wednesday_end: ['', Validators.required],
      thursday_start: ['', Validators.required],
      thursday_end: ['', Validators.required],
      friday_start: ['', Validators.required],
      friday_end: ['', Validators.required],
      saturday_start: ['', Validators.required],
      saturday_end: ['', Validators.required],
      sunday_start: ['', Validators.required],
      sunday_end: ['', Validators.required],
      time_interval: ['', Validators.required],
    });
  }

  onSubmit(): void {
    
    let form = this.newRoomForm.value;
    
    let room_name = form.room_name ?? "";
    let capacity = parseInt(form.room_capacity ?? "");
    let schedule : Schedule = { Sunday: [form.sunday_start?? "", form.sunday_end??"", form.time_interval??""]
      ,Monday: [form.monday_start?? "", form.monday_end??"", form.time_interval??""],
       Tuesday:[form.tuesday_start?? "", form.tuesday_end??"", form.time_interval??""], 
       Wednesday: [form.wednesday_start?? "", form.wednesday_end??"", form.time_interval??""], 
       Thursday: [form.thursday_start?? "", form.thursday_end??"", form.time_interval??""], 
       Friday: [form.friday_start?? "", form.friday_end??"", form.time_interval??""], 
       Saturday: [form.saturday_start?? "", form.saturday_end??"", form.time_interval??""]
    }
    this.addRoomService.create_room(room_name, capacity, schedule).subscribe(
      {
        next: (room) => this.onSuccess(room),
        error: (err) => this.onError(err)
      } 
    );
  }

  private onSuccess(room: Room) {
   
    window.alert(`The resource has been added.`);
    this.newRoomForm.reset();
  }

  private onError(err: any) {
    window.alert(`The room has already been added, please double check.`)
  }
}
