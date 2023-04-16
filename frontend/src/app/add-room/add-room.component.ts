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
    let schedule : Schedule = { Sunday: {
      startTime: form.sunday_start?? "", endTime: form.sunday_end??"", timeInterval: form.time_interval},Monday: {
      startTime: form.monday_start?? "", endTime: form.monday_end??"", timeInterval: form.time_interval}, Tuesday: {
        startTime: form.tuesday_start?? "", endTime: form.tuesday_end??"", timeInterval: form.time_interval}, Wednesday: {
          startTime: form.wednesday_start?? "", endTime: form.wednesday_end??"", timeInterval: form.time_interval}, Thursday: {
            startTime: form.thursday_start?? "", endTime: form.thursday_end??"", timeInterval: form.time_interval}, Friday: {
                startTime: form.friday_start?? "", endTime: form.friday_end??"", timeInterval: form.time_interval}, Saturday: {
                  startTime: form.saturday_start?? "", endTime: form.saturday_end??"", timeInterval: form.time_interval}
    }
    console.log(room_name)
    console.log(capacity)
    console.log(schedule.Friday.startTime)
    console.log(schedule.Friday.endTime)
    console.log(schedule.Friday.timeInterval)
    console.log(schedule)
    this.addRoomService.create_room(room_name, capacity, schedule).subscribe(
      {
        next: (room) => this.onSuccess(room),
        error: (err) => this.onError(err)
      } 
    );
    
  }

  private onSuccess(room: Room) {
   
    window.alert(`The room ${room.name} has been added.`);
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
