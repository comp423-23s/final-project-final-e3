import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Route } from '@angular/router';
import { Observable } from 'rxjs';
import { isAuthenticated } from '../gate/gate.guard';
import { ReservationsService, Room } from '../reservations.service';
import { ReservationsComponent } from '../reservations/reservations.component';
import { ManagementService } from '../management.service';
import { Form, FormBuilder, Validators } from '@angular/forms';
import { AddRoomService } from '../add-room.service';

@Component({
  selector: 'app-add-room',
  templateUrl: './add-room.component.html',
  styleUrls: ['./add-room.component.css']
})
export class AddRoomComponent implements OnInit{
  public static Route: Route = {
    path: 'add-room',
    component: AddRoomComponent, 
    title: 'add-room',  
  };

  public newRoom: Room;

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
    munday_end: '',
    time_interval: '',
  });

  constructor(route: ActivatedRoute, protected formBuilder: FormBuilder, protected addRoomService: AddRoomService) {
    const form = this.newRoomForm;
    form.get('room_name')?.addValidators(Validators.required);
    form.get('room_capacity')?.addValidators(Validators.required);
    form.get('monday_start')?.addValidators(Validators.required);
    form.get('monday_end')?.addValidators(Validators.required);
    form.get('tuesday_start')?.addValidators(Validators.required);
    form.get('tuesday_end')?.addValidators(Validators.required);
    form.get('wednesday_start')?.addValidators(Validators.required);
    form.get('wednesday_end')?.addValidators(Validators.required);
    form.get('thursay_start')?.addValidators(Validators.required);
    form.get('thurday_end')?.addValidators(Validators.required);
    form.get('friday_start')?.addValidators(Validators.required);
    form.get('friday_end')?.addValidators(Validators.required);
    form.get('saturday_start')?.addValidators(Validators.required);
    form.get('saturday_end')?.addValidators(Validators.required);
    form.get('sunday_start')?.addValidators(Validators.required);
    form.get('sunday_end')?.addValidators(Validators.required);
    form.get('time_interval')?.addValidators(Validators.required);
    

    const data = route.snapshot.data as { room: Room };
    this.newRoom = data.room;
  }

  ngOnInit(): void {
    let newRoom = this.newRoom;

    // this.newRoomForm.setValue({
    //   room_name: newRoom.name,
    //   room_capacity: newRoom.max_capacity,
    //   // monday_start: newRoom.monday,
    //   // monday_end: '',
    //   // tuesday_start: '',
    //   // tuesday_end: '',
    //   // wednesday_start: '',
    //   // wednesday_end: '',
    //   // thursday_start: '',
    //   // thursday_end: '',
    //   // friday_start: '',
    //   // friday_end: '',
    //   // saturday_start: '',
    //   // saturday_end: '',
    //   // sunday_start: '',
    //   // munday_end: '',
    //   // time_interval: '',
    // });
  }

  onSubmit(): void {
    if (this.newRoomForm.valid) {
      // Object.assign(this.newRoom, this.newRoom.value)
      this.addRoomService.put(this.newRoom).subscribe(
        {
          next: (room) => this.onSuccess(room),
          error: (err) => this.onError(err)
        } 
      );
    }
  }

  private onSuccess(room: Room) {
    
  }

  private onError(err: any) {
    console.error("How to handle this?");
  }
}
