import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Route } from '@angular/router';
import { Observable } from 'rxjs';
import { isAuthenticated } from '../gate/gate.guard';
import { ReservationsService, Room } from '../reservations.service';
import { ReservationsComponent } from '../reservations/reservations.component';
import { ManagementService } from '../management.service';
import { Form, FormBuilder, Validators } from '@angular/forms';
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
    title: 'add-room',  
  };

  public newRoomForm = this.formBuilder.group({
    room_name: '',
    room_capacity: '',
    monday_start: '',
    monday_end: '',
    tuesday_start: '',
    tuesday_end: '',
    wednesday_start: '',
    wednesday_end: '',
    thursday_start: '',
    thursday_end: '',
    friday_start: '',
    friday_end: '',
    saturday_start: '',
    saturday_end: '',
    sunday_start: '',
    sunday_end: '',
    time_interval: '',
  });

  constructor(protected formBuilder: FormBuilder, protected addRoomService: AddRoomService) {
    // const form = this.newRoomForm;
    // form.get('room_name')?.addValidators(Validators.required);
    // form.get('room_capacity')?.addValidators(Validators.required);
    // form.get('monday_start')?.addValidators(Validators.required);
    // form.get('monday_end')?.addValidators(Validators.required);
    // form.get('tuesday_start')?.addValidators(Validators.required);
    // form.get('tuesday_end')?.addValidators(Validators.required);
    // form.get('wednesday_start')?.addValidators(Validators.required);
    // form.get('wednesday_end')?.addValidators(Validators.required);
    // form.get('thursay_start')?.addValidators(Validators.required);
    // form.get('thurday_end')?.addValidators(Validators.required);
    // form.get('friday_start')?.addValidators(Validators.required);
    // form.get('friday_end')?.addValidators(Validators.required);
    // form.get('saturday_start')?.addValidators(Validators.required);
    // form.get('saturday_end')?.addValidators(Validators.required);
    // form.get('sunday_start')?.addValidators(Validators.required);
    // form.get('sunday_end')?.addValidators(Validators.required);
    // form.get('time_interval')?.addValidators(Validators.required);
    

    // const data = route.snapshot.data as { room: Room };
    // this.newRoom = data.room;
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
   
    window.alert(`The room has been added.`);
    this.newRoomForm.reset();
  }

  private onError(err: any) {
    if (err.message) {
      window.alert(err.message);
    } else {
      window.alert("Unknown error: " + JSON.stringify(err));
    }
  }
}
